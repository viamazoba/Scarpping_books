from webScraping_book import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog


if __name__ == "__main__":

    # --------------------------- Definiéndo los colores del UI ------------------------
    white = '#F3F2ED'
    colorTexto="#29292b"
    colorAceptar="#00B38B" # #00a44d #00B38B #007D59
    colorCancelar="#A52636" # #d92037
    colorAceptarClick="#007D59"
    colorCancelarClick= "#701722"
    #styleTexto=("Draft A Extra Bold",11)
    styleTexto_h1=("Arial",14, 'bold')
    styleTexto_h2=("Arial",12, 'bold')
    styleTexto_h3=("Arial",10, 'bold')

    root= Tk() # Inicio de la ventana
    root.title("Book Scrapping") # Título de la ventana
    root.resizable(0,0) # Para bloquear dimensiones

    # Dimensiones del frame
    w = 500
    h = 300

    # Dimensiones de la pantalla
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    #root.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


    myframe= Frame(root,width=500, height=600, bg= white) # Frame de la aplicación
    myframe.pack()

    labelNegocio= Label(myframe, text="Books at a click",bg= white, font= styleTexto_h1, fg=colorTexto)
    labelNegocio.place(x=160,y=20) # Posicionándo label 


    separadorElementos= ttk.Separator(myframe,name="separador", orient="horizontal") # Separador del logo con los campos a ingresar
    separadorElementos.place(relx=0.08, rely=0.15,relheight=0.01, relwidth=0.85) # rely=0.554







    root.mainloop() # Fin de la ventana