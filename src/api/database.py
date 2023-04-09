import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



def get_db():

    cred = credentials.Certificate('./credentials.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

