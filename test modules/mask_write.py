import cv2
import numpy as np

cam=cv2.VideoCapture(0)

if(cam.isOpened() != 1 ) :
	cam.open()

while(1) :
	ret ,frame = cam.read()
	blured_frame = cv2.blur(frame,(5,5))

	hsv_blured_frame=cv2.cvtColor(blured_frame, cv2.COLOR_BGR2HSV)		

	lower_cig=np.array([12,105,64])
	upper_cig=np.array([25,220,210])

	mask_blured_frame=cv2.inRange(hsv_blured_frame,lower_cig,upper_cig)

	cv2.imshow('mask',mask_blured_frame)
	cv2.imwrite('mask1.jpg',mask_blured_frame)

	k=cv2.waitKey(5) & 0xFF
	if k == 27 :
		break

cv2.destroyAllWindows()
cam.release()
