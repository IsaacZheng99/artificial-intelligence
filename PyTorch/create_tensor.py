"""
different ways to creat a tensor
digression: shape is added to more closely match numpy
"""

import torch


# 1. get an uninitialized Tensor object, more often we use the empty() function
x1 = torch.empty(2, 3)
print(x1)
print(type(x1))

# 2. get an uninitialized Tensor object with the construction function
x2 = torch.Tensor(2, 3)
print(x2)
print(type(x2))

# 3. get an randomly initialized Tensor object with its values are evenly between 0 and 1
x3 = torch.rand(3, 3)
print(x3)
print(type(x3))

# 4. get an randomly initialized Tensor object with its values obey the standard normal distribution
x4 = torch.randn(3, 3)
print(x4)
print(type(x4))

# 5. get an initialized Tensor object with its values are all zero
x5 = torch.zeros(4, 4)
print(x5)
print(x5[0][0].dtype)

# 6. get an initialized Tensor object with its values are all 1
x6 = torch.ones(4, 4, dtype=torch.double)
print(x6)
print(x6[0][0].dtype)

# 7. from an python List object
x7 = torch.tensor([1, 2])
print(x7)
print(x7.shape)
print(x7.dtype)

# 8. from an python List object
x8 = torch.Tensor([1, 2])
print(x8)
print(x8.shape)
print(x8.dtype)

# 9. get a Tensor object with the same dimensions
y = torch.rand(2, 4, dtype=torch.double)
print(y)
print(y.shape)
print(y.dtype)
x9 = torch.rand_like(y)
print(x9)
print(x9.shape)
print(x9.dtype)
print(x9.size())
