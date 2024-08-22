import torch
import numpy as np

# 1. 根据已有的数据创建张量 / Creating tensors based on existing data
def test01():
    # 1.1 创建标量 / Creating Scalar
    data = torch.tensor(10)
    print(data)

    # 1.2 使用numpy数组来创建张量(Float64) / Creating tensors using numpy arrays
    data = np.random.randn(2, 3)
    data = torch.tensor(data)
    print(data)

    # 1.3 使用list创建张量(Float32) / Creating tensors using List
    data = [[10,20,30],[40,50,60]]
    data = torch.tensor(data)
    print(data)
# 2. 创建指定形状的张量 / Creating a tenser with a specified shape
def test02():
    # 2.1 创建二行三列的张量(Float32) / creating a tensor with two rows and three columns
    data = torch.Tensor(2, 3)
    print(data)
    # 2.2 创建指定数值的张量 / creating an tensor with specified values
    # 传递列表 / List
    data = torch.Tensor([2,3])
    print(data)

    data = torch.Tensor([10])
    print(data)





if __name__ == '__main__':
    test01()
    test02()