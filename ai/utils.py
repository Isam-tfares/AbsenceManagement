import os
import cv2
from datetime import datetime
import face_recognition
from initialize_firebase import *
from EncodeGenerator import *
from PIL import Image
import shutil

encodeListKnown, studentIds = get_encoded_images()

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
    ret,fileName = add_pictures_of_user(user_id, file)
    if ret:
        # Update the EncodeFile.p with the new encoding
        global encodeListKnown, studentIds
        imgList=[cv2.imread(fileName)]
        encodeListKnown, studentIds=update_encode_file(imgList,[user_id],encodeListKnown,studentIds)
    return ret


def add_pictures_of_user(user_id,file):

    pil_image = Image.open(file).convert("RGB")
    # Create the directory
    directory = f'dataset/{user_id}'
    os.makedirs(directory, exist_ok=True)
    # Save the image
    image_name=file.filename.rsplit('.', 1)[0].lower() + '.jpg'
    filename_path=os.path.join(f'dataset/{user_id}/', image_name)
    pil_image.save(filename_path)
    # Upload the image in DB
    bucket = storage.bucket()
    blob = bucket.blob(filename_path)
    try:
        blob.upload_from_filename(filename_path)
    except Exception as e:
        # If an error occurs during upload, delete the user and return False
        users_ref.child(user_id).delete()
        shutil.rmtree(f'dataset/{user_id}/')
        os.unlink(filename_path)
        return False,None

    return True,filename_path



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
            person_index = matches.index(True)
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



