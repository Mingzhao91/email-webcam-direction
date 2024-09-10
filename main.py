import cv2
import time

video = cv2.VideoCapture(0)
# wait for 1 second for camera to load
time.sleep(1)

first_frame = None

while True:
    # If you have a laptop, for example you have an integrated camera
    # then you should place zero to use that main camera.
    check, frame = video.read()

    # Convert frames to greyscale frames to reduce the amount of data
    # in matrices.
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # grey frame, amount of blurriness, standard division
    grey_frame_gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grey_frame_gau

    delta_frame = cv2.absdiff(first_frame, grey_frame_gau)

    # if the value is 30, reassign it to 255
    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]

    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    cv2.imshow("My Video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            # if this is a small object, which means it's a fake object, it just the light difference
            # between the static image and the current frame
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Video", frame)




    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
