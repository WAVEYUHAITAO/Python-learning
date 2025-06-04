import torch
import torchvision
from torchvision.models import VGG16_Weights

vgg16 = torchvision.models.vgg16(weights = 'IMAGENET1K_V1')
#保存方式1 模型结构+模型参数
torch.save(vgg16, './models/vgg16_mothod1.pth')


#保存方式2 模型参数 (官方推荐)
torch.save(vgg16.state_dict(), './models/vgg16_mothod2.pth')


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
    def forward(self, x):
        x = self.conv1(x)
        return x

model = Net()
torch.save(model, './models/Net_method1.pth')