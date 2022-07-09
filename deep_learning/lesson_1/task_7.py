from torch import nn

def create_linear():
    return nn.Linear(in_features=10, out_features=100, bias=False)