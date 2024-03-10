from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv

root=Tk()
root.geometry("600x700+400+80")
# root.resizable(False,False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,samplerate=freq,channels=2)
        
    try:
        temp=int(duration.get())
    except:
        print("Please Enter the Right Value")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

    if (temp==0):
     messagebox.showinfo("Time Countdown","Time's up")
    Label(text=f"{str(temp)}",font="arial 40",width=4,background="#4a4a4a").place(x=240,y=590)
        
    sound.wait()
    write("recording.wav",freq.recording)
        
        
image_icon=PhotoImage(file="Img/recorder.png")
root.iconphoto(False,image_icon)

photo=PhotoImage(file="Img/recording.png")
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(padx=5,pady=5)

Label(text="Voice Recorder",font="arial 30 bold",background="#4a4a4a",fg="white").pack()

duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)
Label(text="Enter Time in seconds",font="arial 30 bold",background="#4a4a4a",fg="white").pack()

record=Button(root,font="arial 20",text="Record",bg="#111111",fg="white",border=0,command=Record).pack(pady=30)

root.mainloop()