from tkinter import *
from tkinter import messagebox


def calcularImc() -> None:
    peso = float(txt_peso.get())
    altura = float(txt_altura.get())
    imc = peso / altura ** 2
    messagebox.showinfo("Resultado", f"Seu imc é: {imc:.2f}")
    txt_peso.delete(0, END)
    txt_altura.delete(0, END)

janela = Tk()
#add titulo
janela.title("IRSO BPTUR")
janela.geometry('650x400')

label_peso = Label(janela, text='Peso: ', fg='black', font='Arial 14 bold')
label_altura = Label(janela, text='Altura: ', fg='black', font='Arial 14 bold')
label_peso.grid(row=0, column=0)
label_altura.grid(row=1, column=0)
#campo de texto
txt_peso = Entry(janela, font='Arial 13 italic')
txt_altura = Entry(janela, font='Arial 13 italic')
txt_peso.grid(row=0, column=1)
txt_altura.grid(row=1, column=1)
#botão
btn_calcular = Button(janela, text="CALCULAR", fg="yellow", width=9, height=1,
                      font='Arial 14 bold', bg='red', activebackground='black', activeforeground='white',
                      command=calcularImc)
btn_calcular.grid(row=2, column=2)

janela.mainloop()
