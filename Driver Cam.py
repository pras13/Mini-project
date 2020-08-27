

import numpy
from pygame import mixer
import time
import cv2
from tkinter import * # This tkinter is a GUI(graphical user interface) method used to craete fast interface with python and it is a standard python interface
                       #to "Tk" the GUI toolkit

import tkinter.messagebox # This is a widget used to display the message boxes in python applications here we in our project used this to display
                             #contributors name and project details

root=Tk()  #To initialize tkinter, we have to create a Tk root widget, which is a window with a title bar and other decoration provided by the window manager.
            #The root widget has to be created before any other widgets and there can only be one root widget.

root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2) #It works like a container, which is responsible for arranging the position of other widgets.
                                                   #It uses rectangular areas in the screen to organize the layout and to provide padding of these widgets

frame.pack(fill=BOTH,expand=1)
root.title('Driver Cam')
frame.config(background='light blue')
label = Label(frame, text="Driver Cam",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file=r"C:\Users\PRASANNA\Desktop\manuris\Drowsiness-monitoring-Using-OpenCV-Python-master\demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)



def hel(): #this option tells about what is cv2
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Prasanna \n2. Dinesh \n3. Arshiya \n4. Nikhil \n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   
# These are present in the menu bar at left top corner
menu = Menu(root) #The Menu widget is used to create various types of menus (top level, pull down, and pop up) in the python application.
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1) #It is used to create a hierarchical menu to the parent menu by associating the given menu to the parent menu.
subm1.add_command(label="Open CV Docs",command=hel) #It is used to add the Menu items to the menu.

subm2 = Menu(menu) # same this is also another menu widget for details of contibutors and all
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri) 

def exitt(): # exit from window
   exit()
  
def web(): #capturing video from camera no detection here
   capture =cv2.VideoCapture(0) # here the argument zero(0) means we are using webcam of our laptop 
   while True:      #capturing frame by frame 
      ret,frame=capture.read()  #cap.read() returns a bool (True/False). If frame is read correctly, it will be True.
                                #So you can check end of the video by checking this return value.
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert it into grayscale video 
      cv2.imshow('frame',frame) #displaying the resulting frame
      if cv2.waitKey(1) & 0xFF ==ord('q'): #Since we want to have a way to break the loop and finish the program,
                                           #we will use the waitKey function to check if a given key was pressed.
                                          #So, if that key was pressed, we will break the loop.
         
         break
   capture.release() # When everything done, release the capture this is good practice
   cv2.destroyAllWindows()

def webrec(): #saving a video no detection
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') #This time we create a VideoWriter object
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))#specify the output filename and fourcc is a code to save the video in enough size
                                                            #11.0 is frames per second(fps) and nxt is frame size
   
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release() #releasing both saving and capturing video
   cv2.destroyAllWindows()   

def webdet(): #detecting face and eye while capturing the video itself
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml') #will be using Haar Classifier, which is a machine learning based approach, an algorithm created by Paul Viola and Michael Jones;
                                                               #which are trained from many many positive images (with faces) and negatives images (without faces).
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

       #Now for each frame, we have to classify the face so it is inside while loop.
    #We first read the frame, then convert to a grayscale of each frame and then detects faces of different sizes in the input image.
    #Now our work will be to draw rectangles on the classified face images and to classify the eyes inside each of those rectangles,
       
       faces = face_cascade.detectMultiScale(gray)


       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          #so after making rectangles we have added the eye classifier and make rectangles around eyes also. 
           
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame) #And finally, Display the faces and eyes with rectangular boxes around
       if cv2.waitKey(1) & 0xff == ord('q'): #This all will be repeated until we press the escape button,
                                                #so the final step is to break the loop when Esc is pressed.
          break
   capture.release()
   cv2.destroyAllWindows()


def webdetRec():#our detection is saved into file like recorded
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:#Now we find the faces in the image. If faces are found, it returns the positions of detected faces as Rect(x,y,w,h).
                   #Once we get these locations, we can create a ROI for the face
                   #and apply eye detection on this ROI-Region of interest (since eyes are always on the face !!! ).
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        

           eye_g = eye_glass.detectMultiScale(roi_gray)# Next, we poke around for some eyes using that roi_gray  
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   
def blink(): #this function does the same classification but also along with that for every blink of eye is
                #also detected using inbuilt blinkclassifier and pops a sound
   
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



         blink = blink_cascade.detectMultiScale(roi_gray) #classifying blinking


         for(eyx,eyy,eyw,eyh) in blink: #even it is blink u need to draw rectangle around eyes
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()

            
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()

#placing our buttons with options in our created frame   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=blink,text='Detect Eye Blink & Record With Sound',font=('helvetica 15 bold'))
but5.place(x=5,y=400)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)


root.mainloop()#this is just how tkinter works -- you always end your script by calling the mainloop method of the root window.
                  #When that method returns, your program will exit.

