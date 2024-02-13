from tkinter import *
class dash1:
    def __init__(self,window):
        self.window=window
        self.window.title("Dashboard")
        self.window.geometry("1300x670+20+20")
        self.window.config(bg='#F2E3D5')

        title=Label(self.window,text='TOOLKIT',compound=LEFT
                    ,font=('Georgia',30,'bold'),bg='#024959',fg='White',anchor="w",padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        self.lbl_clock=Label(self.window,text='Welcome To Tookit \t\t Date:dd-mm-yyyy\t\t Time:hh:mm:ss',
                    font=('Georgia',15),bg='#012E40',fg='White')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        framef=Frame(self.window,bd=2,relief=RIDGE,bg='#F2E3D5')
        framef.place(x=200,y=102,width=1200,height=600)

        btn_calculator=Button(framef,text='Claculator',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2',borderwidth=2)
        btn_calculator.place(x=70,y=50,height=130,width=250)

        btn_Wheather=Button(framef,text='Weather',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_Wheather.place(x=420,y=50,height=130,width=250)
        
        btn_notepad=Button(framef,text='Notepad',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_notepad.place(x=770,y=50,height=130,width=250)

        btn_qr_gen=Button(framef,text='QR Generator',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_qr_gen.place(x=70,y=200,height=130,width=250)

        btn_clock=Button(framef,text='Clock',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_clock.place(x=420,y=200,height=130,width=250)
        
        btn_speed_check=Button(framef,text='Speed Check',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_speed_check.place(x=770,y=200,height=130,width=250)

        btn_to_do=Button(framef,text='TO DO',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_to_do.place(x=70,y=350,height=130,width=250)

        btn_white_bord=Button(framef,text='White Bord',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_white_bord.place(x=420,y=350,height=130,width=250)
        
        btn_calender=Button(framef,text='Calender',font=('Georgia',20),bg="#3CA6A6",fg='black',
                            cursor='hand2')
        btn_calender.place(x=770,y=350,height=130,width=250)


        
if __name__=="__main__":
    window=Tk()
    obj=dash1(window)
    window.state('zoomed')
    window.mainloop()
