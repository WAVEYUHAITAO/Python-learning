import torch
import torchvision
from model_save import *
#方式一：保存方式一，加载模型
model1 = torch.load('./models/vgg16_mothod1.pth',weights_only=False)
print(model1)


#方式2,加载模型

#weights加载的是模型的字典权重
weights = torch.load('./models/vgg16_mothod2.pth',weights_only=False)
vgg16 = torchvision.models.vgg16()
vgg16.load_state_dict(weights)
print(weights)
print(vgg16)

#陷阱1
# class Net(torch.nn.Module):
#     def __init__(self):
#         super(Net, self).__init__()
#         self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
#     def forward(self, x):
#         x = self.conv1(x)
#         return x
#这里是自己定义的模型，需要把模型的类复制过来，只是不用实例化这个类. 或者把那个模型import过来
model =torch.load('./models/Net_method1.pth',weights_only=False)
print(model)