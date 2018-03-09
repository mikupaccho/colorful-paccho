#coding: utf-8
from PIL import Image
image = Image.open('sample_image/gas_den.jpg')
image.show() #本来の色のガスパッチョとデンパッチョを表示
r, g, b = image.split()
convert_image = Image.merge("RGB", (b, g, r)) #
convert_image.save('sample_image/gas_den_switch.jpg');
convert_image.show() #色が入れ替わったガスパッチョとデンパッチョを表示