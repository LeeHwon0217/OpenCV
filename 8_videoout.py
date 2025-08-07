import cv2

cap1 = cv2.VideoCapture('./movies/rain.mp4')
cap2 = cv2.VideoCapture('./movies/landscape.mp4')

# 두 동영상을 연결할 때에는 해상도가 같아야 한다
w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

print(w, h)
print(frame_cnt1, frame_cnt2)
print(fps1, fps2)

fourcc = cv2.VideoWriter.fourcc(*'DIVX')  # 이미지는 다 압축기술. 포맷 방식을 결정. DIVX는 avi
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w, h))  # 있으면 덮어씌우기

for i in range(frame_cnt1):
    ret, frame = cap1.read()
    cv2.imshow('output', frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('output', frame)
    out.write(frame)  # 순차적으로 프레임을 이어붙인다
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release()