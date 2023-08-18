import cv2
import matplotlib.pyplot as plt
import easygui
import numpy as np
import imageio
import sys
from tkinter import *
x=Tk()
x.geometry("400x400")

def sketch(imagepath):
    oi=cv2.imread(imagepath)
    oi_1=cv2.cvtColor(oi,cv2.COLOR_BGR2RGB)
    ReSized1 = cv2.resize(oi_1, (960, 540))
    grey_img=cv2.cvtColor(oi, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grey_img, (960, 540))
    invert_img=cv2.bitwise_not(grey_img)

    blur_img=cv2.GaussianBlur(invert_img, (21, 21),sigmaX=0, sigmaY=0)
    ReSized3 = cv2.resize(blur_img, (960, 540))
    sketch_img=cv2.divide(grey_img,255-blur_img, scale=255)
    ReSized4 = cv2.resize(sketch_img, (960, 540))
    cv2.imwrite("sketch.png", sketch_img)
    # Plotting the whole transition
    images=[ReSized1, ReSized2, ReSized3, ReSized4]
    

    fig, axes = plt.subplots(2,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    plt.show()
    if oi is None:
        print("hgcijahcj")
        sys.exit()

def upload():
    imagepath=easygui.fileopenbox()
    sketch(imagepath)



label = Label(x,background="cyan",text="cartoonify")
label.place(x=200,y=10)
button = Button(x,text="upload",command=upload)
button.place(x=50,y=50)
# button1=Button(x, text="cartoonify",command=cartoonify)

# button1.place(x=50,y=100)

x.mainloop()