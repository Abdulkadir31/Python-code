import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale

img = cv2.imread(r'grayscale.jpg',0)
imS = cv2.resize(img, (960, 540))                    # Resize image
#cv2.imshow("output", imS)                            # Show image


#Applying Gaussian Threshold
#th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,71,11)
#cv2.imshow("Window",th4)


#applying Thresh_Otsu

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imshow("Window2",th3)


row=th3.shape[0]
col=th3.shape[1]

count = 0
pixelval=list()
for i in range(row+1):
    pixelval.append(0)

for i in range(1,row):
    count = 0
    for j in range(1,col):
       if(th3[i,j]==0):
           count=count+1
    pixelval[i]=count

# To hold Coordinates of the image
img_cor=list()

#Initialize the Variables
k=1
th=0
i=1
frame='frame'
while i < row:
    if pixelval[i] > th:
        start=i
        end=i
        img_cor.append(start)
        while pixelval[end] > th and end < row:
            end = end + 1
        i = end + 1
        img_cor.append(i)


    else :
        i = i + 1

# Display the images of lines
# i=0
# while i < len(img_cor):
#     line = th3[img_cor[i]:img_cor[i+1],0:col]
#     cv2.imshow(frame,line)
#     i=i+2
#     frame=frame+str(i)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Word Seperation

line = th3[img_cor[0]:img_cor[1],0:col]
cv2.imshow("frame",line)
cv2.waitKey(0)
cv2.destroyAllWindows()

word_row=line.shape[0]
word_col=line.shape[1]


i=0
count = 0
word_pixelval=list()
for i in range(word_col+1):
    word_pixelval.append(0)

# Logic

for i in range(1,word_col):
    count = 0
    for j in range(1,word_row):
       if line[j,i]==0:
           count=count+1
    word_pixelval[i]=count

i=0
th=0
word_cor = list()
while i < word_col:
    if word_pixelval[i]>th:
        start=i
        end=i
        word_cor.append(start)
        while word_pixelval[end] > th and end < word_col:
            end=end+1
        i=end+1
        word_cor.append(i)
    else:
        i=i+1
print(word_cor)
i=0
while i < len(word_cor):
    line1 = line[0:word_row,word_cor[i]:word_cor[i+1]]
    cv2.imshow(frame,line1)
    i=i+2
    frame=frame+str(i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
