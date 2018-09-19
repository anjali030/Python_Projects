import cv2
imgpath='D:\\4.jpg'
img=cv2.imread(imgpath,0)
outpath='D:\\image.jpg'
cv2.namedWindow('Gray Scale Image',cv2.WINDOW_AUTOSIZE)
cv2.imshow('Gray Scale Image',img)
#print(type(img))
#print(img)
cv2.imwrite(outpath,img)
k=cv2.waitKey(0)
#print(k)
if k==27:
     cv2.destroyWindow('Gray Scale Image')
#cv2.destroyAllWindows()
