from tkinter import *
import datetime

janela = Tk()
janela.title('Minha calculadora')
janela.geometry('260x250')
janela.resizable(FALSE, FALSE)
janela.configure(background='#00ced1')

b_1 = Button(janela, text="1", width=11, height=2)
b_1.place(x=0.5, y=100)

b_2 = Button(janela, text="2", width=11, height=2)
b_2.place(x=86.5, y=100)

b_3 = Button(janela, text="3", width=11, height=2)
b_3.place(x=173, y=100)

b_4 = Button(janela, text="4", width=11, height=2)
b_4.place(x=0.5, y=140)

b_5 = Button(janela, text="5", width=11, height=2)
b_5.place(x=86.5, y=140)

b_6 = Button(janela, text="6", width=11, height=2)
b_6.place(x=173, y=140)

b_7 = Button(janela, text="7", width=11, height=2)
b_7.place(x=0.5, y=180)

b_8 = Button(janela, text="8", width=11, height=2)
b_8.place(x=86.5, y=180)

b_9 = Button(janela, text="9", width=11, height=2)
b_9.place(x=173, y=180)

#f_1 = Frame(janela, width=300, height=100, background='gray')
#f_1.place(relx=0, rely=0)
#f_1.pack()

agora = datetime.datetime.now()
print(agora)


label_1 = Label(janela, text="oi", font=('Arial Bold', 20), fg='white', background='#00ced1', width=22)
label_1.grid(row=1, column=1)
label_1.pack()


janela.mainloop()
