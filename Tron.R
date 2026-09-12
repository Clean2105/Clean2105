# 1. Khởi tạo dữ liệu mô phỏng cho 15 máy tính
set.seed(42)
du_lieu_phan_tan <- data.frame(
  May_Tinh = paste0("PC_", 1:15),
  So_Luong_Ma_Doc = c(2, 5, 8, 12, 15, 18, 22, 25, 30, 35, 40, 42, 48, 50, 55),
  RAM_Chiag_Dung_MB = c(120, 180, 250, 310, 390, 420, 510, 580, 620, 710, 790, 830, 910, 950, 1020)
)

# 2. Vẽ biểu đồ phân tán (Scatter Plot)
plot(
  x = du_lieu_phan_tan$So_Luong_Ma_Doc,
  y = du_lieu_phan_tan$RAM_Chiag_Dung_MB,
  main = "BIỂU ĐỒ PHÂN TÁN: MÃ ĐỘC VS DUNG LƯỢNG RAM CHIẾM DỤNG",
  xlab = "Số lượng mã độc phát hiện (Mẫu)",
  ylab = "Bộ nhớ RAM bị chiếm dụng (MB)",
  pch = 19,          # Kiểu điểm: Hình tròn đặc
  col = "#E15759",    # Màu sắc các điểm
  cex = 1.5          # Kích thước điểm
)

# 3. Thêm đường xu hướng (Trendline / Linear Regression)
duong_xu_huong <- lm(RAM_Chiag_Dung_MB ~ So_Luong_Ma_Doc, data = du_lieu_phan_tan)
abline(duong_xu_huong, col = "#4E79A7", lwd = 2, lty = 2)

# 4. Thêm lưới ô vuông giúp dễ quan sát
grid(nx = NULL, ny = NULL, col = "lightgray", lty = "dotted")