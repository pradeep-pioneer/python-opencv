import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while True:
    ret, frame = cap.read()
    cv2.imshow('camera',frame)
    if cv2.waitKey(22) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()