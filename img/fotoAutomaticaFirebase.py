#import the necessary modules
import freenect
import cv2
import numpy as np
import time
import datetime
import pyrebase


def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

def tempo():
    return int(input('Digite o tamanho do intervalo em minutos para tira foto = '))


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

if __name__ == "__main__":

    tamIntervalo = tempo() 
    time_count = 0  

    while 1:
        start_time = time.time()
    
        frame = get_video()
        cv2.imshow('RGB image',frame)
        k = cv2.waitKey(1) & 0xFF

        if k == 32:  
            break
        
        end_time = time.time() 
                     
        time_count += end_time - start_time

        if time_count > tamIntervalo*60 : #tempo em segundos           
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y_%H-%M-%S')
            #storage = firebase.storage()
            cv2.imwrite('imgAuto/'+str(st)+'.png',frame)
            #storage.child('imagens/'+str(st)+'.png').put(frame)
            time_count = 0
        
    cv2.destroyAllWindows()
