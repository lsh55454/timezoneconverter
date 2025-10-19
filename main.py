from tkinter import *

# tkinter object instance
root = Tk()

# title, geometry, resizability
root.title("Time Zone Converter")
root.geometry("300x200+100+100")
root.resizable(False, False)

# Label : title
title = Label(root, text="Time Zone Converter", font=("Consolas", 15, "bold"))

title.pack()





root.mainloop()

