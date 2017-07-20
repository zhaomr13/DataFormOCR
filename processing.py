import cv2
import numpy as np

img = cv2.imread("photo.jpg")
# cv2.imshow('img', img)
# cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img_gray', img_gray)
# cv2.waitKey(0)
img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
# cv2.imshow('img_gray', img_gray)
# cv2.waitKey(0)
ret, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('img_thresh', img_thresh)
# cv2.waitKey(0)
im2, ctrs, hier = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rects = [cv2.boundingRect(ctr) for ctr in ctrs]

cv2.imshow('img_thresh', img_thresh)
cv2.waitKey(0)

for rect in rects:
	cv2.rectangle(img, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 255), 3)

cv2.imshow('processed img', img)
cv2.waitKey(0)