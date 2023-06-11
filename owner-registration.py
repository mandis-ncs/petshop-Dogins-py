#deve fazer a instalação de PIL primeiro. Abrir cmd e digitar 'pip install Pillow'
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import cv2 as cv
import numpy as np



tela = Tk()

def sair_tela():
    tela.destroy()
    return

tela.title("Cadastro do Cliente")
tela.configure(background='#d3d3d3')
tela.geometry("800x500")
tela.resizable(False,False)
largura = 900
altura = 500

#foto padrao antes d upload
fotoOriginal = Image.open("imgs/profile-owner.png")
fotoResize = fotoOriginal.resize((110, 150))
fotoPerfil = ImageTk.PhotoImage(fotoResize)
lbl_foto_Profile = Label(bg="#FFFFFF", image=fotoPerfil)
lbl_foto_Profile.place(x=50, y=50)

#criar pasta para guardar imgs
pasta_inicial = ""

#função para escolher imagem
def escolher_imagem():
    global image_path
    global image
    global rotated_image
    
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura/150
        nova_altura = int(altura/proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))
    image = cv.cvtColor(np.array(imagem_pil), cv.COLOR_RGB2BGR)
    rotated_image = np.copy(image)
    show_image(rotated_image)

#função para girar imagem
def rotate_image():
    global rotated_image
    angle = 45
    rotated_image = cv.rotate(rotated_image, cv.ROTATE_90_CLOCKWISE)
    show_image(rotated_image)

def show_image(image):
    image_pil = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    image_tk = ImageTk.PhotoImage(image_pil)
    lbl_imagem.configure(image=image_tk)
    lbl_imagem.image = image_tk


#botao chamando a função escolher_imagem
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=55, y=210)

btn_rotate = Button(tela, text="Girar imagem", command=rotate_image)
btn_rotate.place(x=65, y=250)

lbl_imagem = Label(tela)
lbl_imagem.place(x=50, y=50)

#campos de cadastro
lbl_titulo = Label(tela, text="Cadastro do cliente").place(x=400, y=10)

lbl_codigo = Label(tela, text="Codigo do cliente", bg="#d3d3d3")
txt_codigo = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_codigo.place(x=200, y=50)
txt_codigo.place(x=200, y=70)

lbl_nome_cliente = Label(tela, text="Nome do cliente", bg="#d3d3d3")
txt_nome_cliente = Entry(tela, width=50, borderwidth=1, fg="blue", bg="white")
lbl_nome_cliente.place(x=350, y=50)
txt_nome_cliente.place(x=350, y=70)

lbl_data_atualizacao = Label(tela, text="Data de atualização", bg="#d3d3d3")
txt_data_atualizacao = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_data_atualizacao.place(x=700, y=50)
txt_data_atualizacao.place(x=700, y=70)

lbl_data_cadastro = Label(tela, text="Data de cadastro", bg="#d3d3d3")
txt_data_cadastro = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_data_cadastro.place(x=700, y=100)
txt_data_cadastro.place(x=700, y=120)

lbl_cpf = Label(tela, text="CPF", bg="#d3d3d3")
txt_cpf = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_cpf.place(x=200, y=100)
txt_cpf.place(x=200, y=120)

lbl_nascimento = Label(tela, text="Data de nascimento", bg="#d3d3d3")
txt_nascimento = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_nascimento.place(x=350, y=100)
txt_nascimento.place(x=350, y=120)

lbl_idade = Label(tela, text="Idade", bg="#d3d3d3")
txt_idade = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_idade.place(x=500, y=100)
txt_idade.place(x=500, y=120)

lbl_telefone = Label(tela, text="Telefone", bg="#d3d3d3")
txt_telefone = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_telefone.place(x=200, y=150)
txt_telefone.place(x=200, y=170)

lbl_celular = Label(tela, text="Telefone", bg="#d3d3d3")
txt_celular = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_celular.place(x=350, y=150)
txt_celular.place(x=350, y=170)

lbl_cep = Label(tela, text="CEP", bg="#d3d3d3")
txt_cep = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_cep.place(x=200, y=200)
txt_cep.place(x=200, y=220)

lbl_cidade = Label(tela, text="Cidade", bg="#d3d3d3")
txt_cidade = Entry(tela, width=30, borderwidth=1, fg="blue", bg="white")
lbl_cidade.place(x=350, y=200)
txt_cidade.place(x=350, y=220)

lbl_bairro = Label(tela, text="Bairro", bg="#d3d3d3")
txt_bairro = Entry(tela, width=30, borderwidth=1, fg="blue", bg="white")
lbl_bairro.place(x=560, y=200)
txt_bairro.place(x=560, y=220)

lbl_rua = Label(tela, text="Rua", bg="#d3d3d3")
txt_rua = Entry(tela, width=50, borderwidth=1, fg="blue", bg="white")
lbl_rua.place(x=200, y=250)
txt_rua.place(x=200, y=270)


