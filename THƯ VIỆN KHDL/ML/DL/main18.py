import torch 

tensor_2d = torch.tensor([[1,2,3], [4,5,6]])

sliced_tensor_1 = tensor_2d[0:1, 1:2]
print(f"Giữ số nguyên:\n {sliced_tensor_1}")

sliced_tensor_2 = tensor_2d[0, 1:2]
print(f"Giảm số chiều:\n {sliced_tensor_2}")

sliced_tensor_3 = tensor_2d[0, 1]
print(f"Giảm số chiều:\n {sliced_tensor_3}")

sliced_tensor_4 = tensor_2d[:, :]
print(f"Giữ số chiều:\n {sliced_tensor_4}") 