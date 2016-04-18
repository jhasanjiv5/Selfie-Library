# A basic GUI program using TK
# Created by David Briddock
import barfacevid3_data
from Tkinter import *
import tkMessageBox
import subprocess as sub


from PIL import ImageTk, Image
import os
#p = sub.Popen('/home/pi/New/barfacevid3_data.py', stdout=sub.PIPE,stderr=sub.PIPE)
#output, errors = p.communicate()

def init(root):
  root.title("Basic GUI Program")
  root.minsize(800, 400)
  root.configure(background='#a1dbcd')
  btn.pack()
  P.pack()
  K.pack()
  L.pack()
  

# find button callback
def hello():
 # tkMessageBox.showinfo("Lend Book", "Book has been lended")
  barfacevid3_data.face_track()
  #tkMessageBox.showinfo("Loan Book", "Please face the camera and show the book barcode")
  #cv2image = 
  #img = Image.fromarray(cv2image)
  #img = img.resize((250, 250),Image.ANTIALIAS)
  #panel = video(root, image = img)
  #panel.pack(side = "bottom", fill ="both", expand = "yes")
# create top-level window object
def quit1():
  global root
  root.quit()
def Lend():
  tkMessageBox.showinfo("Lend Book", "Book has been lended")
  root.quit()
root = Tk()
#text = Text(root)



# create a widget
Label(text="Selfie Library", fg = "blue", bg = "light green", font = "Helvetica 50 bold italic").pack(fill=X,pady=20)
#logo = PhotoImage(file="/home/pi/New/library.gif")
#w1 = Label(root, compound = CENTER, padx =0.5, image=logo).pack(pady=0.5)
btn = Button(root, text="Start", fg="darkgreen",command=hello)
#text = Text(root, height=10, width=20)
P = Text(root, height=1, width=35)
P.insert(END, "Face camera along with book barcode")
#text.insert(END, "Hi")
K = Button(root, text="Lend Book", fg="darkgreen",command=Lend )
K.pack(side=LEFT, padx=10)
L = Button(root, text="Exit", fg="darkgreen", command=quit1)
L.pack(side=RIGHT, padx=10)
#root.mainloop()
# initialise and start main loop
init(root)
mainloop()
