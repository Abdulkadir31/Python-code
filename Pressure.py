import cv2
img = cv2.imread(r'grayscale.jpg',0)
imS = cv2.resize(img, (960, 540))

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


#Applying Gaussian Threshold
th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,71,11)



row=th3.shape[0]
col=th3.shape[1]


print("====== By Otsu Threshhold ======")
# Find pixel intensity

intesity_count=0.0
pixel_count=0
for i in range(row):
     for j in range(col):
        if th3[i,j]==0:
            pixel_count +=1
            intesity_count += img[i,j]

print(pixel_count,intesity_count)
print(intesity_count/pixel_count)



row=th4.shape[0]
col=th4.shape[1]

print("====== By Adaptive Threshhold ======")
# Find pixel intensity

intesity_count=0.0
pixel_count=0
for i in range(row):
     for j in range(col):
        if th3[i,j]==0:
            pixel_count +=1
            intesity_count += img[i,j]

print(pixel_count,intesity_count)
print(intesity_count/pixel_count)
