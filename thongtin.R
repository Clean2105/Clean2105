# 1. Khởi tạo dữ liệu thông tin thí sinh vi phạm
set.seed(123)
du_lieu <- data.frame(
  Truong = rep(c("Trường A", "Trường B", "Trường C", "Trường D"), each = 3),
  Mon_Hoc = rep(c("Toán", "Lập trình", "Cơ sở dữ liệu"), 4),
  So_Vu_Gian_Lan = c(12, 8, 15, 5, 9, 11, 20, 14, 6, 7, 10, 4)
)

# 2. Thống kê tổng số vụ gian lận theo từng trường
tong_theo_truong <- aggregate(So_Vu_Gian_Lan ~ Truong, data = du_lieu, sum)

# 3. Tính tỷ lệ phần trăm (%) cho từng trường
phan_tram <- round(100 * tong_theo_truong$So_Vu_Gian_Lan / sum(tong_theo_truong$So_Vu_Gian_Lan), 1)

# 4. Tạo nhãn hiển thị bao gồm: Tên trường + Số vụ + Tỷ lệ %
nhan_bieu_do <- paste0(
  tong_theo_truong$Truong, "\n", 
  tong_theo_truong$So_Vu_Gian_Lan, " vụ (", phan_tram, "%)"
)

# 5. Vẽ biểu đồ tròn (Pie Chart)
pie(
  x = tong_theo_truong$So_Vu_Gian_Lan,
  labels = nhan_bieu_do,
  col = c("#4E79A7", "#F28E2B", "#E15759", "#76B7B2"),
  main = "TỶ LỆ THÔNG TIN THÍ SINH GIAN LẬN THI CỬ THEO TRƯỜNG",
  radius = 0.9
)