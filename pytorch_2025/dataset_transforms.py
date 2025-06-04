import torchvision
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
dataset_transform = transforms.Compose([
    transforms.ToTensor(),
])
#这里就是下载到指定文件夹，下面两行写一个就好
train_set = torchvision.datasets.CIFAR10(root='./dataset', train=True, transform=dataset_transform, download=True)
test_set = torchvision.datasets.CIFAR10(root='./dataset', train=False, transform=dataset_transform, download=True)

# print(test_set[0])
# print(test_set.classes)
#
#
# img,target = test_set[0]
# print(img)
# print(target)
# print(test_set.classes[target])

# print(test_set[0])

writer = SummaryWriter('logs/cifar10')#括号里设置log保存的路径没有的话会自动创建文件夹
for i in range(10):
    img, label = train_set[i]
    writer.add_image('CIFAR10', img ,i)
writer.close()