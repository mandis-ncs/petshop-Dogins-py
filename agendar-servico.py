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

tela.title("Agendamento do Serviço")
tela.configure(background='#d3d3d3')
tela.geometry("700x500")
tela.resizable(False,False)
largura = 700
altura = 500

#campos de cadastro
lbl_titulo = Label(tela, text="Agendar serviço").place(x=300, y=10)

lbl_codigo = Label(tela, text="Codigo do serviço", bg="#d3d3d3")
txt_codigo = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_codigo.place(x=50, y=50)
txt_codigo.place(x=50, y=70)

lbl_nome_servico = Label(tela, text="Nome do serviço", bg="#d3d3d3")
txt_nome_servico = Entry(tela, width=40, borderwidth=1, fg="blue", bg="white")
lbl_nome_servico.place(x=200, y=50)
txt_nome_servico.place(x=200, y=70)

lbl_data_agendamento = Label(tela, text="Agendar para dia", bg="#d3d3d3")
txt_data_agendamento = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_data_agendamento.place(x=500, y=50)
txt_data_agendamento.place(x=500, y=70)

lbl_data_cadastro = Label(tela, text="Data de hoje", bg="#d3d3d3")
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

lbl_codigo_pet = Label(tela, text="Codigo do pet", bg="#d3d3d3")
txt_codigo_pet = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_codigo_pet.place(x=50, y=280)
txt_codigo_pet.place(x=50, y=300)

lbl_nome_pet = Label(tela, text="Nome do pet", bg="#d3d3d3")
txt_nome_pet = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_nome_pet.place(x=200, y=280)
txt_nome_pet.place(x=200, y=300)

lbl_nome_dono = Label(tela, text="Nome do dono", bg="#d3d3d3")
txt_nome_dono = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
lbl_nome_dono.place(x=350, y=280)
txt_nome_dono.place(x=350, y=300)


# Função para salvar
def salvar():
    var_codigo = txt_codigo.get()
    var_nome_servico = txt_nome_servico.get()
    var_data_agendamento = txt_data_agendamento.get()
    var_data_cadastro = txt_data_cadastro.get()
    var_valor = txt_valor.get()
    var_duracao = txt_duracao.get()
    var_descricao = txt_desc.get("1.0", "end-1c")
    var_codigo_pet = txt_codigo_pet.get()
    var_nome_pet = txt_nome_pet.get()
    var_nome_dono = txt_nome_dono.get()

    if var_nome_pet == "" or var_nome_servico == "":
        MessageBox.showinfo("Erro", "Há campos em branco")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute(f"INSERT INTO agendar (codigo, nome_servico, data_agendamento, data_cadastro, valor, duracao, descricao, nome_pet, codigo_pet, nome_dono) VALUES ('{var_codigo}','{var_nome_servico}','{var_data_agendamento}', '{var_data_cadastro}', '{var_valor}', '{var_duracao}', '{var_descricao}', '{var_nome_pet}', '{var_codigo_pet}', '{var_nome_dono}')")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Cadastro Realizado com Sucesso")
        conectar.close()


# Função para excluir
def excluir():
    if txt_codigo.get() == "":
        MessageBox.showinfo("ALERTA", "Digite o código para deletar")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("DELETE FROM agendar WHERE codigo='" + txt_codigo.get() + "'")
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Informação Excluída com Sucesso")
        conectar.close()


# Função para atualizar
def atualizar():
    var_codigo = txt_codigo.get()
    var_nome_servico = txt_nome_servico.get()
    var_data_agendamento = txt_data_agendamento.get()
    var_data_cadastro = txt_data_cadastro.get()
    var_valor = txt_valor.get()
    var_duracao = txt_duracao.get()
    var_descricao = txt_desc.get("1.0", "end-1c")
    var_codigo_pet = txt_codigo_pet.get()
    var_nome_pet = txt_nome_pet.get()
    var_nome_dono = txt_nome_dono.get()

    if var_nome_pet == "" or var_nome_servico == "":
        MessageBox.showinfo("ALERTA", "Campos obrigatórios vazios")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("UPDATE agendar SET nome_servico = %s, data_agendamento = %s, data_cadastro = %s, valor = %s, duracao = %s, descricao = %s, nome_pet = %s, codigo_pet = %s, nome_dono = %s WHERE codigo = %s",
                       (var_nome_servico, var_data_agendamento, var_data_cadastro, var_valor, var_duracao, var_descricao, var_nome_pet, var_codigo_pet, var_nome_dono, var_codigo))
        conectar.commit()
        MessageBox.showinfo("Status", "Informação Atualizada com Sucesso")
        conectar.close()


# Função para selecionar registros
def select():
    if txt_codigo.get() == "":
        MessageBox.showinfo("ALERTA", "Por favor, digite o código.")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="dogins")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM agendar WHERE codigo='" + txt_codigo.get() + "'")
        rows = cursor.fetchall()

        if len(rows) > 0:
            agendamento = rows[0]
            txt_nome_servico.delete(0, END)
            txt_nome_servico.insert(END, agendamento[1])
            txt_data_agendamento.delete(0, END)
            txt_data_agendamento.insert(END, agendamento[2])
            txt_data_cadastro.delete(0, END)
            txt_data_cadastro.insert(END, agendamento[3])
            txt_valor.delete(0, END)
            txt_valor.insert(END, agendamento[4])
            txt_duracao.delete(0, END)
            txt_duracao.insert(END, agendamento[5])
            txt_desc.delete("1.0", END)
            txt_desc.insert(END, agendamento[6])
            txt_nome_pet.delete(0, END)
            txt_nome_pet.insert(END, agendamento[7])
            txt_codigo_pet.delete(0, END)
            txt_codigo_pet.insert(END, agendamento[8])
            txt_nome_dono.delete(0, END)
            txt_nome_dono.insert(END, agendamento[9])
        else:
            MessageBox.showinfo("ALERTA", "Nenhum registro encontrado para o código informado.")

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

btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP, command=select)
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