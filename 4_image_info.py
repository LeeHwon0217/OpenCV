import cv2
import numpy as np

img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
print('img_gray type: ', type(img_gray))
print('img_gray shape: ', img_gray.shape) # 세로, 가로
print('img_gray dtype: ', img_gray.dtype)

img_color = cv2.imread('./images/dog.bmp')
print('img_color type: ', type(img_color))
print('img_color shape: ', img_color.shape) # 세로, 가로, 색상
print('img_color dtype: ', img_color.dtype)

h, w = img_color.shape[:2]
print(f'이미지 사이즈: {w} * {h}')

# 그레이스케일 영상인지 컬러 영상인지 확인하기
if len(img_color.shape) == 3:
    print('컬러 영상')
elif len(img_color.shape) == 2:
    print('그레이스케일 영상')

img1 = np.zeros((240, 320, 3), dtype=np.uint8)
img2 = np.empty((240, 320), dtype=np.uint8)  # 랜덤값
img3 = np.ones((240, 320), dtype=np.uint8) * 120  # 1로 채운다
img4 = np.full((240, 320, 3), (255, 102, 255), dtype=np.uint8)

# img_color에 특정 색 정보로 영상을 출력
# BGR: (255, 102, 255)
'''
for x in range(h):
    for y in range(w):
        img_color[x, y] = (255, 102, 255)
'''

img1[:, :] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

while True:
    keyvalue = cv2.waitKey()
    if keyvalue == ord('i') or keyvalue == ord('I'):
        img_color = ~img_color  # 컬러 영상 반전
        cv2.imshow('img_color', img_color)
    elif keyvalue == 27:
        break