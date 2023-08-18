from captcha.image import ImageCaptcha
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import random
import string

image = ImageCaptcha(width=250, height= 80)
captchatext_length = 5
characters = string.ascii_letters + string.digits
captchatext = ""   
for index in range(captchatext_length):
    captchatext= captchatext+ random.choice(characters)
print("captcha generated: {}".format(captchatext))
data = image.generate(captchatext)
image_file= "image"+captchatext+".png"
image.write(captchatext,image_file)

def chechcaptcha():
    global captchatext1
    if b1.get()==captchatext or b1.get()==captchatext1:
        messagebox.showinfo("showinfo","Captcha is Correct")
    else:
        messagebox.showwarning("showwarning", "Captcha is Not Correct")

def refresh():
    global captchatext1
    image  = ImageCaptcha(width=250, height= 80)
    captchatext_length = 5
    characters = string.ascii_letters + string.digits
    captchatext1 = ""   
    for index in range(captchatext_length):
        captchatext1= captchatext1+ random.choice(characters)
    print("captcha generated: {}".format(captchatext1))
    data = image.generate(captchatext1)
    image_file1  = "image"+captchatext1+".png"
    image.write(captchatext1,image_file1)
    captchaimage = PhotoImage(file=image_file1)
    #refresh
    l2.config(image=captchaimage)
    l2.image=captchaimage

root = Tk()
root.title("Image Captcha")
root.geometry("500x500")
root.iconbitmap("")
root.configure(bg="lightblue")
captchaimage = PhotoImage(file=image_file)
l2 = Label(image=captchaimage)
l2.place(x=50, y=100)
l1 = Label(root, text="Image Captcha", font="bold 20")
l1.place(x=50,y=50)
b1 = Entry(root, width=50)
b1.place(x=50,y=250)
submit = Button(root, text="Submit", command=chechcaptcha)
submit.place(x=50,y=300)
refresh_button=Button(root,text="refresh",command=refresh)
refresh_button.place(x=50,y=400)
root.mainloop()
