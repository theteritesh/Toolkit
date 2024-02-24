import time
from tkinter import *
from tkinter import ttk
from Calculator import CalculatorClass
from Wheather import WheatherClass
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
        self.btn_frame=Frame(self.window)
        self.btn_frame.place(x=200,y=100,width=1170,height=610)
    
        main_frame=Frame(self.btn_frame,bg="gray")
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
        calculator_logo = PhotoImage(file="img/calculator_logo.png")
        width = 70
        height = 70
        calculator_logo = calculator_logo.subsample(calculator_logo.width() // width, calculator_logo.height() // height)
        btn_calculator = Button(second_frame, image=calculator_logo, text='Calculator', font=('Georgia', 14), bg="#A3842C", fg='black',
                                cursor='hand2', borderwidth=2, compound="top", height=110, width=230, command=self.calculator)
       
        btn_calculator.image = calculator_logo 
        btn_calculator.grid(row=1,column=0,padx=10,pady=10)

        wheather_logo = PhotoImage(file="img/whether_logo.png")
        width = 70
        height = 70
        wheather_logo = wheather_logo.subsample(wheather_logo.width() // width, wheather_logo.height() // height)
        btn_Wheather=Button(second_frame,text='Weather',image=wheather_logo,font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',compound="top", height=110, width=230,command=self.wheather)
        btn_Wheather.image = wheather_logo 
        btn_Wheather.grid(row=1,column=1,padx=10,pady=10)

        notepad_logo = PhotoImage(file="img/notepad_logo.png")
        width = 70
        height = 70
        notepad_logo = notepad_logo.subsample(notepad_logo.width() // width, notepad_logo.height() // height)
        btn_notepad=Button(second_frame,text='Notepad',image=notepad_logo,font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',compound="top", height=110, width=230)
        btn_notepad.image = notepad_logo 
        btn_notepad.grid(row=1,column=2,padx=10,pady=10)

        pdf_logo = PhotoImage(file="img/pdf_logo.png")
        width = 70
        height = 70
        pdf_logo = pdf_logo.subsample(pdf_logo.width() // width, pdf_logo.height() // height)
        btn_pdf_viewer=Button(second_frame,text='PDF Viewer',image=pdf_logo,font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',compound="top", height=110, width=230)
        btn_pdf_viewer.image = pdf_logo
        btn_pdf_viewer.grid(row=1,column=3,padx=10,pady=10)

        qr_logo = PhotoImage(file="img/qr_logo.png")
        width = 70
        height = 70
        qr_logo = qr_logo.subsample(qr_logo.width() // width, qr_logo.height() // height)
        btn_qr_gen=Button(second_frame,text='QR Generator',image=qr_logo,font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',compound="top", height=110, width=230)
        btn_qr_gen.image = qr_logo
        btn_qr_gen.grid(row=2,column=0,padx=10,pady=10)

        clock_logo = PhotoImage(file="img/clock_logo.png")
        width = 70
        height = 70
        clock_logo = clock_logo.subsample(clock_logo.width() // width, clock_logo.height() // height)
        btn_clock=Button(second_frame,image=clock_logo,text='Clock',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2', compound="top",height=110,width=230)
        btn_clock.image = clock_logo
        btn_clock.grid(row=2,column=1,padx=10,pady=10)
        
        speed_test_logo = PhotoImage(file="img/speed_test_logo.png")
        width = 70
        height = 70
        speed_test_logo = speed_test_logo.subsample(speed_test_logo.width() // width, speed_test_logo.height() // height)
        btn_speed_test=Button(second_frame,image=speed_test_logo,text='Speed Test',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_speed_test.image = speed_test_logo
        btn_speed_test.grid(row=2,column=2,padx=10,pady=10)
        
        img_comp_logo = PhotoImage(file="img/img_comp_logo.png")
        width = 70
        height = 70
        img_comp_logo = img_comp_logo.subsample(img_comp_logo.width() // width, img_comp_logo.height() // height)
        btn_img_comp=Button(second_frame,image=img_comp_logo,text='IMG Comp',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_img_comp.image = img_comp_logo
        btn_img_comp.grid(row=2,column=3,padx=10,pady=10)

        to_do_logo = PhotoImage(file="img/to_do_logo.png")
        width = 70
        height = 70
        to_do_logo = to_do_logo.subsample(to_do_logo.width() // width, to_do_logo.height() // height)
        btn_to_do=Button(second_frame,text='TO DO',image=to_do_logo,font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_to_do.image = to_do_logo
        btn_to_do.grid(row=3,column=0,padx=10,pady=10)

        white_board_logo = PhotoImage(file="img/white_board_logo.png")
        width = 70
        height = 70
        white_board_logo = white_board_logo.subsample(white_board_logo.width() // width, white_board_logo.height() // height)
        btn_white_bord=Button(second_frame,image=white_board_logo,text='White Bord',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_white_bord.image = white_board_logo
        btn_white_bord.grid(row=3,column=1,padx=10,pady=10)
        
        calender_logo = PhotoImage(file="img/calendar_logo.png")
        width = 70
        height = 70
        calender_logo = calender_logo.subsample(calender_logo.width() // width, calender_logo.height() // height)
        btn_calender=Button(second_frame,image=calender_logo,text='Calender',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_calender.image = calender_logo
        btn_calender.grid(row=3,column=2,padx=10,pady=10)

        translator_logo = PhotoImage(file="img/translator_logo.png")
        width = 70
        height = 70
        translator_logo = translator_logo.subsample(translator_logo.width() // width, translator_logo.height() // height)
        btn_translator=Button(second_frame,image=translator_logo,text='Translator',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_translator.image = translator_logo
        btn_translator.grid(row=3,column=3,padx=10,pady=10)

        demo_logo1 = PhotoImage(file="img/demo_logo.png")
        width = 70
        height = 70
        demo_logo1 = demo_logo1.subsample(demo_logo1.width() // width, demo_logo1.height() // height)
        btn_demo1=Button(second_frame,image=demo_logo1,text='Demo1',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_demo1.image = demo_logo1
        btn_demo1.grid(row=4,column=0,padx=10,pady=10)

        demo_logo2 = PhotoImage(file="img/demo_logo.png")
        width = 70
        height = 70
        demo_logo2 = demo_logo2.subsample(demo_logo2.width() // width, demo_logo2.height() // height)
        btn_demo2=Button(second_frame,image=demo_logo2,text='demo2',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_demo2.image = demo_logo2
        btn_demo2.grid(row=4,column=1,padx=10,pady=10)
        
        demo_logo3 = PhotoImage(file="img/demo_logo.png")
        width = 70
        height = 70
        demo_logo3 = demo_logo3.subsample(demo_logo3.width() // width, demo_logo3.height() // height)
        btn_demo3=Button(second_frame,image=demo_logo3,text='demo3',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_demo3.image = demo_logo3
        btn_demo3.grid(row=4,column=2,padx=10,pady=10)

        demo_logo4 = PhotoImage(file="img/demo_logo.png")
        width = 70
        height = 70
        demo_logo4 = demo_logo4.subsample(demo_logo4.width() // width, demo_logo4.height() // height)
        btn_demo4=Button(second_frame,image=demo_logo4,text='demo4',font=('Georgia',14),bg="#A3842C",fg='black',
                            cursor='hand2',height=110,width=230,compound="top")
        btn_demo4.image = demo_logo4
        btn_demo4.grid(row=4,column=3,padx=10,pady=10)
        
        self.update_content()
#-----------------------------------------------------------------------------------------------------------------
    def calculator(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=CalculatorClass(self.new_win)
    def wheather(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=WheatherClass(self.new_win)
    
    def update_content(self):
        time1=time.strftime('%I:%M:%S')
        date1=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f'Welcome To Supplement Shop Management System \t\t Date:{str(date1)}\t\t Time:{str(time1)}')
        self.lbl_clock.after(200,self.update_content)

        
if __name__=="__main__":
    window=Tk()
    obj=dash1(window)
    window.state('zoomed')
    window.mainloop()
