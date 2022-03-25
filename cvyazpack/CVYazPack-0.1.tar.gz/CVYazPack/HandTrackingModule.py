import cv2
import mediapipe as mp
import time
import math


class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

        self.RightThumb = False
        self.LeftThumb = False

    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, draw=True):

        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:

            # Iterate over the found hands.
            for hand_no, hand_landmarks in enumerate(self.results.multi_hand_landmarks):
                handNum = int(hand_no) + 1
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    xList.append(cx)
                    yList.append(cy)
                    #print(id, cx, cy)
                    self.lmList.append([handNum, id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 3, (128, 0, 63), cv2.FILLED)
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                bbox = xmin, ymin, xmax, ymax
            if draw:
                cv2.rectangle(img, (bbox[0]-25, bbox[1]-25), (bbox[2]+25, bbox[3]+25), (0, 255, 0), 2)

        return self.lmList, bbox


    def fingersUp(self):
        fingers = []
        # Thumb
        if self.lmList:
            if self.lmList[self.tipIds[0]][2] > self.lmList[self.tipIds[4] - 1][2]:
                self.RightThumb = True
                self.LeftThumb = False
            else:
                self.RightThumb = False
                self.LeftThumb = True

            if self.RightThumb:
                if self.lmList[self.tipIds[0]][2] > self.lmList[self.tipIds[0] - 1][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            elif self.LeftThumb:
                if self.lmList[self.tipIds[0]][2] > self.lmList[self.tipIds[0] - 1][2]:
                    fingers.append(0)
                else:
                    fingers.append(1)

        # 4 Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][3] < self.lmList[self.tipIds[id] - 2][3]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers



    def findDistance(self, p1, p2, img, draw=True):
        x1, y1 = self.lmList[p1][2], self.lmList[p1][3]
        x2, y2 = self.lmList[p2][2], self.lmList[p2][3]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.circle(img, (cx, cy), 10, (255, 150, 4), cv2.FILLED)
            cv2.circle(img, (x1, y1), 10, (255, 150, 4), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 150, 4), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (129, 232, 254), 2)

        length = math.hypot(x2 - x1, y2 - y1)
        return length, img, [x1, y1, x2, y2, cx, cy]

def main():
    pTime = 0
    cTime = 0

    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        # if len(lmList) != 0:
        #     print(lmList)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 140), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
