#!/usr/bin/env python
# coding: utf-8



import numpy as np
import os



################################################################################
#########  Test VIS Gerado pelo codigo Pre processing e do treino
data_folder = '/home/dados2T/DataChallenge2'

images_visNormPP = np.load(os.path.join(data_folder,'images_hjy_normalized.npy'))# 0.0 1.0 0.30354713748997264


#images_visNormPP = images_visNormPP[:,:,:,0]
print(images_visNormPP.shape)
# images_visNormT = np.load('images_efn_vis.npy') # só banda 0,  0.0 1.0 0.30354713748997264

#images_visNormT = np.load('images_efn_visChannel0.npy')
images_visNormT = np.load(os.path.join(data_folder,'images_hjy_new.npy'))
print(images_visNormT.shape)
# print(images_visNormPP.shape)
# print(images_visNormPP.min(), images_visNormPP.max(), images_visNormPP.mean())
# print(images_visNormT.shape)
# print(images_visNormT.min(), images_visNormT.max(), images_visNormT.mean())
print(np.sum(images_visNormPP-images_visNormT))
