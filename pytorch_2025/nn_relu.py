import torch
import torch.nn as nn
import torchvision
from torch.nn import ReLU
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
# input = torch.tensor([[1,-0.5],
#                       [-1,3]])
#
# output = torch.reshape(input, (-1,1,2,2))
# print(input.shape)
# print(output)

dataset = datasets.CIFAR10(root='./dataset', train=False, download=True, transform=transforms.ToTensor())
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = nn.ReLU(inplace=False)
        self.sigmoid = nn.Sigmoid()
    def forward(self, x):
        x = self.sigmoid(x)
        return x

model = Net()

writer = SummaryWriter("./logs/nn_relu")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, step)
    outputs = model(imgs)
    writer.add_images("output", outputs, step)
    step += 1
writer.close()

