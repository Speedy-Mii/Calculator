import tkinter
print("Hello, World")
tk = tkinter.Tk()
tk.title("My First GUI")
label = tkinter.Label(tk, text="Hello, World")
label.pack()
tk.geometry("800x400")
tk.mainloop()