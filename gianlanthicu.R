# 1. Khởi tạo dữ liệu
set.seed(123)
du_lieu <- data.frame(
  Truong = rep(c("Trường A", "Trường B", "Trường C"), each = 4),
  Mon_Hoc = rep(c("Toán", "Lập trình", "Cơ sở dữ liệu", "Mạng máy tính"), 3),
  So_Vu_Gian_Lan = sample(1:15, 12, replace = TRUE)
)

# 2. Tính tổng số vụ theo trường (Tạo biến tong_theo_truong)
tong_theo_truong <- aggregate(So_Vu_Gian_Lan ~ Truong, data = du_lieu, sum)
colnames(tong_theo_truong) <- c("Trường", "Tổng số vụ gian lận")

# 3. Vẽ biểu đồ
barplot(
  height = tong_theo_truong$`Tổng số vụ gian lận`,
  names.arg = tong_theo_truong$`Trường`,
  col = c("#4E79A7", "#F28E2B", "#E15759"),
  main = "Thống kê số lượng gian lận thi cử theo trường",
  xlab = "Trường học",
  ylab = "Số vụ vi phạm",
  ylim = c(0, max(tong_theo_truong$`Tổng số vụ gian lận`) + 10)
)