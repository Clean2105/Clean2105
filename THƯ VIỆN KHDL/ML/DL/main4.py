# Pytorch code
import torch

# Tạo một danh sách hai chiều.
list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Tạo một mảng hai chiều.
tensor_2D_pt = torch.tensor(list_2D)

# Kiểm tra hình dạng, kiểu dữ liệu, loại, thiết bị lưu trữ của mảng.
print(f"Hình dạng của tensor: {tensor_2D_pt.shape}")
print(f"Kiểu dữ liệu của tensor: {tensor_2D_pt.dtype}")
print(f"Loại của tensor: {type(tensor_2D_pt)}")
print(f"Thiết bị lưu trữ của tensor: {tensor_2D_pt.device}")
print(f"Tensor:\n {tensor_2D_pt}") 