import torch
from torch.nn import L1Loss, MSELoss, CrossEntropyLoss

inputs = torch.tensor([1, 2, 3], dtype=torch.float32)
targets = torch.tensor([1, 2, 5], dtype=torch.float32)

inputs = torch.reshape(inputs, (1, 1, 1, 3))
targets = torch.reshape(targets, (1, 1, 1, 3))

loss_L1 = L1Loss()  # reduction默认是mean,可以设置为none或者sum
result_L1 = loss_L1(inputs, targets)

print("L1loss:{:.2f}".format(result_L1))
print(f"L1loss:{result_L1:.2f}")
print("L1loss:%.2f" % result_L1)  # (0+0+2)/3

loss_MSE = MSELoss()
result_MSE = loss_MSE(inputs, targets)
print("MSEloss:{:.2f}".format(result_MSE))  # (0+0+4)/3

x = torch.tensor([[0.1, 0.2, 0.3],
                  [0.4, 0.5, 0.6]])
y = torch.tensor([0,1])
loss_CrossEntropy = CrossEntropyLoss(reduction='none')
loss_cross = loss_CrossEntropy(x, y)

print("CrossEntropyLoss:{}".format(loss_cross))
