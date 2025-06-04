import torch
import torch.nn as nn

# 定义一个简单的网络
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        #在训练开始时，running mean 和 running var 会被初始化为 0 和 1。
        self.bn1 = nn.BatchNorm1d(20)  # BatchNorm1d，输入特征数为 20
        self.fc2 = nn.Linear(20, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.bn1(x)  # 应用 BatchNorm
        x = torch.relu(x)
        x = self.fc2(x)
        return x

# 实例化模型
model = SimpleNet()

# 训练模式
model.train()
print("Training mode:")
input_data = torch.randn(5, 10)  # 输入数据 (batch_size=5, 特征数=10)
output = model(input_data)
print("Output:", output)

# 打印 running mean 和 running var
print("Running mean:", model.bn1.running_mean)
print("Running var:", model.bn1.running_var)

# 推理模式
model.eval()
print("\nEvaluation mode:")
input_data = torch.randn(5, 10)  # 输入数据 (batch_size=5, 特征数=10)
output = model(input_data)
print("Output:", output)

# 再次打印 running mean 和 running var
print("Running mean:", model.bn1.running_mean)
print("Running var:", model.bn1.running_var)