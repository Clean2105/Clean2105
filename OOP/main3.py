# Câu 3: Tao một ClicksCounter đối tượng có thể được gọi như một hàm, để đếm số lần nhấp chuột vào một nút.
class ClicksCounter:
    def __init__(self):
        self.clicks = 0
    def __call__(self):
        self.clicks += 1
        return self.clicks

button_clicks = ClicksCounter()

print(button_clicks())
print(button_clicks())
print(button_clicks())