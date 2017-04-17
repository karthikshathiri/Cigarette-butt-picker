import cv2
import numpy as np

cam = cv2.VideoCapture(-1)
while ( True ):
	ret, frame = cam.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	image_mask=cv2.inRange(hsv,np.array([12,105,64]),
	np.array([25,220,210]))
	output=cv2.bitwise_and(frame,frame,mask=image_mask)
	cv2.imshow('Original',frame)
	cv2.imshow('Output',output)
	cv2.imshow('binary',image_mask)
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()
cam.release()
