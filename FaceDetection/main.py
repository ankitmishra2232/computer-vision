import cv2
import time
import FaceDetectionModule as fdm





cap = cv2.VideoCapture(0)
pTime = 0
detector = fdm.FaceDetector()
while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
    cv2.imshow("img", img)
    cv2.waitKey(1)