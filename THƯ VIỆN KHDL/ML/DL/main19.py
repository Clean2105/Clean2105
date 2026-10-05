import torch 

tensor_2d = torch.tensor([[1,2,3], [4,5,6], [7,8,9]])

row_1_tensor_1 = tensor_2d[1, :]
print(f"Giảm số chiều: {row_1_tensor_1}") 

row_1_tensor_2 = tensor_2d[1:2, :]
print(f"Giữ số chiều: {row_1_tensor_2}") 

column_2_tensor_1 = tensor_2d[:,2]
print(f"Giảm số chiều:\n {column_2_tensor_1}")

column_2_tensor_2 = tensor_2d[:, 2:3]
print(f"Giữ số chiều:\n {column_2_tensor_2}") 