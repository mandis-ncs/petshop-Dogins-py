from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np

tela = Tk()
tela.title("Cadastro do Cliente")
tela.configure(background='#d3d3d3')
tela.geometry("800x500")
tela.resizable(False,False)
largura = 900
altura = 500

fotoOriginal = Image.open("imgs/profile-owner.png")
fotoResize = fotoOriginal.resize((110, 150))
fotoPerfil = ImageTk.PhotoImage(fotoResize)
lbl_foto_Profile = Label(bg="#FFFFFF", image=fotoPerfil)
lbl_foto_Profile.place(x=50, y=50)

pasta_inicial = ""

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

def rotate_image():
    global rotated_image
    angle = 45
    rotated_image = cv.rotate(rotated_image, angle)
    show_image(rotated_image)

def show_image(image):
    image_pil = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    image_tk = ImageTk.PhotoImage(image_pil)
    lbl_imagem.configure(image=image_tk)
    lbl_imagem.image = image_tk

btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=55, y=210)

btn_rotate = Button(tela, text="Rotate", command=rotate_image)
btn_rotate.place(x=55, y=250)

lbl_imagem = Label(tela)
lbl_imagem.place(x=50, y=50)

tela.mainloop()
