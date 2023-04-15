from tkinter import *
import subprocess
from PIL import Image, ImageTk
tela = Tk()

#criando funcoes para redirecionar telas nos menus
def abrir_tela_animais():
    subprocess.run(["python", "pet-registration.py"])

def abrir_tela_clientes():
    subprocess.run(["python", "owner-registration.py"])

def abrir_tela_servicos():
    subprocess.run(["python", "services-registration.py"])

def sair_tela():
    tela.destroy()
    return

tela.title("Menu Dogins")
tela.geometry("600x300")
tela.resizable(False,False)
tela.configure(background='#d3d3d3')
largura = 600
altura = 300

#criando barra de menu superior
barra_menus = Menu(tela)

#criando opcao da barra de menu e armazenando nas variaveis
opcoes_menus_arquivos = Menu(barra_menus) #associando ao Menu(barra_menus)
opcoes_menus_gestao = Menu(barra_menus)
opcoes_novo = Menu(opcoes_menus_arquivos) #associando submenu a opcao 'Arquivo'

#adicionando label 'Arquivo' na barra
barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
#criando sub menus de 'Arquivo'
opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo)
opcoes_menus_arquivos.add_command(label="Abrir")
opcoes_menus_arquivos.add_command(label="Salvar")
opcoes_menus_arquivos.add_command(label="Salvar como...")
opcoes_menus_arquivos.add_separator()
opcoes_menus_arquivos.add_command(label="Sair", command=tela.quit)

#adicionando label 'Gestao' na barra
barra_menus.add_cascade(label="Gestao", menu=opcoes_menus_gestao)
#criando sub menus de 'Gestao'
opcoes_menus_gestao.add_command(label="Animais", command=abrir_tela_animais)
opcoes_menus_gestao.add_command(label="Clientes", command=abrir_tela_clientes)
opcoes_menus_gestao.add_command(label="Serviços", command=abrir_tela_servicos)

#criando opcoes dentro do sub menu 'Novo'
opcoes_novo.add_command(label="Salvar Imagem")
opcoes_novo.add_command(label="Upload de arquivos")

#adicionando configuracao do menu a tela principal
tela.config(menu=barra_menus)

#adicionando botoes ao menu
foto_logo_org= Image.open("imgs/Logo.png")
fotoResize = foto_logo_org.resize((200, 50))
foto_logo = ImageTk.PhotoImage(fotoResize)
lbl_foto_logo = Label(bg="#FFFFFF", image=foto_logo)

foto_sair = PhotoImage(file= r"imgs\sair.png")
foto_pet = PhotoImage(file= r"imgs\pegada.png")
foto_dono = PhotoImage(file= r"imgs\owner.png")
foto_servico = PhotoImage(file= r"imgs\servico.png")

lbl_logo = Label(tela, text="Para pets auudaciosos", compound=TOP, image=foto_logo)
lbl_logo.place(x=200, y=180)

btn_pet = Button(tela, text="Cadastrar pet", image=foto_pet, compound=TOP, command=abrir_tela_animais)
btn_pet.place(x=100, y=80)

btn_dono = Button(tela, text="Cadastrar cliente", image=foto_dono, compound=TOP, command=abrir_tela_clientes)
btn_dono.place(x=200, y=80)

btn_servico = Button(tela, text="Cadastrar serviço", image=foto_servico, compound=TOP, command=abrir_tela_servicos)
btn_servico.place(x=320, y=80)

btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair_tela)
btn_sair.place(x=440, y=80)

tela.mainloop()