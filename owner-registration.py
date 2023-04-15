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

lbl_bairro = Label(tela, text="Rua", bg="#d3d3d3")
txt_bairro = Entry(tela, width=50, borderwidth=1, fg="blue", bg="white")
lbl_bairro.place(x=200, y=250)
txt_bairro.place(x=200, y=270)

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