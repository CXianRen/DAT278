#!python3

import os

import pickle
import json
import numpy as np

def get_files_in_dir(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in sorted(files):
            file_list.append(file)
    return file_list

def load_weights(file):

    with open(file, 'rb') as handle:
        weights = pickle.load(handle)

    return weights

def load_input_batch(path, batch_size=-1):
    
    img_list = get_files_in_dir(path)

    infer_len = min(batch_size, len(img_list)) if batch_size > 0 else len(img_list)

    imgs = []

    for i in range(infer_len):

        with open(path + '/' + img_list[i] , 'rb') as handle:
            img = pickle.load(handle)

        imgs.append(img)

        img_list[i] = img_list[i].split('.')[0] + '.JPEG'

    return img_list[:infer_len], imgs

def load_labels(file, imgs):

    f = open(file)

    data = json.load(f)

    labels = []

    for img in imgs:
        label = data[img]['LABEL_KERAS-CAFFE']
        labels.append(label)

    return labels
