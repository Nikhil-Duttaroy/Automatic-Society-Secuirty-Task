def irrdata():       
    import cv2
    import os
    import sqlite3
    from flask import Flask, render_template, redirect
    import app

    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    face_detector = cv2.CascadeClassifier('FacialRecognition\haarcascade_frontalface_default.xml')

    def getid():
        conn=sqlite3.connect("FaceBase.db")
        cmd="Select * from Irregular WHERE ID=(SELECT max(ID)FROM Irregular)"
        cursor=conn.execute(cmd)
        cursor.execute(cmd)
        rows=cursor.fetchall()
        for row in rows:
            print(row[0])
            global id
            id=row[0]
        conn.commit()
        conn.close()
        print(id)
        return id

    getid()

    # Initialize individual sampling face count
    count = 0

    while(True):

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("FacialRecognition\irregular\irregular." + str(id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 10: # Take 30 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release() 
    cv2.destroyAllWindows()

# irrdata()


