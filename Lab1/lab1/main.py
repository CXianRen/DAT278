#!python3

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/src/python/')

import numpy as np
import pandas as pd

import time

import layers as layers
from utils import load_weights, load_input_batch, load_labels

DATASET_PATH = './data/'
IMGS_DIR     = 'imagenet_val2012'
LABELS_FILE  = 'ILSVRC2012_validation_ground_truth.json'

WEIGHT_FILE  = 'weights.pth'

BATCH_SIZE = 1

def infer(img, weights):

    t = np.reshape(img, (img.shape[0], -1))

    # L0
    t = layers.Conv2d(t, weights[0]['w'], weights[0]['b'], 11, 4, 2)
    t = layers.ReLU(t)
    t = layers.MaxPool2d(t, 3, 2)


    # L1
    t = layers.Conv2d(t, weights[1]['w'], weights[1]['b'], 5, 1, 2)
    t = layers.ReLU(t)
    t = layers.MaxPool2d(t, 3, 2)

    # L2
    t = layers.Conv2d(t, weights[2]['w'], weights[2]['b'], 3, 1, 1)
    t = layers.ReLU(t)

    # L3
    t = layers.Conv2d(t, weights[3]['w'], weights[3]['b'], 3, 1, 1)
    t = layers.ReLU(t)

    # L4
    t = layers.Conv2d(t, weights[4]['w'], weights[4]['b'], 3, 1, 1)
    t = layers.ReLU(t)
    t = layers.MaxPool2d(t, 3, 2)

    # Transition
    t = layers.AdaptiveAvgPool2d(t, 6, 6)
    t = np.reshape(t, (-1,1))

    # L5
    t = layers.Linear(t, weights[5]['w'], np.copy(weights[5]['b']).reshape(-1,1))
    t = layers.ReLU(t)

    # L6
    t = layers.Linear(t, weights[6]['w'], np.copy(weights[6]['b']).reshape(-1,1))
    t = layers.ReLU(t)

    # L7
    t = layers.Linear(t, weights[7]['w'], np.copy(weights[7]['b']).reshape(-1,1))

    return t.reshape(-1)

if __name__ == '__main__':

    weights = load_weights(WEIGHT_FILE)
    img_list, imgs = load_input_batch(DATASET_PATH + IMGS_DIR, BATCH_SIZE)
    labels = load_labels(DATASET_PATH + LABELS_FILE, img_list)

    df = pd.DataFrame(columns=['image', 'label', 'top1', 'top2', 'top3', 'top4', 'top5'])

    top1_acc = 0
    top5_acc = 0
    
    print("##### Starting Inference #####")

    start = time.time()

    print("image size:", len(imgs))
    for i in range(len(imgs)):
        print("Inferring image ", img_list[i])
        pred = infer(imgs[i], weights)
        top5 = np.argsort(pred)[-5:]
        top5 = [x.item() for x in top5]
        if labels[i] == top5[4]:
            top1_acc += 1
        if labels[i] in top5:
            top5_acc += 1
        df.loc[len(df)] = [img_list[i], labels[i],
                           top5[4], top5[3], top5[2], top5[1], top5[0]]
        
    end = time.time()
        
    print('Top 1 accuracy = ', 100 * top1_acc / BATCH_SIZE, '%')
    print('Top 5 accuracy = ', 100 * top5_acc / BATCH_SIZE, '%')

    print('Start Time = ', int(start * 1000))
    print('  End Time = ', int(  end * 1000))

    df.to_csv('results.csv', index=False)
