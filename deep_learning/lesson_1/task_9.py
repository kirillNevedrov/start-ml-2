import torch
from torch import nn

def count_parameters(layer: nn.Module):
    return sum(torch.numel(p) for p in layer.parameters() if p.requires_grad)