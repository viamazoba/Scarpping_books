from webScraping_book import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
import tkinter as tk
from idlelib.tooltip import Hovertip


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
    VarCheckButton= IntVar(value= 0)
    VarDownloadAll = IntVar(value= 0)
    VarWatchProcess = IntVar(value= 0)

    VarConceptoContable= StringVar()


    
    # ------------------------------------------- Creación del Frame ----------------------------------------------------------------------------------------------

    myframe= Frame(root,width=500, height=600, bg= white) # Frame de la aplicación
    myframe.pack()

    
    #------------------------------------------ Estilo personalizado para el comboBox -------------------------------------------------------------------------------
    
    style = ttk.Style()
    #style.configure('Custom.TCombobox', fieldbackground= 'red')
    style.configure('Custom.TCombobox', fieldbackground=backgroudCombobox, padding=(8, 5, 8, 5), height=3, arrowcolor=colorTexto)

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

    labelnumberBooks= Label(myframe, text="found books:",bg= white, font= styleTexto_especial, fg=colorTexto)
    labelnumberBooks.place(x=140,y=110) # Posicionándo label

    labelnumberBooks2= Label(myframe, text="1000",bg= '#fefffe', font= styleTexto_especial, fg=colorTexto)
    labelnumberBooks2.place(x=265,y=112) # Posicionándo label  
    
    
    
    # --------------------- Descripción del libro -----------------------------------------------------------

    labelDescription= Label(myframe, text="Download description?:",bg= white, font= styleTexto_especial, fg=colorTexto)
    labelDescription.place(x=48,y=140) # Posicionándo label 
    
    descriptionOpcionOne = Radiobutton(myframe, text="Yes", variable=VarDescription, value="Yes", background= white, font= styleTexto_h3, highlightthickness=0)
    descriptionOpcionOne.place(x=260, y=142)
    descriptionOpcionTwo = Radiobutton(myframe, text="No", variable=VarDescription, value="No", background= white, font= styleTexto_h3, highlightthickness= 0)
    descriptionOpcionTwo.place(x=310, y=142)

    # ------------------------------ Opciones avanzadas -----------------------------------------------------------------------------

    
    def downloadAllBooks():

        if VarDownloadAll.get() == 1:
            descriptionOpcionOne.config(state= 'disabled')
            descriptionOpcionTwo.config(state= 'disabled')
        else:
            descriptionOpcionTwo.config(state= 'normal')
            descriptionOpcionOne.config(state= 'normal')


    def watchAllProcess():
        pass
    
    def advancedField():

        if VarCheckButton.get()==1:
            
            global xActual, yActual
            
            coordinates = root.geometry()
            xActual, yActual = coordinates.split("+")[1:]
            h1 = 350
            root.geometry("%dx%d+%d+%d" % (w, h1, int(xActual), int(yActual)))
            #myframe.config(height=700)
            botonAceptar.place(y=280)
            botonCancelar.place(y=280)

            downloadAll.place(x=270,y=225)
            watchProcess.place(x=150,y=225)

            separadorElementos.place(relx=0.08, rely=0.128,relheight=0.01, relwidth=0.85)
            #separadorElementosEnd.place(relx=0.17, rely=0.50,relheight=0.01, relwidth=0.65) # rely=0.554
            separadorElementosEnd.place(rely=0.725)
            

            #separadorElementos.place(rely=0.13)
        

        else:
            coordinates = root.geometry()
            #xActual2, yActual2 = coordinates.split("+")[1:]
            h1 = 300
            root.geometry("%dx%d+%d+%d" % (w, h1, int(xActual), int(yActual)))
            #h = 300
            camposIngresados= False
            #VarRubro.set("")
            #VarRecurso.set("")
            #VarArea.set("")
            root.geometry("%dx%d+%d+%d" % (w, h, x, y))
            myframe.config(height=600)
            botonAceptar.place(y=240)
            botonCancelar.place(y=240)

            separadorElementos.place(relx=0.08, rely=0.15,relheight=0.01, relwidth=0.85)
            separadorElementosEnd.place(relx=0.17, rely=0.74,relheight=0.01, relwidth=0.65) # rely=0.554
            
            
            
            watchProcess.place_forget()
            downloadAll.place_forget()
            
    
    
    advancedOption= Checkbutton(myframe,text="Advanced options", font=styleTexto_h3, fg=colorTexto,variable=VarCheckButton, highlightthickness=0, bg= white, command=lambda: advancedField())
    advancedOption.place(x=265,y=180)

    separadorElementosEnd= ttk.Separator(myframe,name="separadorEnd", orient="horizontal") # Separador del logo con los campos a ingresar
    separadorElementosEnd.place(relx=0.17, rely=0.74,relheight=0.01, relwidth=0.65) # rely=0.554


    downloadAll= Checkbutton(myframe,text="Download all", font=styleTexto_h3, fg=colorTexto,variable=VarDownloadAll, highlightthickness=0, bg= white, compound="left", command=lambda: downloadAllBooks())
    myTipDownloadAll = Hovertip(downloadAll, 'Download all books in the web site')

    watchProcess= Checkbutton(myframe,text="Watch process", font=styleTexto_h3, fg=colorTexto,variable=VarWatchProcess, highlightthickness=0, bg= white, compound="left",command=lambda: watchAllProcess())
    myTipWatchProcess = Hovertip(watchProcess, 'Select only if you want to watch how \nthe program download the information')


    # --------------------------------- botones de aceptar y cancelar -------------------------------------------------------------------------

    def validacionVaribales():
        pass
    
    def cancelarOperacion():
        root.quit()
    
    botonAceptar= Button(myframe,text="Accept", width=15,font=styleTexto_h3, bg=colorAceptar, fg=white, bd=0.8, activebackground=colorAceptarClick, activeforeground="#F3F2ED", command=lambda:validacionVaribales())

    botonAceptar.place(x=265,y=240)


    botonCancelar=Button(myframe,text="Cancel", width=15,font= styleTexto_h3, bg=colorCancelar, fg=white, bd=0.8, activebackground=colorCancelarClick, activeforeground="#F3F2ED", command=lambda:cancelarOperacion())

    botonCancelar.place(x=105,y=240)


    root.mainloop() # Fin de la ventana