# Função para salvar
def salvar():
    var_codigo = txt_codigo.get()
    var_nome_cliente = txt_nome_cliente.get()
    var_data_atualizacao = txt_data_atualizacao.get()
    var_data_cadastro = txt_data_cadastro.get()
    var_cpf = txt_cpf.get()
    var_nascimento = txt_nascimento.get()
    var_idade = txt_idade.get()
    var_telefone = txt_telefone.get()
    var_celular = txt_celular.get()
    var_cep = txt_cep.get()
    var_cidade = txt_cidade.get()
    var_bairro = txt_bairro.get()
    var_rua = txt_rua.get()

    if (var_nome_cliente == "" or var_cpf == ""):
        messagebox.showinfo("Erro", "Há campos em branco")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute(f"INSERT INTO dono (codigo_cliente, nome_cliente, data_atualizacao, data_cadastro, cpf, data_nascimento, idade, telefone, celular, cep, cidade, bairro, rua) VALUES ('{var_codigo}','{var_nome_cliente}','{var_data_atualizacao}', '{var_data_cadastro}', '{var_cpf}', '{var_nascimento}', '{var_idade}', '{var_telefone}', '{var_celular}', '{var_cep}', '{var_cidade}', '{var_bairro}', '{var_rua}')")
        cursor.execute("commit")
        messagebox.showinfo("Mensagem", "Cadastro Realizado com Sucesso")
        conectar.close()


# Função para excluir
def excluir():
    if (txt_codigo.get() == ""):
        messagebox.showinfo("ALERTA", "Digite o código para deletar")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM dono WHERE codigo_cliente='" + txt_codigo.get() + "'")
        cursor.execute("commit")
        messagebox.showinfo("Mensagem", "Informação Excluída com Sucesso")
        conectar.close()


def atualizar():
    var_codigo = txt_codigo.get()
    var_nome_cliente = txt_nome_cliente.get()
    var_data_atualizacao = txt_data_atualizacao.get()
    var_data_cadastro = txt_data_cadastro.get()
    var_cpf = txt_cpf.get()
    var_nascimento = txt_nascimento.get()
    var_idade = txt_idade.get()
    var_telefone = txt_telefone.get()
    var_celular = txt_celular.get()
    var_cep = txt_cep.get()
    var_cidade = txt_cidade.get()
    var_bairro = txt_bairro.get()
    var_rua = txt_rua.get()

    if (var_nome_cliente == "" or var_cpf == ""):
        MessageBox.showinfo("ALERTA", "Campos obrigatórios vazios")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("UPDATE cliente SET nome_cliente = %s, data_atualizacao = %s, data_cadastro = %s, cpf = %s, nascimento = %s, idade = %s, telefone = %s, celular = %s, cep = %s, cidade = %s, bairro = %s, rua = %s WHERE codigo = %s",
                       (var_nome_cliente, var_data_atualizacao, var_data_cadastro, var_cpf, var_nascimento, var_idade, var_telefone, var_celular, var_cep, var_cidade, var_bairro, var_rua, var_codigo))
        conectar.commit()
        MessageBox.showinfo("Status", "Informação Atualizada com Sucesso")
        conectar.close()


#select para pesquisar
def Select():
    if (txt_codigo.get() == ""):
        messagebox.showinfo("ALERTA", "Por favor, digite o código.")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM pet WHERE codigo='" + txt_codigo.get() + "'")
        rows = cursor.fetchall()

        if len(rows) > 0:
            pet = rows[0]
            txt_nome_cliente.delete(0, END)
            txt_nome_cliente.insert(END, pet[1])
            txt_data_atualizacao.delete(0, END)
            txt_data_atualizacao.insert(END, pet[2])
            txt_data_cadastro.delete(0, END)
            txt_data_cadastro.insert(END, pet[3])
            txt_cpf.delete(0, END)
            txt_cpf.insert(END, pet[4])
            txt_nascimento.delete(0, END)
            txt_nascimento.insert(END, pet[5])
            txt_idade.delete(0, END)
            txt_idade.insert(END, pet[6])
            txt_telefone.delete(0, END)
            txt_telefone.insert(END, pet[7])
            txt_celular.delete(0, END)
            txt_celular.insert(END, pet[8])
            txt_cep.delete(0, END)
            txt_cep.insert(END, pet[9])
            txt_cidade.delete(0, END)
            txt_cidade.insert(END, pet[10])
            txt_bairro.delete(0, END)
            txt_bairro.insert(END, pet[11])
            txt_rua.delete(0, END)
            txt_rua.insert(END, pet[12])
        else:
            messagebox.showinfo("ALERTA", "Nenhum registro encontrado para o código informado.")
        
        conectar.close()


#armazenando imagens nas variaveis
foto_salvar = PhotoImage(file= r"imgs\salvar-arquivo.png")
foto_excluir = PhotoImage(file= r"imgs\lixeira.png")
foto_alterar = PhotoImage(file= r"imgs\editar.png")
foto_consultar = PhotoImage(file= r"imgs\lupa.png")
foto_sair = PhotoImage(file= r"imgs\excluir.png")

#criando botoes do crud
btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP, command=salvar)
btn_salvar.place(x=130, y=390)

btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP, command=excluir)
btn_excluir.place(x=210, y=390)

btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound=TOP, command=atualizar)
btn_alterar.place(x=290, y=390)

btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP, command=Select)
btn_consultar.place(x=370, y=390)

btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair_tela)
btn_sair.place(x=690, y=390)

#posicionamento de tela no centro da tela do computador
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))


tela.mainloop()