import torch
from torch import nn

def function02(tensor: torch.Tensor):
    return torch.rand(tensor.shape[1],  dtype=torch.float32, requires_grad=True)

step_size = 1e-2

def function04(x: torch.Tensor, y: torch.Tensor):
    model = nn.Linear(in_features=x.shape[1], out_features=1, bias=False)    
    
    w = function02(x)
    i = 0

    while True:
        w.requires_grad = True

        Y_pred = x @ w

        mse = torch.mean((Y_pred - y) ** 2)

        print(f'MSE на шаге {i+1} {mse.item():.5f}')
        
        if mse.item() < 0.3:
            break
            
        i += 1

        mse.backward()

        with torch.no_grad():
            w = w - w.grad * step_size
            
    model.weight = nn.Parameter(w)
            
    return model