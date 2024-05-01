import cv2
import face_recognition
import pickle
import os
from initialize_firebase import *


# Importing student images
def get_upload_images_ids():
    folderPath = 'dataset'
    users = os.listdir(folderPath)
    print(users)
    imgList = []
    studentIds = []
    for user in users:
        studentIds.append(user)
        for image in os.listdir(os.path.join(folderPath, user)):
            fileName = f'{folderPath}/{user}/{image}'
            imgList.append(cv2.imread(fileName))
            bucket = storage.bucket()
            blob = bucket.blob(fileName)
            blob.upload_from_filename(fileName)

    return imgList,studentIds

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def encodeImages(imgList,studentIds):
    print("Encoding Started ...")
    encodeListKnown = findEncodings(imgList)
    encodeListKnownWithIds = [encodeListKnown, studentIds]
    print("Encoding Complete")

    file = open("EncodeFile.p", 'wb')
    pickle.dump(encodeListKnownWithIds, file)
    fileName = "EncodeFile.p"
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    file.close()
    print("File Saved")

def get_encoded_images():
    print("Loading Encode File ...")
    file = open('EncodeFile.p', 'rb')
    encodeListKnownWithIds = pickle.load(file)
    file.close()
    encodeListKnown, studentIds = encodeListKnownWithIds
    return encodeListKnown, studentIds


imgList,studentIds=get_upload_images_ids()
# print(imgList,studentIds)
encodeImages(imgList,studentIds)

    