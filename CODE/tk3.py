from tkinter import* 

root = Tk()

canvas = Canvas(root, width=300, height=200) 
canvas.pack()
canvas.create_rectangle(50, 50, 250, 250, outline="red", fill="gray")

root.mainloop() 