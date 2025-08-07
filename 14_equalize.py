import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

# 히스토그램 평활화
# 이미지의 전체 밝기 분포를 고르게 퍼뜨려 명암 대비를 향상시키는 기법
dst1 = cv2.equalizeHist(img1)  # 뭉쳐있는거 평탄화. 그레이스케일(1채널)에서만 가능

img2 = cv2.imread('./images/field.bmp')
# YCrCb 색공간
# Y : 밝기(명도), Cr : 빨강 계열 색상 정보, Cb : 파란 계열 색상 정보
# 밝기를 조절해서 진하게 한다
dst2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
ycrcb = cv2.split(dst2)
ycrcb = list(ycrcb)
# print(ycrcb)  # 3개로 나뉘어져 있다 y cr cb
ycrcb[0] = cv2.equalizeHist(ycrcb[0])  # 평탄화
dst2 = cv2.merge(ycrcb)  # 다시 합쳐주기
dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR)


hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([dst1], [0], None, [256], [0, 255])

hists = {'hist1': hist1, 'hist2': hist2}

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

# plt.figure(figsize=(12, 8))
# for i, (k, v) in enumerate(hists.items()):
#     plt.subplot(1, 2, i+1)
#     plt.title(k)
#     plt.plot(v)
# plt.show()

cv2.waitKey()

# split(), merge()를 사용하지 않고, 슬라이싱과 인덱싱을 이용하여 위 예제와 동일하게 결과 영상을 만들어보자