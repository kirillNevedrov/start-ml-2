import torch

def function02(tensor: torch.Tensor):
    return torch.rand(tensor.shape[1],  dtype=torch.float32, requires_grad=True)

n_steps = 50
step_size = 1e-2

def function03(x: torch.Tensor, y: torch.Tensor):
    w = function02(x)

    for i in range(n_steps):
        w.requires_grad = True

        Y_pred = x @ w

        mse = torch.mean((Y_pred - y) ** 2)

        print(f'MSE на шаге {i+1} {mse.item():.5f}')

        mse.backward()

        with torch.no_grad():
            w = w - w.grad * step_size
            
    return w