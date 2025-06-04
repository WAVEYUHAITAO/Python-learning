import torch.nn as nn
import torch
import torchvision
from torch.nn import MaxPool2d
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from torch.utils.data import DataLoader

#
# m=nn.MaxPool2d(3,2)
#
# m=nn.MaxPool2d((3,2),(2,1))
#
# input=torch.randn(20,16,50,32)
# print(m(input).shape)


#
# x= torch.tensor([[1,2,0,3,1],
#                  [0,1,2,3,1],
#                  [1,2,1,0,0],
#                  [5,2,3,1,1],
#                  [2,1,0,1,1]])
# x1 = torch.reshape(x,(-1,1,5,5))
# print(x1.shape)
dataset = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=True, transform=transforms.ToTensor())
dataloader = DataLoader(dataset, batch_size=64, shuffle=True, drop_last=True)


class Hai(nn.Module):
    def __init__(self):
        super(Hai, self).__init__()
        # ceil_mode设置为true,kernal未能完全覆盖的地方也会池化取最大，默认是false，不能覆盖就舍去
        #最大池化可以减少数据量
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=True)

    def forward(self, x):
        return self.maxpool1(x)


writer = SummaryWriter("./logs/MaxPool2d")
step = 0
model = Hai()
for data in dataloader:
    imgs, labels = data
    writer.add_images('input', imgs, step)
    writer.add_images('pooled', model(imgs), step)
    step += 1
writer.close()
