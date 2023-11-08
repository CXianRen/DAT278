#!python3

import numpy as np
import math

def im2col_get_pixel(im, rows, cols, channels, row, col, channel, pad):

    row -= pad
    col -= pad

    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    return im[channel, col + cols * row]

# From Berkeley Vision's Caffe!
# https://github.com/BVLC/caffe/blob/master/LICENSE
def im2col(data_im, ksize, stride, pad):

    channels = data_im.shape[0]

    # Squared ifmaps
    rows = cols = int(math.sqrt(data_im.shape[1]))

    r_col = (rows + 2 * pad - ksize) // stride + 1
    c_col = (cols + 2 * pad - ksize) // stride + 1

    channels_col = channels * ksize * ksize
    data_col = np.zeros((channels_col, r_col * c_col)).astype(np.float32)

    for ch in range(channels_col):
        c_offset = ch % ksize
        r_offset = (ch // ksize) % ksize
        c_im = ch // ksize // ksize
        for r in range(r_col):
            for c in range(c_col):
                im_row = r_offset + r * stride
                im_col = c_offset + c * stride
                col_index = r * c_col + c
                data_col[ch, col_index] = im2col_get_pixel(data_im, rows, cols, channels,
                                                           im_row, im_col, c_im, pad)

    return data_col