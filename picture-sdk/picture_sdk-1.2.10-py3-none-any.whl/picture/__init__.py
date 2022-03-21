import math
import operator
import os
import cv2
import imutils
import time
from functools import reduce
from skimage import measure
from PIL import Image


# 图片大小是否一致
def compare_images(path_one, path_two, pwd=None):
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    h1 = image_one.histogram()
    h2 = image_two.histogram()
    try:
        # diff = ImageChops.difference(image_one, image_two)

        diff = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))  # 完全相同时结果为0.0，差别越大值越大
        if diff == 0.0:
            # 图片间没有任何不同则直接退出
            return "success"
        else:
            compare_pic02(path_one, path_two, pwd)

    except ValueError as e:
        return "{0}\n{1}".format(e, "图片大小和box对应的宽度不一致!")


def compare_pic02(path1, path2, pwd):

    imageA = cv2.imread(path1)
    imageB = cv2.imread(path2)

    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = measure.compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    t = time.time()

    if pwd is None:
        pwd = os.path.dirname(os.path.realpath(__file__))

    suffix = "." + path1.split(".")[1]
    cv2.imencode(suffix, imageB)[1].tofile(pwd + "//" + str(int(t)) + suffix)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


