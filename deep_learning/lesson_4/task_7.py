import torch
import torch.nn as nn
from torch.utils.data import DataLoader

@torch.inference_mode()
def predict(model: nn.Module, loader: DataLoader, device: torch.device):
    model.eval()

    predictions = []
    
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        
        output = model(x)

        _, y_pred = torch.max(output, 1)
        
        predictions.append(y_pred)
    
    return torch.cat(predictions)