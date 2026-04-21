import torch
import numpy as np

def dm01():
  # 场景1: 标量 张量
  t1 = torch.tensor(10)
  print(f't1:{t1},type:{type(t1)}')
  print('-' * 30)

  #场景2: 二维列表 ->张量
  data = [[1,2,3],[4,5,6]]
  t2 = torch.tensor(data)
  print(f't2:{t2},type:{type(t2)}')
  print('-' * 30)

  #场景3: numpy nd数组——>张量
  data = np.random.randint(0,10,size=(2,3))
  t3 = torch.tensor(data)
  print(f't3:{t3},type:{type(t3)}')
  print('-' * 30)

if __name__ == '__main__':
  dm01()
