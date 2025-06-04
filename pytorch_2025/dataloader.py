import torchvision
#准备测试数据集
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10("dataset", train = False, transform= torchvision.transforms.ToTensor(), download = True)
#这里的Dataloader num_worker在window下最好为0因为有可能报错，drop_last=True可以把不能形成一个batch的数据打包
test_loader = DataLoader(test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=True)
print(test_loader)
#测试数据集中的第一张图片及target
img, target = test_data[0]
print(img.shape)
print(target)
writer = SummaryWriter('./logs/dataloader')

for epoch in range(2):
    step = 0
    print("开始运行Epoch {}".format(epoch))
    for data in test_loader:
        imgs,targets = data
        # print(img.shape)
        # print(target)
        writer.add_images('Epoch:{}'.format(epoch),imgs,step)
        step += 1
writer.close()
print("完成写入")