from dotenv import load_dotenv
load_dotenv("../.env")

import cv2
import time
from emailing import send_email
import glob
import os

IMAGES_PATH = "images"
KERNEL_SIZE_GAUSSIAN_BLUR = (21, 21)
TH_FRAME_DIFFERENCE = 50
NEW_VALUE_FRAME_DIFFERENCE = 255
TH_CONTOUR_AREA_PX = 5000
COLOR_BOUNDING_RECTANGLE = (0, 255, 0)
WIDTH_BOUNDING_RECTANGLE_PX = 3


def clean_images_folder():
    """ Function for deleting the saved frames after one of them is used as attachment in an email """
    images = glob.glob(IMAGES_PATH + "/*.png")
    for image in images:
        os.remove(image)


video = cv2.VideoCapture(0)
time.sleep(1)

frame_first = None
latest_boundary_existent = []
count_image = 1

while True:
    boundary_existent = False

    # Read the frame
    check, frame_bgr = video.read()

    """
    Preprocessing:
    1. From BGR to Grayscale
    2. Apply Gaussian Blur
    3. If it is the first frame, store it
    4. Absolute difference between current frame and first frame
    5. Apply threshold
    6. Apply dilation
    7. Find contours
    8. Find bounding rectangles for the contours with area bigger than a threshold
    9. Apply the bounding rectangle to the original frame
    """
    frame_gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    frame_gray_gau = cv2.GaussianBlur(frame_gray, KERNEL_SIZE_GAUSSIAN_BLUR, 0)

    if frame_first is None:
        frame_first = frame_gray_gau

    frame_delta = cv2.absdiff(frame_first, frame_gray_gau)
    frame_thresh = cv2.threshold(frame_delta, TH_FRAME_DIFFERENCE, NEW_VALUE_FRAME_DIFFERENCE, cv2.THRESH_BINARY)[1]
    frame_dil = cv2.dilate(frame_thresh, kernel=None, iterations=2)
    contours, check = cv2.findContours(frame_dil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < TH_CONTOUR_AREA_PX:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        boundary = cv2.rectangle(frame_bgr, (x, y), (x+w, y+h), COLOR_BOUNDING_RECTANGLE, WIDTH_BOUNDING_RECTANGLE_PX)
        if boundary.any():
            boundary_existent = True

            cv2.imwrite(f"{IMAGES_PATH}/{count_image}.png", frame_bgr)
            count_image = count_image + 1

            all_images = glob.glob("images/*.png")
            index_image_to_send = int(len(all_images) / 2)
            image_to_send = all_images[index_image_to_send]

    # Update the list keeping the latest 2 statuses showing whether an object / a person exists or not
    latest_boundary_existent.append(boundary_existent)
    latest_boundary_existent = latest_boundary_existent[-2:]

    # If the object / person just exited, send the email
    if latest_boundary_existent[0] == True and latest_boundary_existent[1] == False:
        send_email(image_to_send)
        clean_images_folder()

    # Display the frame
    cv2.imshow("My video", frame_bgr)

    # Stop displaying the frames when the "Q" key is pressed
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()