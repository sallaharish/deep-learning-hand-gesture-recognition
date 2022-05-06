import os
import time
import cv2
import numpy as np
from tkinter import  *
from PIL import Image,ImageTk
image_path=r"C:\Users\Harish\Desktop\project\images"
global iii 
iii = -1
low = 421
high = 431

label=['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]



def cap():
    global iii
    iii = iii + 1
    source_dir=os.path.expanduser(r"C:\Users\Harish\Desktop\project\images"+label[iii])
    #os.mkdir(r"C:\Users\geethika\OneDrive\Documents\project\trails\dataset\\"+label)
    #cam=cv2.VideoCapture(0)
    print("collecting images for {}".format(label[iii]))
    #time.sleep(5)
    for imgnum in range(low,high):
         ret,frame=cam.read()
         frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
         frame=cv2.flip(frame,1)
         x1=int(0.5*frame.shape[1])
         y1=10
         x2=frame.shape[1]-10
         y2=int(0.5*frame.shape[1])
    
         cv2.rectangle(frame,(x1-1,y1-1),(x2+1,y2+1),(255,0,0),1)
         ro = frame[y1:y2,x1:x2]
         ro = cv2.cvtColor(ro,cv2.COLOR_BGR2RGB)
         ro = cv2.resize(ro, (128,128))
         imagename=os.path.join(image_path,label[iii],'{}.jpg'.format(imgnum))
         print(imgnum)
         cv2.imwrite(imagename,ro)
         cv2.imshow("frame",frame)
         time.sleep(1)
         if cv2.waitKey(1) and 0xFF ==ord('q'):
              break


root= Tk()
root.geometry("900x900")
root.configure(bg="black")
Label(root,text="SIGN LANGUAGE DETECTION",font=("times new roman",30,"bold"),bg="black",fg="white").pack()
f1=LabelFrame(root,bg="white")
f1.pack()
L1=Label(f1,bg="white")
L1.pack()
B=Button(root,text="capture",command=cap)
B.pack()

panel = Label(root)
panel.place(x = 100, y = 650, width = 200, height = 50)

#panel2 = Label(root) # initialize image panel
#panel2.place(x = 100, y = 800, width = 200, height = 50)

str=""
word=""
current_symbol="Empty"
panel.config(text="current_symbol:",font=("Courier",10))
#spanel2.config(text="word:",font=("Courier",10))
global cam
cam = cv2.VideoCapture(0)

#cv2.namedWindow("test")
global roi

while True:
    ret,frame=cam.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame=cv2.flip(frame,1)
    x1=int(0.5*frame.shape[1])
    y1=10
    x2=frame.shape[1]-10
    y2=int(0.5*frame.shape[1])
    
    cv2.rectangle(frame,(x1-1,y1-1),(x2+1,y2+1),(255,0,0),1)
    global roi
    roi = frame[y1:y2,x1:x2]
    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (128,128))
    frame=ImageTk.PhotoImage(Image.fromarray(frame))
    

    L1['image']=frame
    root.update()

    if not ret:
        print("failed to grab frame")
        break
    #cv2.imshow("test",frame)




cam.release()

cv2.destroyAllWindows()