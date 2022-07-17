import torch
import torch.nn as nn
from torch.utils.data import DataLoader

@torch.inference_mode()
def predict_tta(model: nn.Module, loader: DataLoader, device: torch.device, iterations: int = 2):
    model.eval()
    
    iteration_outputs = []
    
    for i in range(iterations):
        outputs = []
        
        for x, y in loader:
            x, y = x.to(device), y.to(device)

            output = model(x)

            outputs.append(output)
            
        iteration_outputs.append(torch.cat(outputs, 0))
    
    final_outputs = torch.stack(iteration_outputs, 0).mean(0)
    
    _, y_pred = torch.max(final_outputs, 1)
    
    return y_pred