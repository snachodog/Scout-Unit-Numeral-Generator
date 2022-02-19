import sys
from PIL import Image
# alternate way of importing image?
# images = [Image.open(x) for x in ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']]
# widths, heights = zip(*(i.size for i in images))
# get the numeral images - add pack numeals later
one = Image.open("one.jpg")
two = Image.open("two.jpg")
three = Image.open("three.jpg")
four = Image.open("four.jpg")
five = Image.open("five.jpg")
six = Image.open("six.jpg")
seven = Image.open("seven.jpg")
eight = Image.open("eight.jpg")
nine = Image.open("nine.jpg")
zero = Image.open("zero.jpg")
# get the unit number - add pack as an option later
# make the variable the same as numbers
unitno = input("What is your Troop number?")
print(f'You entered {unitno}')
# parse the troop number

# make parsed numbers equal to their numeral
# combining images
# https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
# alternate method for combining?
# import numpy as np
# import PIL
# from PIL import Image
#
list_im = ['one.jpg', 'two.jpg', 'three.jpg', 'four.jpg', 'five.jpg', 'six.jpg', 'seven.jpg', 'eight.jpg', 'nine.jpg', 'zero.jpg']
imgs    = [ pillow.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Trifecta.jpg' )

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Trifecta_vertical.jpg' )
