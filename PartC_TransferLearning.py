from pathlib import Path

import numpy
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.layers import Flatten, Dense
from keras.models import load_model
import os

from keras.preprocessing.image import ImageDataGenerator, array_to_img
from matplotlib import pyplot as plt
from tensorflow import keras

def images_to_array(dataset_dir, image_size):
    dataset_array = []
    dataset_labels = []

    class_counter = 0

    classes_names = os.listdir(dataset_dir)
    # print(dataset_dir)
    for current_class_name in classes_names:
        # print(current_class_name)
        class_dir = os.path.join(dataset_dir, current_class_name)
        images_in_class = os.listdir(class_dir)

        # print("Class index", class_counter, ", ", current_class_name, ":" , len(images_in_class))

        for image_file in images_in_class:
            if image_file.endswith(".jpg"):
                # print(image_file)
                image_file_dir = os.path.join(class_dir, image_file)

                img = keras.preprocessing.image.load_img(image_file_dir, target_size=(image_size, image_size))
                img_array = keras.preprocessing.image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)

                img_array = preprocess_input(img_array)
                # img_array = img_array/255.0

                # img_array.shape
                # # Adding the fouth dimension, for number of images
                # img_array = np.expand_dims(img_array, axis=0)

                dataset_array.append(img_array)
                dataset_labels.append(class_counter)
        class_counter = class_counter + 1
    dataset_array = numpy.array(dataset_array)
    dataset_labels = numpy.array(dataset_labels)
    return dataset_array, dataset_labels


def predict(test_images, test_labels, model,show=False):
    predictStart = 0
    predictEnd = 1000
    print("images read in: ", len(test_images))
    # this will show the images being predicted
    if show:
        for y in test_images[predictStart:predictEnd]:
            img = array_to_img(y)
            img.show()

    print("Predictions: ", end="")

    # index into the test images array to choose which images to predict
    predictions = model.predict(test_images[predictStart:predictEnd])
    arrayPred = []
    for x in predictions:
        biggest = max(x)
        counter = 0
        for highest in x:
            if biggest == highest:
                #print("image predicted: " + str(counter))
                arrayPred.append(counter)
                break
            else:
                counter += 1
    print(numpy.array(arrayPred))

    print("Actual: ", end="")
    print()
    print(test_labels[predictStart:predictEnd])

    classLabels = ["dandelion", "other-weeds"]
    print(classLabels)


def loadInTrainedModel(model, showImages):

    # Load the model from disk later using:
    model.load_weights('cnnTrainedOnNewData.h5')


    directory = "data1/test"

    resizeTo = 224

    # print("saving images to array")
    # test_images, test_labels = images_to_array(directory, resizeTo)
    # numpy.save("test_img.npy", test_images)
    # numpy.save("test_labels.npy", test_labels)
    test_images = numpy.load("test_img.npy")
    test_labels = numpy.load("test_labels.npy")

    predict(test_images, test_labels, model, show=showImages)


def loadBaseModelAndTrain(train, showImages):

    img_rows = 224
    img_col = 224
    base_model = VGG16(weights='imagenet',
                       include_top=False,
                       input_shape=(img_rows, img_col, 3))

    # Freeze base model
    base_model.trainable = False

    # Create inputs with correct shape
    inputs = base_model.input

    x = base_model(inputs, training=False)

    # Add pooling layer or flatten layer
    x = Flatten()(x)

    # Add final dense layer
    # 1 output dandelion
    outputs = Dense(2, activation='softmax')(x)

    # Combine inputs and outputs to create model
    model = keras.Model(inputs, outputs)

    # model.summary()

    model.compile(loss="categorical_crossentropy", metrics=['acc'])

    if train:
        datagen = ImageDataGenerator(rescale=1. / 225)

        imgSize = 224

        directory = 'C:/Users/Cade Rasmussen/Documents/USU_Fall_2021/CS_5510_robot_intelligence/Assignments/Exam_Q9/data1'

        # load and iterate training dataset
        train_it = datagen.flow_from_directory(directory + "/train",
                                               target_size=(imgSize, imgSize),
                                               color_mode='rgb',
                                               class_mode="categorical",
                                               )

        # load and iterate test dataset
        test_it = datagen.flow_from_directory(directory + "/test",
                                              target_size=(imgSize, imgSize),
                                              color_mode='rgb',
                                              class_mode="categorical",
                                              )

        history = model.fit(train_it,
                            validation_data=test_it,
                            steps_per_epoch=train_it.samples / train_it.batch_size,
                            validation_steps=test_it.samples / test_it.batch_size,
                            epochs=6)

        # list all data in history
        print(history.history.keys())
        print(history.history.values())
        print(history.history['acc'])
        print(history.history['val_acc'])
        print(history.history)
        # summarize history for accuracy
        plt.plot(history.history['acc'])
        plt.plot(history.history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        # summarize history for loss
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        print("done fitting")

        model.save_weights('cnnTrainedOnNewData.h5')
        print("DONE")

        loadInTrainedModel(model, showImages)

    else:
        loadInTrainedModel(model, showImages)

def runBaseModel():
    model = VGG16(weights='imagenet')

    directory = Path(
        "C:/Users/Cade Rasmussen/Documents/USU_Fall_2021/CS_5510_robot_intelligence/Assignments/Exam_Q9/data/test")

    test_images, test_labels = images_to_array(directory, 224)

    predictBaseModel(test_images, test_labels, model)


def predictBaseModel(test_images, test_labels, model, show=False):

    # this will show the images being predicted
    if show:
        for y in test_images[:]:
            img = array_to_img(y)
            img.show()

    # print("Predictions - (class name, class description, class percentage): ", end="")

    vggThinks = []
    for x in test_images:
        prediction = model.predict(x)
        preds = decode_predictions(prediction, top=1)
        # print(preds)
        for x in preds:
            for img in x:
                class_name = img[0]
                class_description = img[1]
                score = img[2]
                vggThinks.append(class_description)
                print("Predictions (className ClassDescription, percentSure) -- ", class_name, class_description, score*100)


    classLabels = ["dandelion", "dandelion", "matchstick"]
    print("Predictions: ", vggThinks)
    print("Actual: ", classLabels)

def main():
    train = False
    showImages = False

    # loadBaseModelAndTrain(train, showImages)
    runBaseModel()


if __name__ == "__main__":
    main()


