import cv2
import face_recognition
import pickle
import os
from initialize_firebase import *

# upload images in Storage
def upload_images():
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

    return imgList,studentIds

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


def get_encoded_images():
    print("Loading Encode File ...")
    file = open('EncodeFile.p', 'rb')
    encodeListKnownWithIds = pickle.load(file)
    file.close()
    encodeListKnown, studentIds = encodeListKnownWithIds
    return encodeListKnown, studentIds

def encodeImages(imgList, studentIds, encodeListKnown=[],studentIdsKnown=[]):
    print("Encoding Started ...")
    new_encodeListKnown = findEncodings(imgList)

    # Append new encodings to existing list
    updated_encodeListKnown = encodeListKnown + new_encodeListKnown
    updated_studentIdsKnown= studentIdsKnown + studentIds
    updated_encodeListKnownWithIds = [updated_encodeListKnown, updated_studentIdsKnown]

    file = open("EncodeFile.p", 'wb')
    pickle.dump(updated_encodeListKnownWithIds, file)
    fileName = "EncodeFile.p"
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    file.close()
    print("Encoding Complete")
    return updated_encodeListKnownWithIds

def update_encode_file(imgList, studentIds, encodeListKnown=[],studentIdsKnown=[]):
    return encodeImages(imgList, studentIds,encodeListKnown,studentIdsKnown)

# imgList, studentIds=get_upload_images_ids()
# update_encode_file(imgList, studentIds)