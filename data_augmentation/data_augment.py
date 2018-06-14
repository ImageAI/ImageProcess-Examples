#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os

def zoom(img_path):
    img_file = img_path.split("\\")[-1]
    img = cv2.imread(img_path)
    res = cv2.resize(img, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_CUBIC)
    cv2.imshow("zoom.jpg", res)
    cv2.imwrite("./output" + "/" + "zoom_" + img_file, res)


def translation(img_path):
    img_file = img_path.split("\\")[-1]
    img = cv2.imread(img_path, 0)
    rows, cols = img.shape[:2]

    M = np.float32([[1,0,100],[0,1,50]])
    res = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow("translation.jpg", res)
    cv2.imwrite("./output" + "/" + "translation_" + img_file, res)


def rotation(img_path):
    img_file = img_path.split("\\")[-1]
    img = cv2.imread(img_path)
    rows, cols = img.shape[:2]

    M = cv2.getRotationMatrix2D((rows/2, cols/2), 90, 1)
    res = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow("rotation.jpg", res)
    cv2.imwrite("./output" + "/" + "rotation_" + img_file, res)


def affine_transformation(img_path):
    img_file = img_path.split("\\")[-1]
    img = cv2.imread(img_path)
    rows, cols, ch = img.shape
    print("width = %d height = %d depth = %d" % (cols, rows, ch))
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    pts3 = np.float32([[5,150],[160,20],[100,250]])

    M = cv2.getAffineTransform(pts1, pts3)
    res = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow("affine_transformation.jpg", res)
    cv2.imwrite("./output" + "/" + "affine_" + img_file, res)


def perspective_transformation(img_path):
    img_file = img_path.split("\\")[-1]
    img = cv2.imread(img_path)
    rows, cols, ch = img.shape
    pts1 = np.float32([[1, 95], [240, 95], [240, 336], [1, 336]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    pts3 = np.float32([[0,0], [240,0], [240,336], [0,336]])
    print(pts1)
    M = cv2.getPerspectiveTransform(pts1, pts3)
    res = cv2.warpPerspective(img, M, (cols, rows))
    cv2.imshow("perspective_transformation.jpg", res)
    cv2.imwrite("./output" + "/" + "perspective_" + img_file, res)

if __name__ == "__main__":
    root_file = "./img"
    if not os.path.exists(root_file):
        print("The file path is not exist")
        exit(1)
    list_img = os.listdir(root_file)
    for i in range(len(list_img)):
        img_name_ext = list_img[i]
        img_name = img_name_ext.split(".")[0]
        print(img_name)
        img_path = root_file + "\\" + img_name_ext
        # img_path = "2007_000187.jpg"
        img = cv2.imread(img_path)
        cv2.imshow("original_img.jpg", img)

        zoom(img_path)
        translation(img_path)
        rotation(img_path)
        affine_transformation(img_path)
        perspective_transformation(img_path)

        cv2.waitKey(0)




