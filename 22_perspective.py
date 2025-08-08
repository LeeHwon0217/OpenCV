import cv2
import numpy as np

img = cv2.imread('./images/pic.jpg')

scale = 0.5
resized = cv2.resize(img, dsize=None, fx=scale, fy=scale)

w, h = 600, 400

srcQuad = np.array(
    [[185, 86], [612, 78], [703, 415], [104, 424]], np.float32
)

dstQuad = np.array(
    [[0, 0], [w, 0], [w, h], [0, h]], np.float32
)

# 투시 변환(perspective Transform)
# 영상에서 원근감을 조절하거나, 사각형을 반듯하게 펴주는 변환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(resized, pers, (w, h))

cv2.imshow('Resized (50%)', resized)
cv2.imshow('dst', dst)

cv2.waitKey(0)