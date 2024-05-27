from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
import os

def sepia(input_img):
    if input_img.shape[2] == 4:
        rgb_img = input_img[:, :, :3]
        alpha_channel = input_img[:, :, 3]
    else:
        rgb_img = input_img
        alpha_channel = None

    sepia_filter = np.array([
    [0.131, 0.534, 0.272],
    [0.168, 0.686, 0.349],
    [0.189, 0.769, 0.393]
    ])
    sepia_img = rgb_img.dot(sepia_filter.T)
    sepia_img = np.clip(sepia_img, 0, 255)

    if alpha_channel is not None:
        sepia_img = np.dstack((sepia_img, alpha_channel))

    return sepia_img
