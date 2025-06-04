import torch
import torch.nn as nn
import torch.nn.functional as F


class Hai(nn.Module):

    def __init__(self):
        super().__init__()
#forward是nn.Module必须要重写的
    def forward(self, input):
        output = input + 1
        return output


hai = Hai()
x = torch.tensor(1.0)
output = hai(x)
print(output)