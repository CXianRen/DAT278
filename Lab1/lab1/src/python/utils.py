#!python3

import os

import torch
from torchvision import transforms

import json
import numpy as np
from PIL import Image

transform = transforms.Compose([
    transforms.Resize(256),                # Resize the image to 256×256 pixels
    transforms.CenterCrop(224),            # Crop the image to 224×224 pixels about the center
    transforms.ToTensor(),                 # Convert the image to PyTorch Tensor data type
    transforms.Normalize(                  # Normalize the image
    mean=[0.485, 0.456, 0.406],            # Mean and std of image as also used when training the network
    std=[0.229, 0.224, 0.225]      
    )])

def get_files_in_dir(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in sorted(files):
            file_list.append(file)
    return file_list

def load_weights(file):

    weights = torch.load(file)

    weight_list = []

    pair = {}

    for k, v in weights.items():
        
        np_vals = v.detach().numpy()

        # Assume corresponding weights and biases are always consecutive
        if 'weight' in k:
            if 'features' in k:
                np_vals = np.reshape(np_vals, (np_vals.shape[0], -1))
            pair['w'] = np_vals
        elif 'bias' in k:
            pair['b'] = np_vals
            weight_list.append(pair)
            pair = pair.copy() # Generate a new reference value

    return weight_list

def load_input_batch(path, batch_size=-1, start=0):
    
    img_list = get_files_in_dir(path)

    infer_len = min(batch_size, len(img_list)) if batch_size > 0 else len(img_list)

    imgs = []

    for i in range(infer_len):
        img = Image.open(path + '/' + img_list[i+start])
        img = img.convert('RGB') # Ensure RGB (three input channels)
        img = transform(img)
        img = img.numpy()
        imgs.append(img)

    return img_list[:infer_len], imgs

def load_labels(file, imgs):

    f = open(file)

    data = json.load(f)

    labels = []

    for img in imgs:
        label = data[img]['LABEL_KERAS-CAFFE']
        labels.append(label)

    return labels
