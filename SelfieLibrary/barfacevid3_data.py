import learnsk
import io
import picamera
import cv2
import numpy as np
#import time
import zbar
import picamera.array
import Image
import psycopg2
import sys
#import glob
#from pyflann import *


#from imagescanner import ImageScanner

window_on = True

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image 
    
      
def face_track():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        #time.sleep(2)
        first_image = True
                            
        print("Start Motion Tracking ....")
        #frame_count = 0
        #start_time = time.time()
        while(True):

         with picamera.array.PiRGBArray(camera) as stream:
            camera.capture(stream, format='bgr')
            camera.framerate = 30
            camera.sharpness = 60
            camera.contrast = 50
            camera.brightness = 50
            image = stream.array
            if first_image:
                face_cascade = cv2.CascadeClassifier('/home/pi/New/SelfieLibrary/faces.xml')
                

            #Convert to grayscale
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                scanner = zbar.ImageScanner()
                scanner.parse_config('enable')   
                #thresh = 70
                #im_bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
   
    #width, height = my_stream.size
                raw = gray.tostring()
                cv2.imwrite("bw.jpg",gray)
                stream = zbar.Image(600, 400, 'Y800', raw)

                scanner.scan(stream)

    #Here connectivity of database
                con = None
    

                for symbol in stream:
                    BookID = symbol.data
                    #print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
                    print 'BookID found', '"%s"' % BookID
                    #return Book

        #BookID = 123456
        

                    try:
     
                        con = psycopg2.connect(database="testdb", user="selfilib", password="12345", host="127.0.0.1", port="5432")     
    
                        cur = con.cursor()
  
                        cur.execute("SELECT * FROM BookD where Id = %s" %(BookID) )
                        rows = cur.fetchall()
                        for row in rows:
                            print row
                            #return row
            #con.commit()
    

                    except psycopg2.DatabaseError, e:
    
                        if con:
                            con.rollback()
    
                        print 'Error %s' % e    
                        sys.exit(1)
    
    
                    finally:
    
                        if con:
                            con.close()
                    
            #Look for faces in the image using the loaded cascade file
                faces = face_cascade.detectMultiScale(gray, 1.1, 5)
                distances =[]
                if window_on:   
            #Draw a rectangle around every found face
                    for (x,y,w,h) in faces:
                        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
                        #print "Found "+str(len(faces))+" face(s)"
                        #if len(faces)>0 :
                        cv2.imwrite('/home/pi/New/SelfieLibrary/result.jpg',gray)
                        print "Found "+str(len(faces))+" face(s)"
                        img = cv2.imread('/home/pi/New/SelfieLibrary/result.jpg')
                            
                        crop_img = img[y: y + h, x: x + w]
                        crop_img = cv2.resize(crop_img,(100, 100))
                        
                            
                            # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
                        cv2.imwrite("/home/pi/New/SelfieLibrary/cropped/probe/cropped.png", crop_img)
                        distances=learnsk.face_rec()
                        print min(distances)[0]
                        if int(min(distances)[0]) <= 1.77436551952e+58:
                            cv2.putText(image,str(min(distances)[1]), (x-100,y), cv2.FONT_HERSHEY_PLAIN,1,(0,0,250),1,1)  
                            
                if window_on:   
                    cv2.imshow('Movement Status',image)
                    #Save the result image
                    
                        

                # Close Window if q pressed
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        
                            #im = cv2.imread("/home/pi/New/cropped/cropped.jpg")
                            #print type(im)
                            
                        cv2.destroyAllWindows()
                        break
#face_track()
                  


    




    








