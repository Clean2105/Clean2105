import tkinter as tk 

def update_value(val):
    value_label.config(text="Value: {}".format(val))

root = tk.Tk()
root.geometry("300x100")

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_value)
scale.pack(pady=20)

value_label = tk.Label(root, text="Value: {}".format(scale.get()))
value_label.pack()

root.mainloop() 