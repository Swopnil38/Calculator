from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.geometry("500x500")
img1 = ImageTk.PhotoImage(Image.open("image/1.jpg").resize((500,500)))
img2 = ImageTk.PhotoImage(Image.open("image/2.jpg").resize((500,500)))
img3 = ImageTk.PhotoImage(Image.open("image/3.jpg").resize((500,500)))
img4 = ImageTk.PhotoImage(Image.open("image/4.jpg").resize((500,500)))
img5 = ImageTk.PhotoImage(Image.open("image/5.jpg").resize((500,500)))


count = 1
label = Label()
label.pack()


def show():
    if count == 1:
        label.config(image=img1)
    elif count == 2:
        label.config(image=img2)
    elif count == 3:
        label.config(image=img3)
    elif count == 4:
        label.config(image=img4)
    elif count == 5:
        label.config(image=img5)
    else:
        print()




def Previous():
    global count
    count  = count - 1
    if count >= 5:
        nex['state']='disabled'
    else:
        nex['state']='normal'
    if count <= 1:
        pre['state']='disabled'
    else:
        pre['state']='normal'
    print(count)
    show()

def Next():
    global count
    count  = count + 1
    if count >= 5:
        nex['state']='disabled'
    else:
        nex['state']='normal'
    if count <= 1:
        pre['state']='disabled'
    else:
        pre['state']='normal'
    print(count)
    show()




pre = Button(window,text="Previous",command=Previous,)
pre.place(x = 0,y = 480)

nex = Button(window,text="Next",command=Next)
nex.place(x = 460,y = 480)
exi = Button(window,text="Exit",command=window.quit)
exi.place(x = 230,y=480)

if count >= 5:
    nex['state'] = 'disabled'
else:
    nex['state'] = 'normal'
if count <= 1:
    pre['state'] = 'disabled'
else:
    pre['state'] = 'normal'
show()

window.mainloop()