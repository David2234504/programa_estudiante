from tkinter import *

# crea el Toplevel y establece su transparencia
toplevel = Toplevel()
toplevel.attributes('-alpha', 0.5)

# crea los Frame dentro del Toplevel
frame1 = Frame(toplevel, width=200, height=200, bg='red')
frame1.pack()

frame2 = Frame(toplevel, width=200, height=200, bg='green')
frame2.pack()

# crea la ventana principal y la muestra
root = Tk()
root.geometry('400x400')
root.mainloop()
