import torch.nn as nn

def create_simple_conv_cifar():
    return nn.Sequential(
                nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),  # 32 x 32 x 16
                nn.BatchNorm2d(16),
                nn.ReLU(),

                nn.MaxPool2d(2),  # 16 x 16 x 16
                nn.Dropout2d(p=0.2),

                nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),  # 16 x 16 x 32
                nn.BatchNorm2d(32),
                nn.ReLU(),

                nn.MaxPool2d(2),  # 8 x 8 x 32
                nn.Dropout2d(p=0.2),

                nn.Flatten(),

                nn.Linear(8 * 8 * 32, 1024),
                nn.BatchNorm1d(1024),
                nn.ReLU(),
                nn.Linear(1024, 128),
                nn.BatchNorm1d(128),
                nn.ReLU(),
                nn.Linear(128, 10)
            )