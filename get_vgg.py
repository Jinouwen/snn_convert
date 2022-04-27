import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

vgg = keras.applications.VGG16()
vgg.summary()
vgg.save(os.path.join(os.path.abspath('.'), 'snntoolbox_applications/models/vgg16/model.h5'), save_format = 'h5')