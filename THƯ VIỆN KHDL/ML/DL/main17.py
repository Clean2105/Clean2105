import torch 

torch.manual_seed(2024) 
tensor_rand = torch.rand((3,4))
print(f"Ngẫu nhiên khoảng [1,0):\n {tensor_rand}")

tensor_randint = torch.randint(-10, 10, size=(3,4))
print(f"Ngẫu nhiên trong khoảng [-10,10):\n  {tensor_randint}") 