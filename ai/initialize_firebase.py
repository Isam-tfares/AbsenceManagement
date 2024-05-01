import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
from google.cloud.firestore_v1.base_query import FieldFilter, Or

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://absencemanagement-8802e-default-rtdb.firebaseio.com/",
     'storageBucket': "absencemanagement-8802e.appspot.com"
})

ref = db.reference('DB')
presence_ref = ref.child('presences')
users_ref = ref.child('users')
bucket = storage.bucket()