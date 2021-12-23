import cv2
import numpy as np


# Funciones de asignación para imagenes
def asiggne_image(path):
    return cv2.imread(path)


# Funciones definidas para el uso del compilador
def rotation(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return rotated_image


def cut(image, p1, p2):
    cut_image = image[p1[1]:p2[1], p1[0]:p2[0]]
    return cut_image


def resize(image, rows, columns):
    down_points = (rows, columns)
    resized_image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
    return resized_image


def blur(image, value_kernel1, value_kernel2):
    ksize = (value_kernel1, value_kernel2)
    blurred_image = cv2.blur(image, ksize)
    return blurred_image


def grayImg(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def print_var(variable):
    if type(variable) is np.numarray:
        cv2.imshow('Image', variable)
    else:
        print(variable)


def size(image):
    return image.shape[0] * image.shape[1]
