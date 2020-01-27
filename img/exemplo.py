import pyrebase
config = {
    "apiKey": "AIzaSyA45MQf2Ig_xx0Er8eynM3r2KL6CeQlw2U",
    "authDomain": "teste-ab9eb.firebaseapp.com",
    "databaseURL": "https://teste-ab9eb.firebaseio.com",
    "projectId": "teste-ab9eb",
    "storageBucket": "teste-ab9eb.appspot.com",
    "messagingSenderId": "862533329365",
    "appId": "1:862533329365:web:b58f5c957fe12c4d8edd5c",
    "measurementId": "G-STFVMB377Q"
}
  
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

storage.child('imagens/02.png').put("teste.png")