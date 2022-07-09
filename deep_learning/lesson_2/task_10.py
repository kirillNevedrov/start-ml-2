import torch
from torch import nn
from torch.utils.data import DataLoader

def evaluate(model: nn.Module, data_loader: DataLoader, loss_fn):
    losses = []

    with torch.no_grad():
        model.eval()
    
        for x, y in data_loader:
            output = model(x)
            loss = loss_fn(output, y)
            losses.append(loss.item())

    return sum(losses)/len(losses)
