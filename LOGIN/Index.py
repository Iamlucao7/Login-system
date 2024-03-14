#Importas as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#Criar janela
jan = Tk()
jan.title("Inov4 Tech - Acess Painel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False) #Não será possível mexer na largura
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="LOGIN/icons/logoicon.ico")

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

'''MensagemTelaLogin = Label(RightFrame, text="FAZER LOGIN", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
MensagemTelaLogin.place(x=110, y=25)

Mensagem2TelaLogin = Label(RightFrame, text="Acessar painel", font=("Century Gothic", 12), bg=azul, fg=preto_cinzento) 
Mensagem2TelaLogin.place(x=144, y=59)'''

#==== Login ===========
UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=37)
UserEntry.place(x=109, y=113)

PassLabel = Label(RightFrame, text="Senha :", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
PassLabel.place(x=5, y= 135)

PassEntry = ttk.Entry(RightFrame, width=37, show="•")
PassEntry.place (x=109, y=146)

#Botões
LoginButton = ttk.Button(RightFrame, text="Entrar", width=20)
LoginButton.place(x=125, y=200)

def Register():
    #Removendo Widgets de login
    LoginButton.place(x=10000)
    RegisterButton.place(x=10000)
    '''MensagemTelaLogin.place(x=10000)
    Mensagem2TelaLogin.place(x=10000)'''

    #Inserindo Widgets de cadastro
    '''ListaCadastro = Label(RightFrame, text="CADASTRO", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
    ListaCadastro.place(x=110, y=5)'''
    
    NameLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
    NameLabel.place(x=5, y=38)

    NameEntry = ttk.Entry(RightFrame, width=37)
    NameEntry.place(x=109, y=52)

    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
    EmailLabel.place(x=5, y= 70)
    
    EmailEntry = ttk.Entry(RightFrame, width=37)
    EmailEntry.place (x=109, y=81)

    #Registrando usuarios no banco de dados
    def RegisterToDataBase():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        DataBaser.cursor.execute('''
        INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
        ''', (Name, Email, User, Pass))
        DataBaser.conn.commit()
        messagebox.showinfo(title='Register Info', message='Account created successfully')

    Register = ttk.Button(RightFrame, text="Registrar", width=30, command=RegisterToDataBase)
    Register.place(x=125, y=225)
    
    def voltar_para_login():
        #Removendo entradas de cadastro
        #ListaCadastro.place(x=5000)
        NameLabel.place(x=10000)
        NameEntry.place(x=10000)
        EmailLabel.place(x=10000)
        EmailEntry.place(x=10000)
        Register.place(x=10000)
        Voltar.place(x=10000)
        #Retornando para tela de login
        #ListaCadastro.place(x=5000)
        '''MensagemTelaLogin = Label(RightFrame, text="FAZER LOGIN", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
        MensagemTelaLogin.place(x=1000)
        Mensagem2TelaLogin = Label(RightFrame, text="Acessar painel", font=("Century Gothic", 12), bg=azul, fg=preto_cinzento) 
        Mensagem2TelaLogin.place(x=1000)'''
        UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg=azul, fg=preto_cinzento)
        UserLabel.place(x=5, y=100)
        LoginButton.place(x=125, y=200)
        RegisterButton.place(x=125, y=235)

    Voltar = ttk.Button(RightFrame, text="Voltar", width=30, command=voltar_para_login)
    Voltar.place(x=125, y=195)

RegisterButton = ttk.Button(RightFrame, text="Registre-se", width=20, command=Register)
RegisterButton.place(x=125, y=235)

jan.mainloop()