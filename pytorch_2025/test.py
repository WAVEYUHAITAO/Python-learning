from PIL import Image
from torchvision import transforms
import torch
import torch.nn as nn
from torch.nn import MaxPool2d

image_path = "./images/dog1.jpg"
image = Image.open(image_path)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model1 = nn.Sequential(
            nn.Conv2d(3, 32, 5, stride=1, padding=2),
            MaxPool2d(2),
            nn.Conv2d(32, 32, 5, stride=1, padding=2),
            MaxPool2d(2),
            nn.Conv2d(32, 64, 5, stride=1, padding=2),
            MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10),
        )

    def forward(self, x):
        x = self.model1(x)
        return x

model = torch.load('./models/CIFAR10/net_10.pth',weights_only=False)
# print(model)
transform = transforms.Compose([transforms.Resize((32, 32)),
                                transforms.ToTensor()])

image = transform(image)
print(image.shape)
image = torch.reshape(image, (1,3,32,32)).to(device)
print(image.shape)
model.eval()
with torch.no_grad():
    output = model(image)
    print(output.shape)
    print(output)
print(output.argmax(1))#第五个类别是狗，猜对了
