
from keras.applications.vgg16 import VGG16
from keras.backend import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.models import load_model
import os
import numpy as np
import cv2
from HelpersToPartB import *


def partA():
    #my directory of images
    dir = "myPics/generic/"

    # load the model
    model = VGG16()

    directory = os.listdir(dir)
    for image in directory:
        imageName = image
        # print(image)
        # load an image from file
        image = load_img(dir + image, target_size=(224, 224))
        # image.show()
        # convert the image pixels to a numpy array
        image = img_to_array(image)

        # reshape data for the model
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

        # prepare the image for the VGG model
        image = preprocess_input(image)

        # predict the probability across all output classes
        yhat = model.predict(image)

        # convert the probabilities to class labels
        label = decode_predictions(yhat)
        # retrieve the most likely result, e.g. highest probability
        label = label[0][0]
        # print the classification
        print("classified " + str(imageName) + " as ", end="")
        print('%s (%.2f%%)' % (label[1], label[2]*100))



def partB():
# define the labels
    labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
              "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
              "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
              "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
              "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
              "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana",
              "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
              "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
              "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
              "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

    # my directory of images
    dir = "myPics/generic/"

    # define the model
    model = load_model("yolo.h5")

    directory = os.listdir(dir)
    for image in directory:

        imageName = image
        # img = cv2.imread(dir + image)
        # cv2.imshow("Image", img)
        # cv2.waitKey(0)

        # define the expected input shape for the model
        input_w, input_h = 224, 224
        # define our new photo
        photo_filename = dir + image
        # load and prepare image
        image, image_w, image_h = load_image_pixels(photo_filename, (input_w, input_h))

        # make prediction
        yhat = model.predict(image)
        # summarize the shape of the list of arrays
        # print([a.shape for a in yhat])

        # define the anchors
        anchors = [[116, 90, 156, 198, 373, 326], [30, 61, 62, 45, 59, 119], [10, 13, 16, 30, 33, 23]]
        # define the probability threshold for detected objects
        class_threshold = 0.6
        boxes = list()
        for i in range(len(yhat)):
            # decode the output of the network
            boxes += decode_netout(yhat[i][0], anchors[i], class_threshold, input_h, input_w)

        # get the details of the detected objects
        v_boxes, v_labels, v_scores = get_boxes(boxes, labels, class_threshold)

        print("classified " + imageName + " as " , end="")
        print(v_labels)


def main():
    # partA()
    partB()


if __name__ == "__main__":
    main()


