# -*- coding: utf-8 -*-

"""# Deep Learning approach"""

import random
import tensorflow as tf
import numpy as np

import tensorflow.keras.layers as tfkl
import tensorflow.keras as tfk 
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Input
from tensorflow.keras import Model
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Conv2DTranspose
from tensorflow.keras.layers import concatenate

from tensorflow.keras.preprocessing.image import ImageDataGenerator



"""MultiModal-U-Net"""

class MultiModalNet():
    def __init__(self, input_shape):

        # layer to be used in the tfk.Model
        self.input = tfkl.Input(input_shape)

        # layer to be used in the network creation
        self.encoder1 = None
        self.encoder2 = None
        self.decoder = None
        
        # list where I save all conv layers that will be concatenated through
        # the skip connection. This will contain the 2 list of the pool layers
        # of the 2 encoders
        self.pool_layers_list = [[], []]
        self.conv_added = []

    def Down_Conv_block(self, inp, filters, encoder):
        conv1 = tfkl.Conv2D(filters=filters, kernel_size=3, strides=1, padding='same', activation='ReLU')(inp)
        conv2 = tfkl.Conv2D(filters=filters, kernel_size=3, strides=1, padding='same', activation='ReLU')(conv1)
        pool = tfkl.MaxPool2D(pool_size=(2, 2), strides=2)(conv2)
        self.pool_layers_list[encoder].append(conv2)
        return pool

    def Up_Conv_block(self, inp, filters, respective_down_layer):      
        conv1 = tfkl.Conv2D(filters=filters, kernel_size=3, strides=1, padding='same', activation='ReLU')(inp)
        conv2 = tfkl.Conv2D(filters=filters, kernel_size=3, strides=1, padding='same', activation='ReLU')(conv1)
        up_conv = tfkl.Conv2DTranspose(filters=filters//2, kernel_size=2, strides=2, padding='same')(conv2)
        concat = tfkl.Concatenate()([respective_down_layer, up_conv])
        
        return concat

    # given 2 lists of layers add all layers of element-wise
    def Add_Conv_layers(self, list_layer_1, list_layer_2):
        added_layers = []
        assert len(list_layer_1) == len(list_layer_2)
        for i in range(len(list_layer_1)):
            sum_layer = tfkl.Add()([list_layer_1[i], list_layer_2[i]])
            added_layers.append(sum_layer)
        return added_layers


    def build_model(self, filters_list):

        # Encoder Microglia
        for i, filters in enumerate(filters_list[:-1]):

            # if it's the first layer the input should be self.input
            if i == 0:
                self.encoder1 = self.Down_Conv_block(self.input[ :, :, :, 0:1], filters, encoder=0)
            else:
                self.encoder1 = self.Down_Conv_block(self.encoder1, filters, encoder=0)
        
        # Encoder Nuclei
        for i, filters in enumerate(filters_list[:-1]):

            # if it's the first layer the input should be self.input
            if i == 0:
                self.encoder2 = self.Down_Conv_block(self.input[ :, :, :, 1:2], filters, encoder=1)
            else:
                self.encoder2 = self.Down_Conv_block(self.encoder2, filters, encoder=1)
        
        # summing Microglia and Nuclei feature maps at each layer
        self.conv_added = self.Add_Conv_layers(self.pool_layers_list[0], self.pool_layers_list[1])

        # reverse the list of layers to give to the encoder in the right order
        rev_list = self.conv_added[::-1]

        # set the starting layer of the decoder
        self.decoder = tfkl.Add()([self.encoder1, self.encoder2])

        # Decoder
        for i, filters in enumerate(filters_list[:-len(filters_list):-1]):
            self.decoder = self.Up_Conv_block(self.decoder, filters, rev_list[i])
        
        # first convolutions of filters_list
        layer = tfkl.Conv2D(filters=filters_list[0], kernel_size=3, strides=1, padding='same', activation='ReLU')(self.decoder)
        layer = tfkl.Conv2D(filters=filters_list[0], kernel_size=3, strides=1, padding='same', activation='ReLU')(layer)

        # custom convolutions
        layer = tfkl.Conv2D(filters=4, kernel_size=3, strides=1, padding='same', activation='ReLU')(layer)
        layer = tfkl.Conv2D(filters=2, kernel_size=3, strides=1, padding='same', activation='ReLU')(layer)
        out = tfkl.Conv2D(filters=1, kernel_size=3, strides=1, padding='same', activation='sigmoid')(layer)

        model = tfk.Model(inputs=[self.input], outputs=out)

        return model
