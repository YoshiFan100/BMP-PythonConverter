from tkinter import *
import tkinter.messagebox
import time
from tkinter import filedialog
from PIL import Image
root = Tk()
root.minsize(600, 100)

def fun(arg):
    global p
    if arg == 1:
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = ((".png .jpg .jpeg files","*.png *.jpg *.jpeg"),("all files","*.*")))
  
            
        t1 = Label(text="You selected " + root.filename + ".").place(x=200, y=0)
        newFile = str(re.sub(".jpg|.png|.jpeg", "", root.filename))
        Image.open(str(root.filename)).save(str(newFile) + ".bmp")
    if arg == 2 :
     
        root.destroy()
        

t1 = Label(text="Select a .jpg, .jpeg or .png file to be converted to a .bmp file.").place(x=200, y=0)
b1 = Button(root, text="Browse Directorys", command=lambda: fun(1)).place(x=250, y=85)




b2 = Button(root, text="Exit", command=lambda: fun(2)).place(x=520, y=0)
