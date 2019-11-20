from __future__ import print_function
import cv2

image_file = 'bg_image.jpg'
bg_image = cv2.imread(image_file)

while True:
    cv2.imshow('bg_image', bg_image)
    key = cv2.waitKey(10) & 0xff
    if key == ord('q'):
        break



