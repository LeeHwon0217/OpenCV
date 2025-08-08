import cv2

# ROI(Region of Interest) : 관심 영역

img = cv2.imread('./images/sun.jpg')

x = 182
y = 22
w = 119
h = 108

roi = img[y:y+h, x:x+w]
roi_copy = roi.copy()
img[y:y+h, x+w:x+w+w] = roi
cv2.rectangle(img, (x, y, 2*w, h), (255, 0, 0), 3)
cv2.rectangle(img, (x, y), (x+w+w, y+h), (255, 0, 0), 3)



cv2.imshow('img', img)
cv2.waitKey()