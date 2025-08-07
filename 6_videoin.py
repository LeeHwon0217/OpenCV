import cv2
import sys

cap = cv2.VideoCapture('./movies/chicken.mp4')  # 비디오를 읽어오거나 웹캠을 읽어옴

if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit()  # 프로그램 종료

print('동영상 불러오기 성공')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(width)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(height)

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 전체 프레임 수
print(frame_count)

fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임 수. 보통 초당 16이면 자연스럽다 느낀다
print(fps)

while True:
    ret, frame = cap.read()  # 프레임 한 장을 가져옴. ret는 성공 여부, frame은 이미지
    if not ret:  # 더 이상 프레임이 없으면
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:  # (밀리세컨드). 이 안에 안 누르면 넘어감
        break
# 동영상 속도가 아닌 for문 도는 속도로 영상이 넘어간다
# 실제 속도는 int(1000 / fps) 이처럼 밀리세컨드 단위로 변환해야 한다

cap.release()