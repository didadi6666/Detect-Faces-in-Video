import cv2.cv as cv
import time

cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)

while True:
    img = cv.QueryFrame(capture)
    # cv.ShowImage("camera", img)

    cv.SaveImage('test_7-24-2015.jpg', img)

    if cv.WaitKey(10) == 27:
        break
cv.DestroyAllWindows()