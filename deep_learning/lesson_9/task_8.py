import torch
import torch.nn as nn


class Similarity2(nn.Module):
    def __init__(self, encoder_dim: int, decoder_dim: int, intermediate_dim: int):
        super().__init__()

        self.fc1 = nn.Linear(encoder_dim, intermediate_dim)
        self.fc2 = nn.Linear(decoder_dim, intermediate_dim)
        self.fc3 = nn.Linear(intermediate_dim, 1)
        self.tanh = nn.Tanh()

    def forward(self, encoder_states: torch.Tensor, decoder_state: torch.Tensor):
        x_1 = self.fc1(encoder_states)
        x_2 = self.fc2(decoder_state)
        x = self.tanh(x_1 + x_2)
        
        return self.fc3(x)

test = Similarity2(3, 3, 2)

encoder_states = torch.randn(2, 3)
decoder_state = torch.randn(3)

test.forward(encoder_states, decoder_state)