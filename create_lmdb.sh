#!/usr/bin/env sh
MY=/Users/jiangyu/caffe/examples/myfile

echo "Create train lmdb.."
rm -rf $MY/img_train_lmdb
/Users/jiangyu/caffe/build/tools/convert_imageset \
--shuffle \
--resize_height=256 \
--resize_width=256 \
/Users/jiangyu/caffe/data/re/train/ \
$MY/train.txt \
$MY/img_train_lmdb

echo "Create test lmdb.."
rm -rf $MY/img_test_lmdb
/Users/jiangyu/caffe/build/tools/convert_imageset \
--shuffle \
--resize_width=256 \
--resize_height=256 \
/Users/jiangyu/caffe/data/re/test/ \
$MY/test.txt \
$MY/img_test_lmdb

echo "All Done.."