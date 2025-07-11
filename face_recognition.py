from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2.face
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np




class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
       
       #1st image
        img_top = Image.open(r"C:\Users\USER\Desktop\4th sem project\images\Untitled design (2).jpg")
        img_top = img_top.resize((650,750), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl =ttk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=650, height=750)

       #2nd image
        img_bottom = Image.open(r"C:\Users\USER\Desktop\4th sem project\images\Untitled design (3).jpg")
        img_bottom = img_bottom.resize((950,750), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl =ttk.Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=45, width=950, height=750)  


         #button
        b1_1=Button(f_lbl,text="Face Detector",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_1.place(x=460,y=422,width=250,height=34)

    #============attendance===========================   
    def mark_attendance(self,i,r,n,d):
        with open("att.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))  
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")



    #==============face recognition======================    

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select student_name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n) if n else "Unknown"

                my_cursor.execute("select roll_number from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r) if r else "Unknown"

                my_cursor.execute("select department from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d) if d else "Unknown"

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:    
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()                