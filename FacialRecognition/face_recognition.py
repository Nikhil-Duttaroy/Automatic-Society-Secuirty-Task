
def reco():
    print("Func")
    import cv2,os
    import numpy as np
    import sqlite3
    from flask import Flask, render_template,redirect,url_for
    import irregular_dataset
    import app

    
   

    path = os.path.dirname(os.path.abspath(__file__))
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(path+r'\trainer\trainer.yml')
    cascadePath = "FacialRecognition\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    def getProfile(id):
        conn=sqlite3.connect("./FaceBase.db")
        cmd="Select * from Users WHERE ID="+str(id)
        cursor=conn.execute(cmd) 
        profile=None
        for row in cursor:
            profile=row
        conn.close()
        return profile

    def inserttimetemp(id):
        conn=sqlite3.connect("FaceBase.db")
        cmd="Select * from Users WHERE ID="+str(id)
        cursor=conn.execute(cmd)
        isRecordExist=0
        for row in cursor:
            isRecordExist=1
        if(isRecordExist==1):
            cmd="Update Users SET Time=(datetime('now','localtime')) WHERE ID="+str(id)
        else:
            cmd="INSERT INTO Users(Time) Values(datetime('now','localtime'))"
        conn.execute(cmd)
        conn.commit()

        # us = SMBus(1)
        # sensor = MLX90614(bus, address=0x5A)
        # celsius= sensor.get_object_1()
        # fahrenheit = (celsius * 1.8) + 32

        # print "Ambient Temperature :", sensor.get_ambient()
        # print "Object Temperature :", fahrenheit
        # bus.close()

        # cmd="Select * from Users WHERE ID="+str(id)
        # cursor=conn.execute(cmd)
        # isRecordExist=0
        # for row in cursor:
        #     isRecordExist=1
        # if(isRecordExist==1):
        #     cmd="Update Users SET Temperature=(fahrenheit) WHERE ID="+str(id)
        # else:
        #     cmd="INSERT INTO Users(Temperature) Values(?);"
        # conn.execute(cmd,(fahrenheit))
        # conn.commit()



        conn.close()

    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
            id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            
        
            profile=getProfile(id)
            if(profile!=None):
                if (int(conf) < 67):

                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                    conf = "  {0}%".format(round(100 - conf))
                    # cv2.putText(im, str(conf), (x,y+h), font,1, (0,255,0), 2)
                    cv2.putText(im,str(profile[1]), (x+2,y+h+30),font, 1, (0,255,0), 2)
                    cv2.putText(im,str(profile[4]), (x+2,y+h+60),font, 1, (0,255,0), 2)
                    inserttimetemp(id)
                else:
                    id = "unknown"
                    # conf = "  {0}%".format(round(100 - conf))
                    cv2.putText(im,str(id), (x,y+h),font, 1, (0,0,255), 2) 
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
                    
        cv2.imshow('im',im) 

        stop = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if stop == 27:
            break

    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
# reco()
