import cv2
import numpy as np

cap=cv2.VideoCapture(0)

if(cap.isOpened() != 1 ) :
	cap.open()

while(1) :
	ret ,frame = cap.read()
	blured_frame = cv2.blur(frame,(5,5))
# original
	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)		

	lower_cig=np.array([12,105,64])
	upper_cig=np.array([25,220,210])

	mask = cv2.inRange(hsv,lower_cig,upper_cig)

	result = cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('original',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('final',result)

# blured mask
	blured_mask=cv2.blur(mask,(5,5))
	blured_mask_result = cv2.bitwise_and(frame,frame,mask=blured_mask)

	cv2.imshow('blured_frame',blured_frame)
	cv2.imshow('blured_mask',blured_mask)
	cv2.imshow('blured_mask_final',blured_mask_result)

# mask of blured image 

	hsv_blured_frame=cv2.cvtColor(blured_frame, cv2.COLOR_BGR2HSV)

	mask_blured_frame=cv2.inRange(hsv_blured_frame,lower_cig,upper_cig)

	mask_blured_frame_result = cv2.bitwise_and(frame,frame,mask=mask_blured_frame)

	cv2.imshow('mask_blured_frame',mask_blured_frame)
	cv2.imshow('mask_blured_frame_result',mask_blured_frame_result)

# blured mask of blured image

	blured_mask_blured_frame=cv2.blur(mask_blured_frame,(5,5))
	blured_mask_blured_frame_result=cv2.bitwise_and(frame,frame,mask=blured_mask_blured_frame)

	cv2.imshow('blured_mask_blured_frame',blured_mask_blured_frame)
	cv2.imshow('blured_mask_blured_frame_result',blured_mask_blured_frame_result)

	k=cv2.waitKey(5) & 0xFF
	if k == 27 :
		break

cv2.destroyAllWindows()
