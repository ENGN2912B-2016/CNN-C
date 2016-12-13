#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/myfile
DATA=data/re
TOOLS=/Users/jiangyu/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/img_train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."

compute_image_mean.exe --backend=leveldb examples\myfile\img_train_leveldb examples\myfile\mean.binaryproto
