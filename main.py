from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face recognition system")
        #first image
        img=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\Untitled design(1).jpg")
        img=img.resize((500,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=200)

        #second image
        img1=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\Untitled design (2).jpg")
        img1=img1.resize((600,250),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=600,height=250)

        #third image
        img2=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\Untitled design.jpg")
        img2=img2.resize((600,200),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=600,height=200)
 
        #bg image
        img3=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\Untitled design (3).jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\student button.jpg")
        img4=img4.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=80,width=220,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=280,width=220,height=40)

         #detect face button
        img5=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\photos (5).jpg")
        img5=img5.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=80,width=220,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=280,width=220,height=40)

          #attendance button
        img6=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\attendance.jpg")
        img6=img6.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=80,width=220,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=280,width=220,height=40)

        #help button
        img7=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\output8.png")
        img7=img7.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=80,width=220,height=200)

        b1_1=Button(bg_img,text="Help desk",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=280,width=220,height=40)

        #train face button
        img8=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\Untitled design (7).jpg")
        img8=img8.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=330,width=220,height=200)

        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=530,width=220,height=40)

          #photos button
        img9=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\photos (1).jpg")
        img9=img9.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=330,width=220,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=530,width=220,height=40)

         #devolper button
        img10=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\software developer.jpeg")
        img10=img10.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=330,width=220,height=200)

        b1_1=Button(bg_img,text="Devoloper",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=530,width=220,height=40)

        #exit button
        img11=Image.open(r"C:\Users\USER\OneDrive\Desktop\4th sem project\images\output.png")
        img11=img11.resize((220,200),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=330,width=220,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=530,width=220,height=40)

    def  open_img(self):
        os.startfile("data")    
      
      #=======functions button=========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)   

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)       


      















if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        