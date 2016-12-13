# CNN-C

Overview:




Part 1.
Data Preprocessing:

We download our Chinese handwriting character data at CASIA:http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html. 
The version we use is HWDB1.1trn_gnt and HWDB1.1tst_gnt. HWDB1.1 includes 3,755 GB2312-80 level-1 Chinese characters and 171 alphanumeric and symbols. 

We convert gnt file to JPG file in convert_gnt_to_jpg.py. 
The only change you need to do is to change the path of gnt file and target file.

Part 2.
Caffe Based Train And Test:

(1)Run create_filelist.sh to create train.txt and text.txt.
(2)Run create_lmdb.sh to create data sets, which are image_train_lmdb and image_test_lmdb.
(3)Run make_imagenet_mean to calculate the mean of data sets.
(4)Modify network_parameter_settings.prototxt to change the parameters of networks.
(5)Run train_and_test_model.prototxt to train and test data sets.
