from tkinter import *
from PIL import ImageTk, Image

root=Tk()


root.geometry('1000x500')
logo = ImageTk.PhotoImage(Image.open("../img/ht1.gif"))
background=Label(root, image=logo).place(x=0,y=0,relwidth=1, relheight=1)

chat_button=Button(root,justify = LEFT, bg="#b0966b", bd=0)
chat_photo=ImageTk.PhotoImage(Image.open("../img/chat1tp.gif"), width=80, height=80)
chat_button.config(image=chat_photo, width=78, height=78)
chat_button.place(x=835, y=50)

history_button = Button(root, justify = RIGHT, bg="#b0966b", bd=0)
history_photo=ImageTk.PhotoImage(Image.open("../img/hstictp.gif"), width=50, height=50)
history_button.config(image=history_photo, width=46, height=46)
history_button.place(x=850, y=180)

fav_button = Button(root, justify = RIGHT, bd=0)
fav_photo=ImageTk.PhotoImage(Image.open("../img/favictp.gif"), width=50, height=50)
fav_button.config(image=fav_photo, width=46, height=46)
fav_button.place(x=850, y=250)

aboutus_button = Button(root, bd=0)
aboutus_photo = ImageTk.PhotoImage(Image.open("../img/aboutus.gif"), width=50, height=50)
aboutus_button.config(image=aboutus_photo, width=45, height=45)
aboutus_button.place(x=845, y=390)

reset_button = Button(root, bd=0)
reset_photo = ImageTk.PhotoImage(Image.open("../img/reset.gif"), height=50, width=50)
reset_button.config(image=reset_photo, width=45, height=45)
reset_button.place(x=845, y=320)


root.mainloop()
