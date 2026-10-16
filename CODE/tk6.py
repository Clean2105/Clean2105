import tkinter as tk 

login_info = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3"
}

def check_login():
    username = entry_username.get()
    password = entry_password.get()

    if username in login_info and password == login_info[username]:
        label_result.config(text="Đăng nhập thành công!", fg="green")
    else:
        label_result.config(text="Tên đăng nhập hoặc mật khẩu không đúng!", fg="red")

window = tk.Tk()
window.title("Đăng nhập")
window.geometry("300x250") 

label_username = tk.Label(window, text="Tên đăng nhập:")
label_username.pack(pady=5)

entry_username = tk.Entry(window) 
entry_username.pack(pady=5)

label_password = tk.Label(window, text="Mật khẩu:")
label_password.pack(pady=5)

entry_password = tk.Entry(window, show="*") 
entry_password.pack(pady=5)

button_login = tk.Button(window, text="Đăng nhập", command=check_login)
button_login.pack(pady=15)

label_result = tk.Label(window, text="") 
label_result.pack(pady=5)

window.mainloop()