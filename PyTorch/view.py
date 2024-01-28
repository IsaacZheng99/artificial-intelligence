"""
different usages of the view() function
the core is that the parameter of the view() function is "*shape", which is a variable-length parameter
"""

import torch
from functools import reduce
from operator import mul


x = torch.rand(4, 4)
print(x)
print(x.shape)

# 1. convert x to a 1-dimension tensor
y1 = x.view(-1)
print(y1)
print(y1.shape)

# 2. convert x to a 1-dimension tensor
y2 = x.view(4 * 4)
print(y2)
print(y2.shape)

# 3. convert x to a 1-dimension tensor
y3 = x.view(reduce(mul, x.shape))
print(y3)
print(y3.shape)

# 4. convert x to a 2-dimension tensor
y4 = x.view(2, 8)
print(y4)
print(y4.shape)

# 5. convert x to a 3-dimension tensor
y5 = x.view(2, 2, 4)
print(y5)
print(y5.shape)

# 6. the usage of the "-1" argument in the view() function
# the core is that the length of the variable-length parameter "*shape" is the dimension of the new tensor, 
# and the "-1" will help calculate the corresponding dimension automatically
y6 = x.view(-1, 16)
print(y6)
print(y6.shape)

y7 = x.view(-1, 2)
print(y7)
print(y7.shape)

y8 = x.view(-1, 2, 4)
print(y8)
print(y8.shape)
