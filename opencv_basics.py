# import cv2
# print("hello world")
# #
# #
# # # -------for image-------
# # img = cv2.imread("F:\opencvExample\sample.jpg")
# # cv2.imshow("output",img)
# # cv2.waitKey(0)
# #
# #
# # # -------for video-------
# # cap = cv2.VideoCapture("F:\HACKSTER\lorawan dam monitoring\B-L072Z.mp4")
# # while True:
# #     success, img = cap.read()
# #     cv2.imshow("Video",img)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
#
# # -------for web cam------
# cap = cv2.VideoCapture(2)
# # cap.set(3,640)
# # cap.set(4,480)
# # cap.set(10,100)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

import cv2
import mediapipe as mp
import time

# import fuction_pose as fp

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
def main():
    count = 0
    while (count<20):
        count += 1
        print("checking condition")
        success, img = cap.read()
        flipp = cv2.flip(img, flipCode=0)
        flipped = cv2.flip(flipp, flipCode=0)
        frame1 = cv2.resize(flipped, (640, 480))
        imgRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
        lmList = []
        results = pose.process(imgRGB)
        # print(results.pose_landmarks)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                print(lmList[0][2])
                if (lmList[0][2]) > 430:
                    print("fall detected")
                    count = 19


                # if lmList[12][1] > 370 and lmList[11][1] > 370:
                #     print("fall detected")
                #     sleep(0.5)

                # cTime = time.time()
                # fps = 1 / (cTime - pTime)
                # pTime = cTime

                # cv2.putText(results, str(int(fps)), (100,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                cv2.imshow("output", img)
                cv2.waitKey(1)
                # cv2.destroyAllWindows()
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    # cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
