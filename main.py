#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import threading
import time
import folder


def splashscrn():
    w=Tk()

    #Using piece of code from old splash screen
    width_of_window = 427
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
    w.configure(bg='#ED1B76')
    w.overrideredirect(1) #for hiding titlebar

    Frame(w, width=427, height=250, background='#272727').place(x=0,y=0)
    label1=Label(w, text='A.M YANO ESQ*', fg='white', background='#272727') #decorate it 
    label1.configure(font=("Game Of Squids", 20, "bold"))   #You need to install this font in your PC or try another one
    label1.place(x=80,y=90)
    label2=Label(w, text='powered by MIEYAN0', fg='#0F9D58', bg='#272727') #decorate it 
    label2.configure(font=("Game Of Squids", 10))
    label2.place(x=100,y=180)


    label2=Label(w, text='Loading...', fg='#0F9D58', bg='#272727') #decorate it 
    label2.configure(font=("Calibri", 11))
    label2.place(x=10,y=215)

    #making animation

    image_a=ImageTk.PhotoImage(Image.open('assets/c2.png'))
    image_b=ImageTk.PhotoImage(Image.open('assets/c1.png'))




    for i in range(5): #5loops
        l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)
        folder.create_folders()

    w.destroy()
    """CALLING INITIALIZING FUNCTIONS"""
    import log_in
    log_in.w.mainloop()

def splash_thread():
    threading.Thread(target=splashscrn).start()
        

    
    
def main():
    splash_thread()
    
if __name__ == '__main__':
    main()
    


