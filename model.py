import os
import torch
from torch import nn
import numpy as np
import cv2

from torchvision.models import resnet50, ResNet50_Weights


def get_pain_value(image_path):

    model = resnet50(weights=ResNet50_Weights.DEFAULT)
    model.fc = nn.Sequential(
            nn.Dropout(0.8),
            nn.Linear(in_features=2048, out_features=3)
            )
    model.layer4[0].downsample = nn.Sequential(
            nn.Dropout(0.8),
            nn.Conv2d(1024, 2048, kernel_size=(1, 1), stride=(2, 2), bias=False),
            nn.BatchNorm2d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )

    image = cv2.imread(image_path)
    cropped_frame = cv2.resize(image, (352, 240), interpolation=cv2.INTER_LINEAR)

    model.load_state_dict(torch.load('models/res_fdr_e10-lr-5-wd-3.pth', map_location ='cpu'))

    ten = torch.tensor(cropped_frame.astype(np.float32).swapaxes(-1, 0)).unsqueeze(0)
    ten.shape
    outputs = model(ten)
    preds = torch.argmax(outputs, dim=-1)

    return preds[0].item()

