from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"C:\Users\USER\Desktop\4th sem project\images\photos (3).jpg")
        img_top = img_top.resize((1530,750), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl =ttk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=750)

        # frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=500)

        img_top1 = Image.open(r"C:\Users\USER\Desktop\4th sem project\images\aman.jpeg")
        img_top1 = img_top1.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        f_lbl =ttk.Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)
        
        #developr info
        dev_label=Label(main_frame,text="Hello,My name is AMAN T.K",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am a Bvoc software Devolopment student.",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        







if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()  
