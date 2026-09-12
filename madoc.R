# 1. Khởi tạo tập dữ liệu số lượng mã độc máy tính
du_lieu_ma_doc <- data.frame(
  Loai_Ma_Doc = c("Trojan", "Ransomware", "Spyware", "Worm/Virus", "Adware"),
  So_Luong = c(450, 280, 150, 120, 80)
)

# 2. Tính tỷ lệ phần trăm (%)
tong_so <- sum(du_lieu_ma_doc$So_Luong)
phan_tram <- round(100 * du_lieu_ma_doc$So_Luong / tong_so, 1)

# 3. Tạo nhãn hiển thị (Tên mã độc + Số lượng + %)
nhan_bieu_do <- paste0(
  du_lieu_ma_doc$Loai_Ma_Doc, "\n", 
  du_lieu_ma_doc$So_Luong, " mẫu (", phan_tram, "%)"
)

# 4. Bảng thống kê chi tiết ra Console
cat("=== BẢNG THỐNG KÊ SỐ LƯỢNG MÃ ĐỘC MÁY TÍNH ===\n")
du_lieu_ma_doc$Ty_Le_Percent <- phan_tram
print(du_lieu_ma_doc)
cat("\nTổng số mẫu mã độc phát hiện:", tong_so, "\n-----------------------------------\n")

# 5. Vẽ biểu đồ tròn (Pie Chart)
pie(
  x = du_lieu_ma_doc$So_Luong,
  labels = nhan_bieu_do,
  col = c("#E15759", "#F28E2B", "#4E79A7", "#76B7B2", "#59A14F"),
  main = "THỐNG KÊ TỶ LỆ SỐ LƯỢNG MÃ ĐỘC MÁY TÍNH",
  radius = 0.9
)