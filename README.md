# CNN-C

Overview:




Data Preprocessing

We download our Chinese handwriting character data at CASIA:http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html. 
The version we use is HWDB1.1trn_gnt and HWDB1.1tst_gnt. HWDB1.1 includes 3,755 GB2312-80 level-1 Chinese characters and 171 alphanumeric and symbols. 

We convert gnt file to JPG file in convert_gnt_to_jpg.py. 
The only change you need to do is to change the path of gnt file and target file.
