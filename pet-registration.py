#deve fazer a instalação de PIL primeiro. Abrir cmd e digitar 'pip install Pillow'
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import subprocess
#PIL permite importar imgs externas
#ttk permite fazer ComboBox

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
def escolher_imagem(): #inicio da função
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                                                           ("Todos os arquivos", "*.*"))) #localização do arquivo e tipos a serem utilizados
    imagem_pil = Image.open(caminho_imagem) #abertura do arquivo atraves do PIL
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura/150
        nova_altura = int(altura/proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura)) #redimensionamento da imagem
    imagem_tk = ImageTk.PhotoImage(imagem_pil) #convertendo a imagem para formato compativel com o Tkinter
    lbl_imagem = Label(tela, image=imagem_tk) 
    lbl_imagem.image = imagem_tk #a imagem escolhida será armaznada em uma label
    lbl_imagem.place(x=50, y=50)

#botao chamando a função escolher_imagem
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=55, y=210)

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
btn_sair.place(x=690, y=390)

#posicionamento de tela no centro da tela do computador
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))


tela.mainloop()