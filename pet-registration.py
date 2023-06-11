#deve fazer a instalação de PIL primeiro. Abrir cmd e digitar 'pip install Pillow'
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np

tela = Tk()

def sair_tela():
    tela.destroy()
    return

tela.title("Cadastro do pet")
tela.configure(background='#d3d3d3')
tela.geometry("800x500")
tela.resizable(False,False)
largura = 900
altura = 500

#foto padrao antes d upload
fotoOriginal = Image.open("imgs/profile-dog.png")
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
lbl_titulo = Label(tela, text="Cadastro do pet").place(x=400, y=10)

lbl_codigo = Label(tela, text="Codigo do pet", bg="#d3d3d3")
txt_codigo = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_codigo.place(x=200, y=50)
txt_codigo.place(x=200, y=70)

lbl_nome_pet = Label(tela, text="Nome do pet", bg="#d3d3d3")
txt_nome_pet = Entry(tela, width=50, borderwidth=1, fg="blue", bg="white")
lbl_nome_pet.place(x=350, y=50)
txt_nome_pet.place(x=350, y=70)

lbl_data_atualizacao = Label(tela, text="Data de atualização", bg="#d3d3d3")
txt_data_atualizacao = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_data_atualizacao.place(x=700, y=50)
txt_data_atualizacao.place(x=700, y=70)

lbl_data_cadastro = Label(tela, text="Data de cadastro", bg="#d3d3d3")
txt_data_cadastro = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_data_cadastro.place(x=700, y=100)
txt_data_cadastro.place(x=700, y=120)

lbl_nascimento = Label(tela, text="Data de nascimento", bg="#d3d3d3")
txt_nascimento = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_nascimento.place(x=200, y=100)
txt_nascimento.place(x=200, y=120)

lbl_idade = Label(tela, text="Idade", bg="#d3d3d3")
txt_idade = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_idade.place(x=350, y=100)
txt_idade.place(x=350, y=120)

#criando botao radio do sexo
lbl_idade = Label(tela, text="Sexo", bg="#d3d3d3").place(x=500, y=100)
var=StringVar()
var.set("m") #set determina que o radio começa com 'm' selecionado
#text = texto vizualizado, variable = guarda escolha em var, value é o valor daquele radio
rdb_btn_m = Radiobutton(tela, text="Masculino", variable=var, value="m", bg="#d3d3d3")
rdb_btn_f = Radiobutton(tela, text="Feminino", variable=var, value="f", bg="#d3d3d3")

rdb_btn_m.place(x=500, y=120)
rdb_btn_f.place(x=600, y=120)

#ComboBox da especie
list_especies = ["Gato", "Cachorro"]
lbl_especies = Label(tela, text="Especies", bg="#d3d3d3")
lbl_especies.place(x=200, y=150)
cb_especies = ttk.Combobox(tela, values=list_especies)
cb_especies.set("Cachorro")
cb_especies.place(x=200, y=170)

lbl_raca = Label(tela, text="Raça", bg="#d3d3d3")
txt_raca = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_raca.place(x=380, y=150)
txt_raca.place(x=380, y=170)

lbl_peso = Label(tela, text="Peso", bg="#d3d3d3")
txt_peso = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_peso.place(x=530, y=150)
txt_peso.place(x=530, y=170)

#campo de descriçao Text
lbl_desc = Label(tela, text="Descrição", bg="#d3d3d3")
txt_desc =Text(tela)
lbl_desc.place(x=200, y=200)
txt_desc.place(x=200, y=220, width=500, height=100)

#armazenando imagens nas variaveis
foto_salvar = PhotoImage(file= r"imgs\salvar-arquivo.png")
foto_excluir = PhotoImage(file= r"imgs\lixeira.png")
foto_alterar = PhotoImage(file= r"imgs\editar.png")
foto_consultar = PhotoImage(file= r"imgs\lupa.png")
foto_sair = PhotoImage(file= r"imgs\excluir.png")


#banco de dados

def salvar():
    var_codigo = txt_codigo.get()
    var_nome_pet =  txt_nome_pet.get()
    var_data_atualizacao = txt_data_atualizacao.get()
    var_data_cadastro = txt_data_cadastro.get()
    var_nascimento =  txt_nascimento.get()
    var_idade = txt_idade.get()
    var_raca = txt_raca.get()
    var_peso = txt_peso.get()
    var_descricao =  txt_desc.get("1.0", "end-1c")

    if(var_nome_pet == "" or var_raca == ""):
        MessageBox.showinfo("Erro", "Há campos nome pet e raça em branco")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute(f"INSERT INTO pet (codigo, nome_pet, nascimento, idade, raca, peso, descricao) VALUES ({var_codigo},'{var_nome_pet}','{var_nascimento}', '{var_idade}','{var_raca}', '{var_peso}','{var_descricao}')")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Cadastro Realizado com Sucesso")
        conectar.close()

#Botão para excluir
def excluir():
    if(txt_codigo.get() == ""):
        MessageBox.showinfo("ALERT", "Digite o código para deletar")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM pet WHERE codigo='"+txt_codigo.get()+"'")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Informação Excluída com Sucesso")
        conectar.close()


#Botao para atualizar
def atualizar():
    var_codigo = txt_codigo.get()
    var_nome_pet =  txt_nome_pet.get()
    var_data_atualizacao = txt_data_atualizacao.get()
    var_data_cadastro = txt_data_cadastro.get()
    var_nascimento =  txt_nascimento.get()
    var_idade = txt_idade.get()
    var_raca = txt_raca.get()
    var_peso = txt_peso.get()
    var_descricao = txt_desc.get("1.0", "end-1c")

    if (var_nome_pet == "" or var_raca == ""):
        MessageBox.showinfo("ALERT", "Campos obrigatórios vazios")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("UPDATE pet SET nome_pet = %s, data_atualizacao = %s, data_cadastro = %s, nascimento = %s, idade = %s, raca = %s, peso = %s, descricao = %s WHERE codigo = %s",
                       (var_nome_pet, var_data_atualizacao, var_data_cadastro, var_nascimento, var_idade, var_raca, var_peso, var_descricao, var_codigo))
        conectar.commit()
        MessageBox.showinfo("Status", "Informação Atualizada com Sucesso")
        conectar.close()
        

def Select():
    if txt_codigo.get() == "":
        MessageBox.showinfo("ALERTA", "Por favor, digite o código.")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM pet WHERE codigo='" + txt_codigo.get() + "'")
        rows = cursor.fetchall()

        if len(rows) > 0:
            pet = rows[0]
            txt_nome_pet.delete(0, END)
            txt_nome_pet.insert(END, pet[1])
            txt_data_atualizacao.delete(0, END)
            txt_data_atualizacao.insert(END, pet[2])
            txt_data_cadastro.delete(0, END)
            txt_data_cadastro.insert(END, pet[3])
            txt_nascimento.delete(0, END)
            txt_nascimento.insert(END, pet[4])
            txt_idade.delete(0, END)
            txt_idade.insert(END, pet[5])
            txt_raca.delete(0, END)
            txt_raca.insert(END, pet[6])
            txt_peso.delete(0, END)
            txt_peso.insert(END, pet[7])
            txt_desc.delete("1.0", END)
            txt_desc.insert(END, pet[8])
        else:
            MessageBox.showinfo("ALERTA", "Nenhum registro encontrado para o código informado.")
        
        conectar.close()


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