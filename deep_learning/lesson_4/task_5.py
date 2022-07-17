import torch

def get_normalize(features: torch.Tensor):
    return torch.mean(features, (0, 2, 3)), torch.std(features, (0, 2, 3))