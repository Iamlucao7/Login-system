#Importas as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Criar janela
jan = Tk()
jan.title("Inov4 Tech - Acess Painel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False) #Não será possível mexer na largura
jan.attributes("-alpha", 0.9)

#====== Carregando Imagens
logo = PhotoImage(file="LOGIN/icons/logo.png")
azul = "#00BFE9"
branco = "#FFFFFF"
preto_cinzento = "#011A20"
#===== Widgets =================
LeftFrame = Frame(jan, width=225, height=300, bg=branco, relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=370, height=300, bg=azul, relief="raise")
RightFrame.pack(side=RIGHT)

Logolabel = Label(LeftFrame, image=logo, bg=branco)
Logolabel.place(x=7, y=59)

#==== Login ===========
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=113)

PassLabel = Label(RightFrame, text="Password :", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
PassLabel.place(x=5, y= 135)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place (x=150, y=146)

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=20)
LoginButton.place(x=125, y=200)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20)
RegisterButton.place(x=125, y=235)

jan.mainloop()
