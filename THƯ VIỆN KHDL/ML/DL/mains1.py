import openpyxl 
import pandas as pd 

def tinh_doanhthu(file_input, file_output):
    try:
        df = pd.read_excel(file_input, engine="openpyxl")
        required_columns = ['Tên sản phẩm', 'Số lượng', 'Giá']
        for col in required_columns:
            if col not in df.columns:
                print(f"Lỗi! Không tìm thấy cột '{col}' trong excel")
                return
        df['Tổng'] = df['Số Lượng'] * df['Giá']
        df.to_excel(file_output, index=False, engine="openpyxl")

        print(f"Đã tính tổng doanh thu lưu vào: {file_output}")
    except FileNotFoundError:
        print(f"Không tìm thấy file excel: {file_output}")
    except Exception as e:
        print(f"Lỗi xảy ra {e}!") 

if __name__ == '__main__':
    file_input = "Doanhthu.xlsx"
    file_output = "DoanhThu.xlsx" 

    tinh_doanhthu(file_input, file_output)               