from __future__ import print_function
import torch

x = torch.Tensor(5,3)
print(x)

x = torch.rand(5,3)
print(x)

print(x.size())

print(x+x)
print(torch.add(x,x))

x = x+x
x.add_(x)
print(x)