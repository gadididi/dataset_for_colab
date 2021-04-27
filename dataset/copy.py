import cv2
import os

path = "./train/"
dst = "./train_img/"
for filename in os.listdir(path):
    if "json" in filename:
        continue
    else:
        img = cv2.imread(path + filename)
        cv2.imwrite(dst + filename, img)
