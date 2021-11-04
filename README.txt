save onxx file that is recognizable by all major perception librarys

using tensorflow keras VGG16 model

issue with latest version of tensorflow - https://forums.developer.nvidia.com/t/unable-to-import-keras-models-on-tensorflow-2-6-0-jetpack-v46/191904
USING VERSION 2.5.0

help with YOLO - https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/
help to creat YOLO model from yolov3.weights file - https://stackoverflow.com/questions/50078960/how-to-convert-the-darknet-yolo-model-to-keras

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

part c)