import torch
import torch.nn as nn
from torch.nn import MaxPool2d


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model1 = nn.Sequential(
            nn.Conv2d(3, 32, 5, stride=1, padding=2),
            MaxPool2d(2),
            nn.Conv2d(32, 32, 5, stride=1, padding=2),
            MaxPool2d(2),
            nn.Conv2d(32, 64, 5, stride=1, padding=2),
            MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10),
        )

    def forward(self, x):
        x = self.model1(x)
        return x

if __name__ == '__main__':
    net = Net()
    input = torch.ones(64,3,32,32)
    output = net(input)
    print(output.shape)
