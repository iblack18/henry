#Import modules
import picamera
import picamera.array
import time
import cv2

#Initialize camera
camera = picamera.PiCamera()
camera.resolution = (640,480)
rawCapture = picamera.array.PiRGBArray(camera)
#Let camera warm up
time.sleep(0.1)

#Capture image
camera.capture(rawCapture, format="bgr")
img = rawCapture.array

#Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Blur image to reduce noise
blurred = cv2.GaussianBlur(gray, (9, 9), 0)

ret,th1 = cv2.threshold(blurred,35,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#using threshold remave noise
ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)# invert the pixels of the image frame

# invert the pixels of the image frame
# ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)

 contours, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find the contours
   #     cv2.drawContours(frame,contours,-1,(0,255,0),3)
   #     cv2.imshow('frame',frame) #show video
        for cnt in contours:
           if cnt is not None:
           area = cv2.contourArea(cnt)# find the area of contour
           if area>=500 :
            # find moment and centroid
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

#SET DIRECTION BASED ON CENTROID(X) ONLY
 if cx<=150:
                l=(cx*100/160)
                PWMR.start (0)
                PWML.start (0)
                PWMR1.ChangeDutyCycle (100)
                PWML1.ChangeDutyCycle (abs(l-25))
                time.sleep(.08)

            elif cx>=170:
                r=((320-cx)*100/160)
                PWMR.start (0)
                PWML.start (0)
                PWMR1.ChangeDutyCycle (abs(r-25))
                PWML1.ChangeDutyCycle (100)
                time.sleep(.08)

            elif cx>151 and cx<169:
                PWMR.start (0)
                PWML.start (0)
                PWMR1.ChangeDutyCycle (96)
                PWML1.ChangeDutyCycle (100)
                time.sleep(.3)

            else:
                PWMR1.start (0)
                PWML1.start (0)
                PWMR.ChangeDutyCycle (100)
                PWML.ChangeDutyCycle (100)
                time.sleep(.08)

           else:
               PWMR1.start (0)
               PWML1.start (0)
               PWMR.ChangeDutyCycle (100)
               PWML.ChangeDutyCycle (100)
               time.sleep(.08)

        else:
            PWMR1.start (0)
            PWML1.start (0)
            PWMR.ChangeDutyCycle (100)
            PWML.ChangeDutyCycle (100)
            time.sleep(.1)

PWMR.start (0)
PWMR1.start (0)
PWML.start (0)
PWML1.start (0
