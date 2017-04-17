import cv2
import numpy as np

image = cv2.imread('mask.jpg')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

image2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

count=len(contours)

for i in range(count):

	rect= cv2.minAreaRect(contours[i])
	box=cv2.boxPoints(rect)
#	q,w,e=cv2.minAreaRect(contours[i])
#	print('q,w,e are ',q,' ',w,' ',e)
	box=np.int0(box)
	cv2.drawContours(image,[box],0,(0,0,255),2)

while (1) :
	cv2.imshow('original',image)
	cv2.imshow('thresh',thresh)
	k=cv2.waitKey(5) & 0xFF
	if k == 27 :
		break

cv2.destroyAllWindows()
