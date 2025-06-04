# 准备数据集
import torch
import torch.nn as nn
import torchvision
from torch.utils.tensorboard import SummaryWriter
import time
from cifar_model import *
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torchvision import transforms

train_data = torchvision.datasets.CIFAR10(root='./dataset', train=True, download=True, transform=transforms.ToTensor())
test_data = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=True, transform=transforms.ToTensor())

# length长度
train_data_size = len(train_data)
test_data_size = len(test_data)
print("训练数据集长度:{},测试数据集长度:{}".format(train_data_size, test_data_size))

# 利用 Dataloader 加载数据集
train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

# 搭建神经网络
net = Net()

# 创建损失函数
loss_fn = nn.CrossEntropyLoss()

# 创建优化器
# 1e-2 = 1x(10)^(-2)=0.01
learning_rate = 1e-2
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

# 设置训练网络的一些参数
# 记录每轮训练的次数
total_train_step = 0
# 记录每轮测试的次数
total_test_step = 1
# 记录训练次数
epoch = 10

# 添加tensorboard
writer = SummaryWriter("./logs/train_logs")

# 计算程序运行时间
start_time = time.time()
print("开始时间戳:", start_time)
for i in range(epoch):
    print("--------第{}轮训练开始--------".format(i + 1))
    # 训练步骤开始
    net.train()#Set the module in train mode. e.g. Dropout, BatchNorm, etc.This is equivalent with self.train(True).
    for data in train_dataloader:
        img, target = data
        output = net(img)
        loss = loss_fn(output, target)
        # 优化器梯度清零
        optimizer.zero_grad()
        # 计算梯度
        loss.backward()
        # 优化梯度根据learning_rate进行一次调优
        optimizer.step()
        total_train_step += 1
        # 这样写冯百才打印训练结果，防止看着太乱
        if total_train_step % 100 == 0:
            # 直接打印loss是tensor数据类型，tensor.item()会转化为一个数字
            print("训练次数:{},loss:{}".format(total_train_step, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train_step)
    # 测试步骤开始
    #在训练开始时，running mean 和 running var 会被初始化为 0 和 1。
    net.eval()#Set the module in evaluation mode. e.g. Dropout, BatchNorm, etc.This is equivalent with self.train(False).
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataloader:
            img, target = data
            output = net(img)
            loss = loss_fn(output, target)
            total_test_loss += loss.item()
            accuracy = (output.argmax(dim=1)==target).sum()
            total_accuracy += accuracy.item()
    print("整体测试集上的loss:{}".format(total_test_loss))
    print(f"整体测试集上的正确率:{total_accuracy/test_data_size}")
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    writer.add_scalar("test_accuracy", total_accuracy/test_data_size, total_test_step)
    #保存每一步的模型
    torch.save(net, "./models/CIFAR10/net_{}.pth".format(total_test_step))
    total_test_step += 1
end_time = time.time()
print("结束时间戳:", end_time)
elapsed_time = end_time - start_time
print(f"程序运行时间:{elapsed_time:.4f}秒")
writer.close()
