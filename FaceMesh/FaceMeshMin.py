import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
pTime = 0

mpdraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
facemesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpdraw.DrawingSpec(thickness=1,circle_radius=1)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = facemesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpdraw.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_CONTOURS,
                                  drawSpec,drawSpec)
            for id,lm in enumerate(faceLms.landmark):
                # print(lm)
                ih, iw, ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                print(id,x,y)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime =cTime
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),
                cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    cv2.imshow("img",img)
    cv2.waitKey(1)