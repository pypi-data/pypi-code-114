import io
import matplotlib.pyplot as plt
import numpy as np
import cv2
from importlib import resources


def read_img(images_uri, size=550):
    """
    Reads images from a list of paths and returns a single image with all images stacked on top of each other.
    parameters
    ----------
    :param images_uri: list
        name of to images to be processed
    :param size: int
        image resize dimensions
    :return: np.array
        numpy arrays of vertically stacked images
    """
    images = []
    for image_uri in images_uri:
        with resources.open_binary('architecture', *[image_uri]) as image_file:
            img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (size, img.shape[0]))
            images.append(img)
    return np.vstack(images)


def showImage(images_uri):
    """
    Shows a list of images passed as a list of paths.
    :param images_uri: list
        list of images by name to be displayed
    :return: None
    """
    for i in range(len(images_uri)):
        plt.subplot(1, len(images_uri), i + 1)
        with resources.open_binary('architecture', *[images_uri[i]]) as image_file:
            img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.xticks([])
            plt.yticks([])
            plt.title(images_uri[i].split("/")[-1][:-4])
    plt.show()


def TLU():
    plt.figure(figsize=(10, 10))
    showImage(['TLU.png'])


def Perceptron():
    plt.figure(figsize=(10, 10))
    showImage(['Perceptron.png'])


def MLP():
    plt.figure(figsize=(10, 10))
    showImage(['MLP.png'])


def LeNet5():
    plt.figure(figsize=(10, 10))
    LeNet = read_img(["LeNet5_A.png", "LeNet5_B.png"], size=500)
    plt.imshow(LeNet)
    plt.xticks([])
    plt.yticks([])
    plt.title("LeNet5")
    plt.show()


def AlexNet():
    plt.figure(figsize=(14, 10))
    alexNet = read_img(["AlexNet_A.png", "AlexNet_B.png"], size=600)
    plt.imshow(alexNet)
    plt.xticks([])
    plt.yticks([])
    plt.title("AlexNet")
    plt.show()


def VGG():
    """
    Plots the VGG architecture.
    :return: None
    """
    plt.figure(figsize=(11, 11))
    vgg = read_img(["VGG.png", "VGG_B.png"], size=550)
    plt.imshow(vgg)
    plt.xticks([])
    plt.yticks([])
    plt.title("VGG architecture")
    plt.show()


def InceptionModule():
    plt.figure(figsize=(8, 8))
    img = plt.imread("InceptionModule.png")
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()


def GoogleNet():
    plt.figure(figsize=(10, 10))
    # img = plt.imread(read_img(["GoogleNet.png"]))
    plt.imshow(read_img(['GoogleNet.png']))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def GoogleNetAux():
    plt.figure(figsize=(12, 40))
    img = plt.imread("GoogleNetAux.png")
    plt.imshow(read_img(['GoogleNetAux.png']))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def PlainVsRes():
    plt.figure(figsize=(45, 15))
    img = read_img(["PlainvsResidual.png"])
    img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()


def NOfP():
    plt.figure(figsize=(10, 8))
    plt.imshow(read_img(['NumberOfParameters.png']))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def ResNextVar():
    plt.figure(figsize=(30, 15))
    plt.imshow(read_img(['ResNextVariants.png']))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def ResNextArch():
    plt.figure(figsize=(13, 10))
    plt.imshow(read_img(['ResNextArchitecture.jpg']))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def InvertedResidual():
    plt.figure(figsize=(10, 8))
    plt.imshow(read_img(['InvertedResidual.jpg']))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def LBottleNeck():
    plt.figure(figsize=(8, 8))
    plt.imshow(read_img(['MobilenetBlock.jpg']))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def MBnetArch():
    plt.figure(figsize=(12, 10))
    plt.imshow(read_img(["MobilenetArch.jpg"]))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def Densenetview():
    plt.figure(figsize=(20, 15))
    img = plt.imread('DenseNetOverview2.jpg')
    plt.imshow(read_img(["DenseNetOverview2.jpg"]))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def Densenetarch():
    plt.figure(figsize=(16, 16))
    plt.imshow(read_img(["DenseNetArch"]))
    plt.xticks([])
    plt.yticks([])
    plt.show()


def Densenetarch2():
    plt.figure(figsize=(15, 5))
    img = read_img(['DenseNetArch2.jpg'])
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()
