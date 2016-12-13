import struct
from PIL import Image
import os

#loc to save images
trn_path = '/Users/Liu/Documents/trn/'
tst_path = '/Users/Liu/Documents/tst/'


count_train = 0
count = {}

for z in xrange(1001,1241):
	pic_path = '/Users/Liu/Desktop/HWDB1.1trn_gnt/' + str(z) + '-c.gnt'
	f = open(pic_path, 'rb')

	total_bytes = os.path.getsize(pic_path)
	decoded_bytes = 0

	while decoded_bytes!= total_bytes:
		#count_train to record the number of pictures to be trained
		count_train = count_train + 1

		#record info of each pic:
		#data_length[4 bytes]: record the number of bytes between the first character data and the next character data
		#tag_code[2 bytes]: GBK encoding of the character
		#image_width[2 bytes]: widthof the character image
		#image_height[2 bytes]: height of the character image
		#pixel: actual data of the image
		data_length = struct.unpack('<I', f.read(4))[0]

		tag_code = struct.unpack('>H', f.read(2))[0]

		image_width = struct.unpack('<H', f.read(2))[0]

		image_height = struct.unpack('<H', f.read(2))[0]

		image = Image.new('RGB',(image_width, image_height))
		image_array = image.load()
		for row in xrange(0,image_height):
			for col in xrange(0, image_width):
				pixel = struct.unpack('<B',f.read(1))[0]
				image_array[col,row] = (pixel, pixel, pixel)
	
		decoded_bytes = decoded_bytes + data_length
		#print count_train

		#save the image
		if (os.path.exists(trn_path + str(tag_code))):
			count[tag_code] = int(count[tag_code]) + 1
			filename = trn_path + str(tag_code) + '/' + str(count[tag_code]) + '.jpg'
			image.save(filename)
		else:
			count[tag_code] = 1
			os.makedirs(trn_path+str(tag_code))
			filename = trn_path + str(tag_code) + '/' + str(1) + '.jpg'
			image.save(filename)
	f.close()
	print str(z) + '-c.gnt' + str(count_train)


count_test = 0
count = {}

for z in xrange(1241,1301):
	pic_path = '/Users/Liu/Desktop/HWDB1/' + str(z) + '-c.gnt'
	f = open(pic_path, 'rb')

	total_bytes = os.path.getsize(pic_path)
	decoded_bytes = 0

	while decoded_bytes!= total_bytes:
		#count_train to record the number of pictures to be trained
		count_test = count_test + 1

		data_length = struct.unpack('<I', f.read(4))[0]
		tag_code = struct.unpack('>H', f.read(2))[0]
		image_width = struct.unpack('<H', f.read(2))[0]
		image_height = struct.unpack('<H', f.read(2))[0]

		image = Image.new('RGB',(image_width, image_height))
		image_array = image.load()
		for row in xrange(0,image_height):
			for col in xrange(0, image_width):
				pixel = struct.unpack('<B',f.read(1))[0]
				image_array[col,row] = (pixel, pixel, pixel)
	
		decoded_bytes = decoded_bytes + data_length

		#save the image
		if (os.path.exists(tst_path + str(tag_code))):
			count[tag_code] = int(count[tag_code]) + 1
			filename = tst_path + str(tag_code) + '/' + str(count[tag_code]) + '.jpg'
			image.save(filename)
		else:
			count[tag_code] = 1
			os.makedirs(tst_path+str(tag_code))
			filename = tst_path + str(tag_code) + '/' + str(1) + '.jpg'
			image.save(filename)
	f.close()
	print str(z) + '-c.gnt' + str(count_test)
