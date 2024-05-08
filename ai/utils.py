import os
from datetime import datetime
import pickle
import face_recognition
import tempfile
from initialize_firebase import *

def load_encoded_faces():
    blob = bucket.blob('EncodeFile.p')
    blob.download_to_filename('EncodeFile.p')
    with open('EncodeFile.p', 'rb') as f:
        return pickle.load(f)

encodeListKnown, studentIds = load_encoded_faces()

def add_user(name, file):
    # Check if the name already exists in the database
    query = users_ref.order_by_child('name').equal_to(name).get()
    if query:
        # If the name already exists, return False
        return False

    # Add the new user to the database
    new_user = users_ref.push({'name': name, "last_presence": ""})
    user_id = new_user.key
    
    # Call add_pictures_of_user function and return its result
    return add_pictures_of_user(user_id, file)


def add_pictures_of_user(user_id,file):
    # Create a temporary file to store the uploaded image
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file.save(temp_file.name)

        # Upload the file to Firebase Storage
        filename = f'dataset/{user_id}/{file.filename}'
        bucket = storage.bucket()
        blob = bucket.blob(filename)
        
        try:
            blob.upload_from_filename(temp_file.name)
        except Exception as e:
            # If an error occurs during upload, delete the user and return False
            users_ref.child(user_id).delete()
            os.unlink(temp_file.name)
            return False

    # Delete the temporary file
    os.unlink(temp_file.name)
    return True



# Function to identify person from image
def identify_person_from_image(image_path):
    # Load image
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) == 0:
        return {'name': 'Unknown', 'id': None}

    # Compare face encodings
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(encodeListKnown, face_encoding)
        if True in matches:
            person_index = matches.index(True) // 3
            person_id = studentIds[person_index]  # get person_id
            person_data = users_ref.child(person_id).get()
            person_name = person_data['name']
            last_presence = person_data.get('last_presence')
            isLastPresenceUpdating = False
            if last_presence:
                # Check if last presence is more than 2 hours ago
                last_presence_datetime = datetime.strptime(last_presence, '%Y-%m-%d %H:%M:%S')
                time_difference = datetime.now() - last_presence_datetime
                if time_difference.total_seconds() / 3600 > 2:
                    # Update value of last_presence
                    users_ref.child(person_id).update({'last_presence': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    isLastPresenceUpdating = True
            else:
                # Add value to last_presence
                users_ref.child(person_id).update({'last_presence': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                isLastPresenceUpdating = True

            if isLastPresenceUpdating:
                return {'name': person_name, 'id': person_id, 'last_presence_updated': True}
            else:
                return {'name': person_name, 'id': person_id, 'last_presence_updated': False}

    return {'name': 'Unknown', 'id': None, 'last_presence_updated': False}



