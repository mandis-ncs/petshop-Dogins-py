#deve fazer a instalação de PIL primeiro. Abrir cmd e digitar 'pip install Pillow'
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
#PIL permite importar imgs externas

tela = Tk()

def sair_tela():
    tela.destroy()
    return

tela.title("Cadastro do Serviço")
tela.configure(background='#d3d3d3')
tela.geometry("700x500")
tela.resizable(False,False)
largura = 700
altura = 500

#campos de cadastro
lbl_titulo = Label(tela, text="Cadastro do serviço").place(x=300, y=10)

lbl_codigo = Label(tela, text="Codigo do serviço", bg="#d3d3d3")
txt_codigo = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_codigo.place(x=50, y=50)
txt_codigo.place(x=50, y=70)

lbl_nome_servico = Label(tela, text="Nome do serviço", bg="#d3d3d3")
txt_nome_servico = Entry(tela, width=40, borderwidth=1, fg="blue", bg="white")
lbl_nome_servico.place(x=200, y=50)
txt_nome_servico.place(x=200, y=70)

lbl_data_atualizacao = Label(tela, text="Data de atualização", bg="#d3d3d3")
txt_data_atualizacao = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_data_atualizacao.place(x=500, y=50)
txt_data_atualizacao.place(x=500, y=70)

lbl_data_cadastro = Label(tela, text="Data de cadastro", bg="#d3d3d3")
txt_data_cadastro = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_data_cadastro.place(x=500, y=100)
txt_data_cadastro.place(x=500, y=120)

lbl_valor = Label(tela, text="Valor", bg="#d3d3d3")
txt_valor = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_valor.place(x=50, y=100)
txt_valor.place(x=50, y=120)

lbl_duracao = Label(tela, text="Tempo de duração", bg="#d3d3d3")
txt_duracao = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_duracao.place(x=200, y=100)
txt_duracao.place(x=200, y=120)

#campo de descriçao Text
lbl_desc = Label(tela, text="Descrição", bg="#d3d3d3")
txt_desc =Text(tela)
lbl_desc.place(x=50, y=150)
txt_desc.place(x=50, y=170, width=400, height=100)

#armazenando imagens nas variaveis
foto_salvar = PhotoImage(file= r"imgs\salvar-arquivo.png")
foto_excluir = PhotoImage(file= r"imgs\lixeira.png")
foto_alterar = PhotoImage(file= r"imgs\editar.png")
foto_consultar = PhotoImage(file= r"imgs\lupa.png")
foto_sair = PhotoImage(file= r"imgs\excluir.png")

#criando botoes do crud
btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP)
btn_salvar.place(x=130, y=390)

btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP)
btn_excluir.place(x=210, y=390)

btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound=TOP)
btn_alterar.place(x=290, y=390)

btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP)
btn_consultar.place(x=370, y=390)

btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair_tela)
btn_sair.place(x=500, y=390)

#posicionamento de tela no centro da tela do computador
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))


tela.mainloop()