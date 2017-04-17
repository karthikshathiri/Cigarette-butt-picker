import cv2
import numpy as np

image = cv2.imread('mask.jpg')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(thresh,kernel,iterations = 3)
morphed= cv2.erode(dilation,kernel,iterations = 4)

image2,contours, hierarchy = cv2.findContours(morphed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))

count=len(contours)

for i in range(count):

	M =cv2.moments(contours[i])
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])

	print ('c of ',i,' is (',cx,',',cy,') ')

	rect = cv2.minAreaRect(contours[i])
	box=cv2.boxPoints(rect)
	box=np.int0(box)
	cv2.drawContours(image,[box],0,(0,0,255),2)

	q,(w,e),r=cv2.minAreaRect(contours[i])
	print(w*e)

while (1) :
	cv2.imshow('original',image)

	k=cv2.waitKey(5) & 0xFF
	if k == 27 :
		break

cv2.destroyAllWindows()
