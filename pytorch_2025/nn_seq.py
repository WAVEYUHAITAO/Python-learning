import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn
from torch.nn import Flatten, MaxPool2d, Conv2d
from torch.utils.tensorboard import SummaryWriter


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # self.conv1 = nn.Conv2d(3, 32, 5, stride=1, padding=2)
        # self.maxpool1 = nn.MaxPool2d(2)
        # self.conv2 = nn.Conv2d(32, 32, 5, stride=1, padding='same')
        # self.maxpool2 = nn.MaxPool2d(2)
        # self.conv3 = nn.Conv2d(32, 64, 5, stride=1, padding='same')
        # self.maxpool3 = nn.MaxPool2d(2)
        # self.flatten = Flatten()
        # self.fc1 = nn.Linear(1024, 64)
        # self.fc2 = nn.Linear(64, 10)

        self.model1 =nn.Sequential(
            Conv2d(3, 32, 5, stride=1, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, stride=1, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, stride=1, padding=2),
            MaxPool2d(2),
            Flatten(),
            nn.Linear(1024, 64),
            nn.Linear(64, 10)
        )
    def forward(self, x):
        # x=self.conv1(x)
        # x=self.maxpool1(x)
        # x=self.conv2(x)
        # x=self.maxpool2(x)
        # x=self.conv3(x)
        # x=self.maxpool3(x)
        # x = self.flatten(x)
        # x = self.fc1(x)
        # x = self.fc2(x)
        x= self.model1(x)
        return x

model = Net()
print(model)

input = torch.ones(64,3,32,32)
output = model(input)
print(output.shape)

writer = SummaryWriter("./logs/nn_seq")
writer.add_graph(model, input)
writer.close()
