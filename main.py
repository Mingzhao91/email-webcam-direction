import cv2
import time

video = cv2.VideoCapture(0)
# wait for 1 second for camera to load
time.sleep(1)

while True:
    # If you have a laptop, for example you have an integrated camera
    # then you should place zero to use that main camera.
    check, frame = video.read()
    cv2.imshow("My Video", frame)
    # print(check)
    # print(frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
