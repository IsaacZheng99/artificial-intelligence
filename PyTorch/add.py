"""
different ways to adding two tensors
"""

import torch


a = torch.rand(2, 3)
b = torch.ones(2, 3)

# 1. operation +
c1 = a + b
print(c1)

# 2. torch.add()
c2 = torch.add(a, b)
print(c2)

# 3. torch.add(out= )
c3 = torch.empty(2, 3)
torch.add(a, b, out=c3)
print(c3)

# 4. add() this is an out-of-place operation
c4 = a.add(b)
print(a)
print(c4)

# 5. add_()  here "_" means this is an in-place operation
a.add_(b)
print(a)
