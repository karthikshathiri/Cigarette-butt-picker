import cv2
import numpy as np

image = cv2.imread('mask.jpg')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(thresh,kernel,iterations = 3)
#dilation1 = cv2.dilate(thresh,None,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 4)



while (1) :
	cv2.imshow('original',image)
	cv2.imshow('morphed',dilation)
#	cv2.imshow('morphed1',dilation1)
	cv2.imshow('final',erosion)

	k=cv2.waitKey(5) & 0xFF
	if k == 27 :
		break

cv2.destroyAllWindows()
