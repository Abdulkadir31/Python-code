import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
#cv2.namedWindow("output", cv2.WINDOW_NORMAL)
img = cv2.imread(r'C:\Users\Admin\Desktop\Project\handwriting pics\Images1\Set2\pic (1).jpg',0)
#imS = cv2.resize(img, (960, 540))                    # Resize image
#cv2.imshow("output", imS)                            # Show image
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#applying adaptive gausian thresholding

img1=img
cv2.namedWindow("output1", cv2.WINDOW_NORMAL)
th3 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,71,11)
print (th3.shape)
row=th3.shape[0]
col=th3.shape[1]
print (row)
im=cv2.resize(img,(row//5,col//5),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Result",im)
#px= th3[500,700]
#print (px)
#for i in range(col):
#    start=0
#    while(th3[100,i]==0):
#        i=i+1
#    end=i
#     im=img1.resize(img,()
#     cv2.imshow("output",im)


im = cv2.resize(th3, (960, 540))                    # Resize image
cv2.imshow("output1", im)                            # Show image
cv2.waitKey(0)
cv2.destroyAllWindows()

#
"""
cv2.namedWindow("output1", cv2.WINDOW_NORMAL)
ret,thre1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print (type(thre1))
im = cv2.resize(thre1, (960, 540))                    # Resize image
cv2.imshow("output1", im)                            # Show image
cv2.waitKey(0)
cv2.destroyAllWindows()

"""