import cv2
cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture(1)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
    
while ret:
    ret,frame=cap.read()
    img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('Original Webcam Feed',frame)
    cv2.imshow('Converted image',img1)
    if cv2.waitKey(1)==27:
       cap.release()
       cv2.destroyAllWindow()
       break
       cv2.imshow('Captured Image',img1)
