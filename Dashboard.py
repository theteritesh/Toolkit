from tkinter import *
from tkinter import ttk
from Calculator import CalculatorClass
class dash1:
    def __init__(self,window):
        self.window=window
        self.window.title("Dashboard")
        self.window.geometry("1300x670+20+20")
        self.window.config(bg='#FFFFFF')

        #title
        title=Label(self.window,text='TOOLKIT',compound=LEFT
                    ,font=('Georgia',30,'bold'),bg='#575200',fg='White',anchor="w",padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #welcome title with clock
        self.lbl_clock=Label(self.window,text='Welcome To Tookit \t\t Date:dd-mm-yyyy\t\t Time:hh:mm:ss',
                    font=('Georgia',15),bg='#8a6626',fg='White')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        menu_frame=Frame(self.window,bg="Dark gray")
        menu_frame.place(x=0,y=100,width=200,height=610)

        #creat button frame
        btn_frame=Frame(self.window)
        btn_frame.place(x=200,y=100,width=1170,height=610)
    
        main_frame=Frame(btn_frame,bg="gray")
        main_frame.pack(fill=BOTH,expand=1)

        #create canvas
        my_canvas=Canvas(main_frame,height=150,width=1150)
        my_canvas.pack(side=LEFT,fill=BOTH)
        #Add scrolbar to canvas
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)

        #configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))


        #create another frame Inside canvas
        second_frame=Frame(my_canvas)
        #add new frame to window in the canvas
        my_canvas.create_window((0,0),window=second_frame,anchor="nw")

        #buttons 
        btn_calculator=Button(second_frame,text='Calculator',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',borderwidth=2,height=3,width=15,command=self.calculator)
        btn_calculator.grid(row=1,column=0,padx=10,pady=10)

        btn_Wheather=Button(second_frame,text='Weather',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_Wheather.grid(row=2,column=0,padx=10,pady=10)

        btn_notepad=Button(second_frame,text='Notepad',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_notepad.grid(row=3,column=0,padx=10,pady=10)

        btn_pdf_viewer=Button(second_frame,text='PDF Viewer',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_pdf_viewer.grid(row=4,column=0,padx=10,pady=10)

        btn_qr_gen=Button(second_frame,text='QR Generator',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_qr_gen.grid(row=5,column=0,padx=10,pady=10)

        btn_clock=Button(second_frame,text='Clock',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_clock.grid(row=1,column=1,padx=10,pady=10)
        
        btn_speed_check=Button(second_frame,text='Speed Check',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_speed_check.grid(row=2,column=1,padx=10,pady=10)

        btn_img_comp=Button(second_frame,text='IMG Comp',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_img_comp.grid(row=3,column=1,padx=10,pady=10)

        btn_to_do=Button(second_frame,text='TO DO',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_to_do.grid(row=4,column=1,padx=10,pady=10)

        btn_white_bord=Button(second_frame,text='White Bord',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_white_bord.grid(row=5,column=1,padx=10,pady=10)
        
        btn_calender=Button(second_frame,text='Calender',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_calender.grid(row=1,column=2,padx=10,pady=10)

        btn_translator=Button(second_frame,text='Translator',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_translator.grid(row=2,column=2,padx=10,pady=10)

        btn_demo1=Button(second_frame,text='Demo1',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_demo1.grid(row=3,column=2,padx=10,pady=10)

        btn_demo2=Button(second_frame,text='demo2',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_demo2.grid(row=4,column=2,padx=10,pady=10)
        btn_demo3=Button(second_frame,text='demo3',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_demo3.grid(row=5,column=2,padx=10,pady=10)

        btn_demo4=Button(second_frame,text='Translator',font=('Georgia',20),bg="#A3842C",fg='black',
                            cursor='hand2',height=3,width=15)
        btn_demo4.grid(row=1,column=3,padx=10,pady=10)

#-----------------------------------------------------------------------------------------------------------------
    def calculator(self):
        self.new_win=Toplevel(self.window)
        self.new_obj=CalculatorClass(self.new_win)

        
if __name__=="__main__":
    window=Tk()
    obj=dash1(window)
    window.state('zoomed')
    window.mainloop()
