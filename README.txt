save onxx file that is recognizable by all major perception librarys

using tensorflow keras VGG16 model

issue with latest version of tensorflow - https://forums.developer.nvidia.com/t/unable-to-import-keras-models-on-tensorflow-2-6-0-jetpack-v46/191904
USING VERSION 2.5.0

help with YOLO - https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/
help to creat YOLO model from yolov3.weights file - https://stackoverflow.com/questions/50078960/how-to-convert-the-darknet-yolo-model-to-keras

help with transfer learning - https://www.learndatasci.com/tutorials/hands-on-transfer-learning-keras/
help using vgg16 decode method - https://docs.w3cub.com/tensorflow~2.3/keras/applications/inception_v3/decode_predictions

# I added the coffee mug as a gut check that my classifier was working properly
part a) after running main.py program executes and prints the following

classified Coffee-Mug.jpg as coffee_mug (69.98%)
classified labelme_dvkvazcsyvkumig.jpg as cab (42.62%)
classified labelme_ksbcdzlsogcuudh.jpg as dogsled (70.03%)
classified labelme_ukezunjodtimqkc.jpg as streetcar (36.44%)
classified sun_afqecbbwvpxqcuew.jpg as fountain (83.64%)
classified sun_aiiubfphimhxnlkk.jpg as garbage_truck (7.93%)
classified sun_ajhljrrlroysumtf.jpg as restaurant (33.89%)
classified sun_akeacyqqafcecdbg.jpg as monastery (35.96%)
classified sun_annhmcysnhhysgnz.jpg as china_cabinet (40.43%)
classified sun_anuocfbudybnkgtg.jpg as dam (93.48%)
classified sun_anzyycgyacnppfws.jpg as four-poster (58.91%)
classified sun_aoemlihrrrwglvor.jpg as picket_fence (35.46%)
classified sun_atdkanradmwnyiyn.jpg as four-poster (39.13%)
classified sun_atipxhxbzczdttnx.jpg as turnstile (78.99%)
classified sun_avqxcffpkatshvcl.jpg as horizontal_bar (32.91%)
classified sun_awlzasuxltfvoqrx.jpg as boathouse (41.43%)
classified sun_axbmrnrlmwuzaodf.jpg as wardrobe (10.99%)
classified sun_ayembmzlbmvbrvqc.jpg as maze (96.82%)
classified sun_bhwcxdrfinabwbpi.jpg as totem_pole (37.59%)
classified sun_biqtmpypgwgktgab.jpg as microwave (19.15%)
classified sun_cpsvebxdrvevzsim.jpg as screen (13.74%)

Process finished with exit code 0

# to run this part you will need to get a yolo.h5 file by converting yolov3.weights via the convert.py script at the following repo
# git clone https://github.com/qqwweee/keras-yolo3.git
# you can download the yolov3.weights online

part b) after running main.py program executes and prints the following

classified Coffee-Mug.jpg as ['cup', 'cup', 'cup']
classified labelme_dvkvazcsyvkumig.jpg as ['person', 'person', 'person', 'car', 'car', 'car', 'car', 'car', 'car', 'car', 'person', 'person', 'person', 'person', 'person']
classified labelme_ksbcdzlsogcuudh.jpg as ['person', 'person', 'person', 'person', 'person', 'person', 'person', 'person', 'person']
classified labelme_ukezunjodtimqkc.jpg as ['person']
classified sun_afqecbbwvpxqcuew.jpg as []
classified sun_aiiubfphimhxnlkk.jpg as []
classified sun_ajhljrrlroysumtf.jpg as ['diningtable', 'oven', 'bowl']
classified sun_akeacyqqafcecdbg.jpg as []
classified sun_annhmcysnhhysgnz.jpg as ['chair', 'chair', 'chair', 'chair', 'chair', 'chair', 'chair', 'chair', 'chair', 'chair', 'chair']
classified sun_anuocfbudybnkgtg.jpg as []
classified sun_anzyycgyacnppfws.jpg as ['bed', 'bed']
classified sun_aoemlihrrrwglvor.jpg as []
classified sun_atdkanradmwnyiyn.jpg as ['bed', 'sofa', 'bed', 'bed', 'chair', 'chair']
classified sun_atipxhxbzczdttnx.jpg as []
classified sun_avqxcffpkatshvcl.jpg as []
classified sun_awlzasuxltfvoqrx.jpg as []
classified sun_axbmrnrlmwuzaodf.jpg as []
classified sun_ayembmzlbmvbrvqc.jpg as []
classified sun_bhwcxdrfinabwbpi.jpg as ['person', 'person', 'person', 'person', 'person', 'person', 'person']
classified sun_biqtmpypgwgktgab.jpg as ['chair', 'chair', 'chair', 'chair', 'chair', 'clock', 'clock', 'clock', 'tvmonitor']
classified sun_cpsvebxdrvevzsim.jpg as ['person', 'person', 'person', 'person', 'person']

