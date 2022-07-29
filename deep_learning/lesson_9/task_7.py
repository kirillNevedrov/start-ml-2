import torch
import torch.nn as nn


class Similarity1(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, encoder_states: torch.Tensor, decoder_state: torch.Tensor):
        sim = torch.matmul(encoder_states, decoder_state)

        return sim

test = Similarity1()

encoder_states = torch.randn(2, 3)
decoder_state = torch.randn(3)

test.forward(encoder_states, decoder_state)