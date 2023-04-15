from tkinter import *
from tkinter import ttk
import subprocess

tela = Tk()

tela.geometry("500x500")

#comboBox especies

list_especies = ["Gato", "Cachorro"]

lbl_especies = Label(tela, text="Especies")
lbl_especies.place(x=50, y=50)

cb_especies = ttk.Combobox(tela, values=list_especies)
cb_especies.set("Cachorro")
cb_especies.place(x=50, y=80)

#radio_especies

#criando botao radio da especie
lbl_especie = Label(tela, text="Espécie", bg="#d3d3d3").place(x=200, y=150)
var2=StringVar()
var2.set("c")
rdb_btn_c = Radiobutton(tela, text="Cachorro", variable=var2, value="c", bg="#d3d3d3")
rdb_btn_g = Radiobutton(tela, text="Gato", variable=var2, value="g", bg="#d3d3d3")
rdb_btn_c.place(x=200, y=170)
rdb_btn_g.place(x=290, y=170)

#campo de descriçao Text
Label(tela, text="Descrição").place(x=50, y=300)
descricao = Text(tela).place(x=50, y=330, width=300, height=100)

def abrir_tela_animais():
    subprocess.run(["python", "pet-registration.py"])

btn_botao = Button(tela, text="Redirecionar", command=abrir_tela_animais)
btn_botao.pack()

tela.mainloop()