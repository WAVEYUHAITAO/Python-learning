import torch
import torch.nn as nn
import torchvision
from torch.utils.data import Dataset, DataLoader
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]])
kernal = torch.tensor([[1, 2, 1],
                       [0, 1, 0],
                       [2, 1, 0]])

input = torch.reshape(input, (1, 1, 5, 5))
kernal = torch.reshape(kernal, (1, 1, 3, 3))

print(input.shape)
print(kernal.shape)

output = F.conv2d(input, kernal, stride=1)
print(output)
print(output.shape)

output1 = F.conv2d(input, kernal, stride=2)
print(output1)
print(output1.shape)

output2 = F.conv2d(input, kernal, stride=1, padding=1)
print(output2)


dataset = torchvision.datasets.CIFAR10(root='./dataset', train=False, transform=transforms.ToTensor())
dataloader = DataLoader(dataset, batch_size=64, shuffle=True, drop_last=True)
class HaiNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 3,stride=1, padding=0)
    def forward(self, x):
        x = self.conv1(x)
        return x
writer = SummaryWriter("./logs/conv")
step = 0
model = HaiNet()
for data in dataloader:
    img, target = data
    output = model(img)
    print(img.shape)
    print(output.shape)
    #torch.Size([64, 3, 32, 32])
    writer.add_images('input', img, step)
    #torch.Size([64, 6, 30, 30]) 6个chanel没法显示
    output1 = output.reshape(-1,3,30,30) #这里把6个channel变成3个因为tensorboard不会显示6通道，所以batchsize不懂多少，可以写-1，程序会自动调整
    writer.add_images('output', output1, step)
    step += 1
writer.close()
