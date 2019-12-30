from tkinter import *


mapa=Tk()
scrollbar = Scrollbar(mapa)
scrollbar.pack(side=RIGHT, fill=BOTH)
canvas = Canvas(mapa, width=150, height=150)
canvas.create_line(0, 0, 200, 300)
canvas.create_line(0, 100, 300, 50, fill="red", dash=(4, 4))

canvas.create_rectangle(50, 25, 150, 275, fill="blue")
canvas.pack()

  
canvas.pack()
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=canvas.yview)
canvas.configure(scrollregion=canvas.bbox("all"))

mainloop()
