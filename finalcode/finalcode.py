import cv2
import numpy as np

cam=cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)

if(cam.isOpened() != 1 ) :
    cam.open()

while(1) :
    ret ,frame = cam.read()
    blured_frame = cv2.blur(frame,(5,5))

    hsv_blured_frame=cv2.cvtColor(blured_frame, cv2.COLOR_BGR2HSV)

    lower_cig=np.array([12,105,64])
    upper_cig=np.array([25,220,210])

    mask_blured_frame=cv2.inRange(hsv_blured_frame,lower_cig,upper_cig)
    
    dilation = cv2.dilate(mask_blured_frame,kernel,iterations = 3)
#    erosion = cv2.erode(dilation,kernel,iterations = 4)
    morphed = cv2.erode(dilation,kernel,iterations = 4)

    image2,contours, hierarchy = cv2.findContours(morphed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    count=len(contours)
    print(count)
    
    for i in range(count):

	M =cv2.moments(contours[i])
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])

        rect = cv2.minAreaRect(contours[i])
        box=cv2.boxPoints(rect)
        box=np.int0(box)
        cv2.drawContours(frame,[box],0,(0,0,255),2)

# integrate area condition
        q,(w,e),r=cv2.minAreaRect(contours[i])

    cv2.imshow('original',frame)
    cv2.imshow('mask',morphed)

    k=cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

cv2.destroyAllWindows()
cam.release()

