import torch
import torchvision
import torch.nn as nn
from torchvision import transforms

dataset = torchvision.datasets.CIFAR10(root="./dataset", train=True, download=True, transform=transforms.ToTensor())

dataloader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True,drop_last=True)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(196608,10)
    def forward(self, x):
        x=self.linear1(x)
        return x

model = Net()
for data in dataloader:
    imgs, targets = data
    print(imgs.shape)
    # output = torch.reshape(imgs,(1,1,1,-1))
    output = torch.flatten(imgs)
    print(output.shape)
    output = model(output)
    print(output.shape)