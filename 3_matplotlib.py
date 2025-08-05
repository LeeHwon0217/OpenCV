import cv2
import matplotlib.pyplot as plt

# subplot이용하여 left plot에는 그레이스케일 영상, right plot에는 컬러영상을 출력
img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('./images/dog.bmp', cv2.IMREAD_COLOR)
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

plt.subplot(121)  # plt.subplot(1, 2, 1) -> 1행 2열의 첫 번째 subplot
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.subplot(122)  # plt.subplot(1, 2, 2) -> 1행 2열의 두 번째 subplot
plt.axis('off')
plt.imshow(img_color)
plt.show()