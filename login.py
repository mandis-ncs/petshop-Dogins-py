from tkinter import *
import subprocess
screen = Tk()

def abrir_menu():
    subprocess.run(["python", "menu.py"])

def sair_tela():
    screen.destroy()
    return

screen.title("Login do Funcionário")
screen.configure(background='#d3d3d3')
screen.geometry("470x200")
screen.resizable(False,False)
width = 470
heigh = 200

loginLabel = Label(screen, text="Sign In", 
                   background='#d3d3d3')
loginLabel.place(x=50, y=10)

userLabel = Label(screen, text="Username")
userLabel.place(x=50, y=50)

txtUser = Entry(screen, width=20)
txtUser.place(x=120, y=50)

passwordLabel = Label(screen, text="Password")
passwordLabel.place(x=50, y=100)

txtPassword = Entry(screen, width=20)
txtPassword.place(x=120, y=100)

EnterImage = PhotoImage(file= r"imgs\conecte-se.png")
CloseImage = PhotoImage(file= r"imgs\excluir.png")

btnUser = Button(screen, text="Login", image=EnterImage, compound=TOP, command=abrir_menu)
btnUser.place(x=270, y=50)

btnfechar = Button(screen, text="Sair", image=CloseImage, compound=TOP, command=sair_tela)
btnfechar.place(x=350, y=50)

screenWidth = screen.winfo_screenwidth()
screenHeight = screen.winfo_screenheight()

posx = screenWidth/2 - width/2
posy = screenHeight/2 - heigh/2

print(screenWidth, screenHeight)
screen.geometry("%dx%d+%d+%d" % (width, heigh, posx, posy))

screen.mainloop()