from tkinter import*

def do_something():
    print("You clicked a menu item")

root = Tk()

menu_bar = Menu(root)

root.config(menu=menu_bar)

file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=do_something)
file_menu.add_command(label="Open", command=do_something)
file_menu.add_command(label="Exit", command=root.quit)

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=do_something)

root.mainloop() 