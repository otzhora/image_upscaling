import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from skimage import transform
import os

def load_image( infilename ) :
  img = Image.open( infilename )
  img.load()
  data = np.asarray( img, dtype="int32" )
  return data


def imgshow(img):
  plt.figure(figsize=(18, 9))
  plt.imshow(img)
  plt.show()


def load_images(path, n=-1):
  names = next(os.walk(path))[2]
  filenames = [path + name for name in names[0:n]]
  images = [load_image(filename) for filename in filenames]
  return images
  

def lr_image(img, downscale=4):
  dim = (img.shape[0] // downscale, img.shape[1] // downscale, 3)
  lr_img = transform.rescale(img, 1/downscale, multichannel=True, preserve_range=True).astype(dtype="int32")
  return lr_img 


def lr_images(images, downscale=4):
  return [lr_image(img, downscale) for img in images]