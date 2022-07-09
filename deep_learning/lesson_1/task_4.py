import torch

def function01(tensor: torch.Tensor, count_over: str):
    return torch.mean(tensor, 1 if count_over == "rows" else 0)