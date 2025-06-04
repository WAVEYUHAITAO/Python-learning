import torchvision
from torch import nn
from torchvision import transforms
# train_data = torchvision.datasets.ImageNet("./dataset",split="train",transform=transforms.ToTensor(),
#                                            download=True)
vgg16_false = torchvision.models.vgg16(pretrained=False)
vgg16_true = torchvision.models.vgg16(pretrained=True)
print('ok')
print(vgg16_true)

train_data = torchvision.datasets.CIFAR10(root='./dataset', train=True, download=True, transform=transforms.ToTensor())
#在现有模型中填加层
vgg16_true.classifier.add_module('add_linear', nn.Linear(1000, 10))
print(vgg16_true)
#直接修改现有模型的层
vgg16_false.classifier[6]=nn.Linear(4096, 10)
print(vgg16_false)