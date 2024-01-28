"""
the usage of the item() function: output the value of a scalar-tensor, which is a tensor with 1 dimension and 1 value
"""

import torch


x = torch.rand(1)
y = x.item()
print(x)
print(x.shape)
print(type(x))
print(y)
print(type(y))
