from tkinter import *
from tkinter import messagebox
from tkinter import Frame
from tkinter.filedialog import test
import numpy as np
from PIL import ImageTk,Image
import cv2 as cv

main=Tk()
main.title("LUCY")
main.iconbitmap("Z:\PYTHON\Face detection\icon.ico")
main.geometry("1920x720+0+80")


def mainwin():
    def exit():
        win.destroy()
    def camera():
        global name1
        import cv2 as cv
        import numpy as np
        import face_recognition 
        import os
        import fnmatch
        record=[]


        for root, dir, files in os.walk("Z:\PYTHON\opencv\image"):
                    
                if root=="Z:\PYTHON\opencv\image":

                    for items in fnmatch.filter(files, "*"):
                        record.append(items)
                        print("items:")
                        # print(dir)
                        print(items)
        print(len(record))
        def encoding():
            encodings=[]
            for i in record:
                img=face_recognition.load_image_file("Z:\PYTHON\opencv\image\\"+str(i),mode='RGB')
                img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
                faceencoding=face_recognition.face_encodings(img)
                encodings.append(faceencoding)
                
                
            return encodings


        data=encoding()
        print(type(data))
        print(len(data))


        cap=cv.VideoCapture(0)
            
        while True:
            sucess,frame=cap.read(0)
            img=cv.resize(frame,(0,0),None,0.25,0.25)
            img=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
                
            fl=face_recognition.face_locations(img)
            fe=face_recognition.face_encodings(img)
            result=None
            for (e,name) in zip(data,record):
                try:
                    result=face_recognition.compare_faces(e[0],fe)
                    dis=face_recognition.face_distance(e,fe)
                    

                    
                except:
                    pass

                if result!=None:
                        
                    if result==[True]:
                        name1=name.split(".")
                        print(name1[0])
                        


                
            cv.imshow("frame",frame)
            
            if cv.waitKey(1)==ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()

        



    def compare():
        from tkinter import filedialog
        import face_recognition
        first_file=filedialog.askopenfilename(initialdir="G:\'",title="select first file",filetype=(("all files","*.*"),("text files","*.txt"))) #takes minimum 2 options in filetype
        second_file=filedialog.askopenfilename(initialdir="G:\'",title="select second file",filetype=(("all files","*.*"),("text files","*.txt")))
        print(first_file,second_file)
        try:
            img1=face_recognition.load_image_file(first_file,mode='RGB')
            img1=cv.cvtColor(img1,cv.COLOR_BGR2RGB)

            img2=face_recognition.load_image_file(second_file,mode='RGB')
            img2=cv.cvtColor(img2,cv.COLOR_BGR2RGB)
            #---------first file--------------------------------------------------------------------
            fl=face_recognition.face_locations(img1)[0]
            fe=face_recognition.face_encodings(img1)[0]
            cv.rectangle(img1,(fl[3],fl[0],fl[1],fl[2]),(0,255,0),thickness=2)
            # cv.imshow("first file",img1)
            #----------second file------------------------------------------------------------------
            fl2=face_recognition.face_locations(img2)[0]
            fe2=face_recognition.face_encodings(img2)[0]
            cv.rectangle(img2,(fl2[3],fl2[0],fl2[1],fl2[2]),(0,255,0),thickness=2)
            # cv.imshow("second file",img2)
        

            result=face_recognition.compare_faces([fe],fe2)
            dis=face_recognition.face_distance([fe],fe2)
            # print(fe,fe2)
            print(result,dis)
            if result==[True]:
                messagebox.showinfo("Completed","Match Found with"+ " "+str(round(dis[0]*100))+"%"+" " +" accuracy")
            elif result==[False]:
                messagebox.showinfo("Completed","Match Not Found")
        except:
            messagebox.showinfo("Error","Could not compare images")



        cv.waitKey(0)
    
    def data():
        pass

    global info_frame
    global data_image
    global compare_image
    global camera_image
    global wall_image
    global exit_image
    main.destroy()
    win=Tk()
    win.title("LUCY")
    win.iconbitmap("Z:\PYTHON\Face detection\icon.ico")
    win.geometry("1920x720+0+80")


    #-----exit icon------------
    imgexit=Image.open("Z:\PYTHON\Face detection\exit.ico")
    exit_image=ImageTk.PhotoImage(imgexit)
    exit_enter=Button(win,image=exit_image,background="white",borderwidth=0,command=exit)
    exit_enter.place(x=1450,y=680)
    #---------options--------------
    #---1. real time recognition
    #---2. compare two faces

    imgcamera=Image.open("Z:\PYTHON\Face detection\camera.png")
    imgcamera=imgcamera.resize((50,50))
    camera_image=ImageTk.PhotoImage(imgcamera)
    camera_button=Button(win,image=camera_image,background=None,borderwidth=0,command=camera)
    camera_button.place(x=600,y=200)

    imgcompare=Image.open("Z:\PYTHON\Face detection\image.png")
    imgcompare=imgcompare.resize((50,50))
    compare_image=ImageTk.PhotoImage(imgcompare)
    compare_button=Button(win,image=compare_image,background=None,borderwidth=0,command=compare)
    compare_button.place(x=690,y=200)
     


    info_frame=LabelFrame(win,padx=50,pady=50)
    info_frame.grid(row=1,column=1)
    







#-----------password--------------
def open():
    password=epass.get()
    print(password)
    if password=="2587":
        mainwin()
    else:
        messagebox.showwarning("error","Wrong password")

#----------into image------------
img1=Image.open("Z:\PYTHON\Face detection\img1.png")
img1=img1.resize((1200,400))
winimage=ImageTk.PhotoImage(img1)
# mainwin=Frame(main,background="white",border=0,width=1200,height=400).place(x=180,y=0)
winimagelb=Label(main,image=winimage).place(x=180,y=0)

#----------password entry------------
lpass=Label(main,text="Password", font=("times new roman",20,"italic"),fg="black").place(x=700,y=450)
epass=Entry(main,borderwidth=0,width=50,font=("times new roman",10,'italic'),border=2)
epass.config(show="*")
epass.place(x=600,y=500)


#--------pass_entry-------------------
img2=Image.open("Z:\PYTHON\Face detection\icons8-enter-96.ico")
pass_image=ImageTk.PhotoImage(img2)
print(pass_image)
pass_enter=Button(main,image=pass_image,background=None,borderwidth=0,command=open)
pass_enter.place(x=735,y=550)



print(main["bg"])


main.mainloop()