this is a pretty cool image detector because it is detecting multiple things in one image and its only "looking once"
as you can see it is a bit limited in what it identifies. Sometimes it doesnt identify anything


# I am using a dandeliond dataset from here - https://www.kaggle.com/coloradokb/dandelionimages
# when running the base model classifier before it has been trained you will need a few images of a dandelion in the correct folder on your comp

part c)
BASE MODEL CLASSIFIES 2 IMAGES OF DANDELIONS AS FOLLOWS:
** images used dandelion.jpg and dandi2.jpg and match.jpg

Predictions (className ClassDescription, percentSure) --  n11879895 rapeseed 65.46717286109924
Predictions (className ClassDescription, percentSure) --  n11939491 daisy 92.84752011299133
Predictions (className ClassDescription, percentSure) --  n03729826 matchstick 93.97574663162231

Predictions:  ['rapeseed', 'daisy', 'matchstick']
Actual:  ['dandelion', 'dandelion', 'matchstick']

AFTER TRANSFER LEARNING:

Found 1262 images belonging to 2 classes.
Found 1262 images belonging to 2 classes.

Epoch 1/6
39/39 [==============================] - 217s 6s/step - loss: 1.9865 - acc: 0.5214 - val_loss: 1.3742 - val_acc: 0.5119
Epoch 2/6
39/39 [==============================] - 226s 6s/step - loss: 1.1680 - acc: 0.5864 - val_loss: 0.7292 - val_acc: 0.6506
Epoch 3/6
39/39 [==============================] - 220s 6s/step - loss: 1.0227 - acc: 0.6616 - val_loss: 1.0879 - val_acc: 0.5650
Epoch 4/6
39/39 [==============================] - 220s 6s/step - loss: 0.8492 - acc: 0.6886 - val_loss: 0.2687 - val_acc: 0.8883
Epoch 5/6
39/39 [==============================] - 222s 6s/step - loss: 0.8643 - acc: 0.7108 - val_loss: 0.5500 - val_acc: 0.7472
Epoch 6/6
39/39 [==============================] - 221s 6s/step - loss: 0.7230 - acc: 0.7369 - val_loss: 0.8882 - val_acc: 0.6957

Not super accurate but 0 is dandelion and 1 is other-weeds
NOTICE: in the predictions there are a lot more dandelion predictions then in the end when they are all weeds
in other words it falsy thought a dandelion was a weed a bunch of times, but it never saw a bunch of weeds and
classified it as a dandelion
    **NOTE: I think I could refine the database, there are a lot of images that appear to only be weeds that is being
            trained as a dandelion and I think that is throwing off the trainer. Also i could have trained it over more
            epochs

Predictions: [0 0 1 1 1 0 0 0 0 1 1 1 1 1 1 1 0 1 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 0 0 0 1
 1 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 1 0 1 0 0 0 1 1 1 0 0 1 0 1 1 1 1 0 1 1 0
 1 1 1 0 0 0 1 1 0 0 1 1 0 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 0 0 1 1 1 0 0 1 0
 0 0 0 1 1 1 1 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 1
 1 0 0 1 1 1 1 1 0 0 0 1 1 1 1 1 0 1 0 0 0 0 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1
 1 1 1 0 1 0 0 1 0 1 0 0 1 1 1 1 1 1 1 0 0 1 0 0 1 0 0 0 0 0 0 0 1 1 1 1 1
 0 1 1 1 1 1 1 1 0 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1
 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 0 1 1 1 1 1 1 1 1 1
 1 1 1 0 1 1 1 0 1 0 1 0 1 0 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 1 1 0 0 1 1 1
 1 0 1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 1 0 1 1 0 0 1 0 1 1 1 1 1 1 1 1 1 0 1
 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
 0 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 0 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1]
Actual:
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1]
['dandelion', 'other-weeds']

SLICE IN CENTER imgs 500-600
Predictions:
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
Actual:
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
['dandelion', 'other-weeds']

SLICE IN CENTER imgs 900-1000
Predictions:
[0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1 0 0 0 1 1 1 0 1 0 0 0 0 0 0 0 0
 0 0 1 0 0 1 1 0 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 1 0 1 0 1
 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 1 0 1 1]
Actual:
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
['dandelion', 'other-weeds']