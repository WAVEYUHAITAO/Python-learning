import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn
from torch.nn import Flatten, MaxPool2d, Conv2d
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root='./dataset', train=True, download=True, transform=transforms.ToTensor())
dataloader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True, drop_last=True)


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

        self.model1 = nn.Sequential(
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
        x = self.model1(x)
        return x


model = Net()
loss = nn.CrossEntropyLoss() #设定损失函数
optim = torch.optim.SGD(model.parameters(), lr=0.01) #设定优化函数
steps = 0
for epoch in range(20):
    running_loss = 0.0
    for data in dataloader:
        imgs, labels = data
        print(len(imgs),len(labels),len(data),len(dataloader))
        outputs = model(imgs)
        result_loss = loss(outputs, labels)
        optim.zero_grad() #每一轮的梯度归零
        result_loss.backward()  # 反向传播，这里用来计算每个kernal对应节点的梯度，没有.backward()不会计算梯度
        optim.step() #优化参数
        running_loss += result_loss / len(labels)
    print(f"Epoch{epoch + 1}:{running_loss}")
