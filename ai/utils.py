import os
from datetime import datetime
import pickle
import face_recognition
from initialize_firebase import *

def load_encoded_faces():
    blob = bucket.blob('EncodeFile.p')
    blob.download_to_filename('EncodeFile.p')
    with open('EncodeFile.p', 'rb') as f:
        return pickle.load(f)

encodeListKnown, studentIds = load_encoded_faces()
encodeListKnown,studentIds
def add_user(name):
    new_user=users_ref.push({'name': name })
    return new_user.key

def add_pictures(user_id,folderPath="dataset"):
     for image in os.listdir(os.path.join(folderPath, user_id)):
        fileName = f'{folderPath}/{user_id}/{image}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)


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



