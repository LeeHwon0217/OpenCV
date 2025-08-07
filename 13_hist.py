import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/candies.png', cv2.IMREAD_GRAYSCALE)

# 히스토그램
# 이미지 히스토그램 : 밝기(또는 색상) 값의 분포를 그래프로 표현
# 어떤 픽셀이 밝기 0(검정)인지 255(흰색)인지, 각 값이 몇 개나 있는지를 확인
# images : 대상 이미지 리스트
# channel : 분석할 채널 번호 (B:0, G:1, R:2)
# mask : 분석할 영역의 마스크 (None : 전체)
# histSize : 히스토그램의 빈 개수
# ranges : 값의 범위
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])



img2 = cv2.imread('./images/candies.png')
print('shape : ', img2.shape)
print('dtype: ', img2.dtype)
'''
b = img2[:, :, 0]
g = img2[:, :, 1]
r = img2[:, :, 2]
'''
b, g, r = cv2.split(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
plt.plot(hist1)  # 픽셀의 개수
plt.show()

cv2.waitKey()