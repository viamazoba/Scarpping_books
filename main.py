from webScraping_book import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
import tkinter as tk


if __name__ == "__main__":

    # --------------------------- Definiéndo los colores del UI ------------------------
    white = '#F3F2ED'
    #white = '#f6efe9'
    backgroudCombobox = '#e5e1e0'
    colorTexto="#29292b"
    colorAceptar="#00B38B" # #00a44d #00B38B #007D59
    colorCancelar="#A52636" # #d92037
    colorAceptarClick="#007D59"
    colorCancelarClick= "#701722"
    #styleTexto=("Draft A Extra Bold",11)
    styleTexto_h1=("Arial",14, 'bold')
    styleTexto_h2=("Arial",12, 'bold')
    styleTexto_h3=("Arial",10, 'bold')
    styleTexto_especial=("Arial",11, 'bold')

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


    # ------------------------------------------ A continuación se definen las variables utilizadas dentro de la interfaz gráfica ---------------------------------
    VarCategory=StringVar()
    VarDescription= StringVar(value= 'No')
    VarEncargo= StringVar()
    VarEncargo.set("10010019030") # Por defecto se deja con el número de cuenta de Coninsa
    VarTipoPago= StringVar()
    VarConceptoContable= StringVar()


    
    # ------------------------------------------- Creación del Frame ----------------------------------------------------------------------------------------------

    myframe= Frame(root,width=500, height=600, bg= white) # Frame de la aplicación
    myframe.pack()

    
    #------------------------------------------ Estilo personalizado para el comboBox -------------------------------------------------------------------------------
    
    style = ttk.Style()
    #style.configure('Custom.TCombobox', fieldbackground= 'red')
    style.configure('Custom.TCombobox', fieldbackground=backgroudCombobox, padding=(10, 5, 10, 5), height=3, arrowcolor=colorTexto)

    style.map('TCombobox', fieldbackground=[('readonly', backgroudCombobox)])

    labelNegocio= Label(myframe, text="InfoBooks",bg= white, font= styleTexto_h1, fg=colorTexto)
    labelNegocio.place(x=195,y=20) # Posicionándo label 


    separadorElementos= ttk.Separator(myframe,name="separador", orient="horizontal") # Separador del logo con los campos a ingresar
    separadorElementos.place(relx=0.08, rely=0.15,relheight=0.01, relwidth=0.85) # rely=0.554


    labelCategoria= Label(myframe, text="Choose a category:",bg= white, font= styleTexto_h2, fg=colorTexto)
    labelCategoria.place(x=70,y=75) # Posicionándo label 


    optionsTipoPago=["Transferencia Electronica", "Cheque gerencia - Recoger en oficina banco",
                 "Traslado entre encargos", "Traslado entre cuenta y encargo",
                 "Efectivo - Recoger en oficina banco","Cheque - Recoger en Alianza"]

    comboboxCategoria= ttk.Combobox(myframe,values=optionsTipoPago, state="readonly", textvariable=VarCategory, style='Custom.TCombobox') # state= disabled para bloquear campo, state="readonly" para que el campo no sea editable (no se pueda escribir en el)
    comboboxCategoria.config(width=23,height=30, font= styleTexto_h3)
    comboboxCategoria.current(0) # Poner elemento por default
    #tipoDePago.configure()

    # Cambiar el color de fondo del elemento seleccionado
    def on_select(event):
        comboboxCategoria.configure(style='Custom.TCombobox')
        comboboxCategoria.selection_clear()

    comboboxCategoria.bind('<<ComboboxSelected>>', on_select)
    comboboxCategoria.place(x=265, y=75)

    
    # ------------------------- Cantidad de elementos encontrados ---------------------------------------------------------------------------------

    labelnumberBooks= Label(myframe, text="number of category's books:",bg= white, font= styleTexto_especial, fg=colorTexto)
    labelnumberBooks.place(x=70,y=120) # Posicionándo label

    labelnumberBooks2= Label(myframe, text="1000",bg= '#fefffe', font= styleTexto_especial, fg=colorTexto)
    labelnumberBooks2.place(x=320,y=122) # Posicionándo label  
    
    
    
    # --------------------- Descripción del libro -----------------------------------------------------------

    labelDescription= Label(myframe, text="Download description?:",bg= white, font= styleTexto_h2, fg=colorTexto)
    labelDescription.place(x=70,y=170) # Posicionándo label 
    
    descriptionOpcionOne = Radiobutton(myframe, text="Yes", variable=VarDescription, value="Yes", background= white, font= styleTexto_h3, highlightthickness=0)
    descriptionOpcionOne.place(x=300, y=172)
    descriptionOpcionTwo = Radiobutton(myframe, text="No", variable=VarDescription, value="No", background= white, font= styleTexto_h3, highlightthickness= 0)
    descriptionOpcionTwo.place(x=350, y=172)



    root.mainloop() # Fin de la ventana