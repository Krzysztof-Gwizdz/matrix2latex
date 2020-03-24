import cv2
import numpy as np
import pytesseract

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_flipped = cv2.flip( frame, -1)
    frame_gray = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1,1), np.uint8)
    dilated = cv2.dilate(frame_gray, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    gaus = cv2.adaptiveThreshold(frame_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 3.5)
    cv2.imshow('capture', gaus)
##    img_text = pytesseract.image_to_string(gaus)
##    print(img_text)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
