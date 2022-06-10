from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root=Tk()
root.geometry("1080x400")
root.configure(background="yellow")

lbl_title=Label(root,text="language translator")
lbl_title.place(relx=0.1,rely=0.2,anchor=CENTER)

lbl_input=Label(root,text="enter")
lbl_input.place(relx=0.3,rely=0.4,anchor=W)

enter_input=Text(root,height=11,width=60,padx=5,pady=5,wrap=WORD)
enter_input.place(relx=0.3,rely=0.5,anchor=W)



root.mainloop()
