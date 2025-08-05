import cv2

# 그레이스케일 영상
img1 = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
print(img1)

# bgr형태의 이미지
img2 = cv2.imread('./images/dog.bmp')
print(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey()  # 아무 키를 누를 때까지 대기
