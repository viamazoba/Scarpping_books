from webScraping_book import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
import tkinter as tk
from idlelib.tooltip import Hovertip
from webScraping_book import webScraping_book
import multiprocessing
import time


# --------- Se obtienen las categorias y la cantidad de líbros en cada una ------------------------

def start_info_numberOfBooks(urls, list_numBooks):
    pageToScrape = webScraping_book('http://books.toscrape.com/', True)
    pageToScrape.load_page()

    for url in urls:
        pageToScrape.openNewTab(url)
        list_numBooks.append(pageToScrape.obtain_results())
        pageToScrape.closeNewTab()

    pageToScrape.close_web()    


def start_info(categories,url_categories, category_books):
    #global categories, url_categories, category_books
    category_book = []
    pageToScrape = webScraping_book('http://books.toscrape.com/', True)
    pageToScrape.load_page()


    category , url_category = pageToScrape.obtain_genres()
    categories.extend(category) # No debes reemplazar la lista creada con multiprocessing
    url_categories.extend(url_category)

    pageToScrape.close_web()
    
    manager = multiprocessing.Manager()
    first_part = manager.list()
    second_part = manager.list()
    third_part = manager.list()
    fourth_part = manager.list()

    process_list = []

    process_0 = multiprocessing.Process(target= start_info_numberOfBooks, args=(url_categories[0:10], first_part,))
    process_list.append(process_0)
    process_1 = multiprocessing.Process(target= start_info_numberOfBooks, args=(url_categories[10:20], second_part,))
    process_list.append(process_1)
    process_2 = multiprocessing.Process(target= start_info_numberOfBooks, args=(url_categories[20:30], third_part,))
    process_list.append(process_2)
    process_3 = multiprocessing.Process(target= start_info_numberOfBooks, args=(url_categories[30:], fourth_part,))
    process_list.append(process_3)

    for process in process_list:
        process.start()
    
    for process in process_list:
        process.join()


    first_part = list(first_part)
    second_part = list(second_part)
    third_part = list(third_part)
    fourth_part = list(fourth_part)

    category_books.extend(first_part + second_part + third_part+ fourth_part)






def dowload_information(category, Dictionary_url, watch_process, bool_description):

    # definir variable para descargar descripción
    messagebox.showinfo(title='Information',message='The download process will begin, and upon completion, an alert message will be displayed.')

    no_watch = True
    if watch_process == 1:
        no_watch = False

    
    pageBooks = webScraping_book('http://books.toscrape.com/', no_watch)
    pageBooks.load_page()
    pageBooks.openNewTab(Dictionary_url[category])
    repeatProcess = True


    while repeatProcess:
        pageBooks.obtain_info_books(bool_description)
        repeatProcess = pageBooks.next_page()
        if  not repeatProcess:
            break;

    pageBooks.closeNewTab()
    pageBooks.close_web()

    create_file(pageBooks._titles, pageBooks._prices, pageBooks._stars, pageBooks._states, pageBooks._description)
    messagebox.showinfo('Information','The download process has been successfully completed, and the information has been recorded in info_books.txt.')


def create_file(titles, prices, stars, states, description):

    with open('info_books.txt', 'w') as file:

        if description:
            line = 'titles|prices|stars|states|description' + '\n'
        else:
            line = 'titles|prices|stars|states' + '\n'
        

        for position in range(0, len(titles)):
            if description:
                line += titles[position]+'|' + prices[position] +'|'+ stars[position]+'|' + states[position]+'|' + description[position] + '\n'
            else:

                line += titles[position]+'|' + prices[position] +'|'+ stars[position]+'|' + states[position] + '\n'
            
        file.write(line)



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
    dark_blue = '#456990'
    #styleTexto=("Draft A Extra Bold",11)
    styleTexto_h1=("Arial",14, 'bold')
    styleTexto_h2=("Arial",12, 'bold')
    styleTexto_h3=("Arial",10, 'bold')
    styleTexto_especial=("Arial",11, 'bold')

    
    # ----------------------------------------------------------- Barra inicial de carga información --------------------------------------------------

    def load_bar():

        start_time = time.time()

        window = tk.Tk()
        window.title("Collecting information")
        window.resizable(0,0) # Para bloquear dimensiones

        # Dimensiones del frame
        w = 400
        h = 200

        # Dimensiones de la pantalla
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # root.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location
        window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        window.config(background= white)


        # Se crea label para la ventana de actualización
        update_text = Label(window, text="Collecting initial information for the \nsystem, please wait 13 seconds.",bg= white, font= styleTexto_especial, fg=colorTexto)
        update_text.place(x = 30, y = 50)

        style = ttk.Style()
        style.configure("red.Horizontal.TProgressbar", foreground = dark_blue, troughcolor = '#e5e1e0')

        # Crear barra de progreso
        progress_bar = ttk.Progressbar(window, style= "red.Horizontal.TProgressbar",orient="horizontal", length=250, mode="indeterminate")
        progress_bar.place(x=78, y= 120)
        progress_bar.start(17)

        
        def close_window():
            window.destroy()

        
        def on_closing():
            pass
        
        def update_time():
            end_time = time.time()
            time_donwload = int(13-(end_time-start_time))
            message = "Collecting initial information for the \nsystem, please wait {} seconds.".format(time_donwload)
            update_text.config(text= message)

            window.after(1000, update_time)


        window.after(13000, close_window)
        window.after(1000, update_time)
        window.protocol("WM_DELETE_WINDOW", on_closing)

        window.mainloop()


        
    manager = multiprocessing.Manager()
    categories = manager.list()
    url_categories = manager.list()
    category_books = manager.list()

    p2 = multiprocessing.Process(target=load_bar)
    p1 = multiprocessing.Process(target=start_info, args=(categories,url_categories, category_books,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    

    categories = list(categories)
    url_categories = list(url_categories)
    category_books = list(category_books)

    categories_dictionary = dict(zip(categories,category_books))
    categoriesDictionary_url = dict(zip(categories, url_categories))

        
    # -------------------------------- Ventana principal para la descarga de la información ------------------------------------------------------------
    root= Tk() # Inicio de la ventana
    root.title("Book Scrapping") # Título de la ventana
    root.resizable(0,0) # Para bloquear dimensiones

    # Se establece la configuración de los dialogos informativos
    root.option_add('*Dialog.msg.font', 'Airal 10 bold')
    # Dimensiones del frame
    w = 500
    h = 300

    # Dimensiones de la pantalla
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


    # ------------------------------------------ A continuación se definen las variables utilizadas dentro de la interfaz gráfica ---------------------------------
    VarCategory=StringVar()
    VarDescription= BooleanVar(value= False)
    VarNumBooks = StringVar(value= category_books[0])
    VarEncargo= StringVar()
    VarEncargo.set("10010019030") # Por defecto se deja con el número de cuenta de Coninsa
    VarCheckButton= IntVar(value= 0)
    VarDownloadAll = IntVar(value= 0)
    VarWatchProcess = IntVar(value= 0)

    VarConceptoContable= StringVar()


    
    # ------------------------------------------- Creación del Frame ----------------------------------------------------------------------------------------------

    myframe= Frame(root,width=500, height=600, bg= white) # Frame de la aplicación
    myframe.pack()

    def instruction():
        # Crear una instancia de Toplevel()
        window = tk.Toplevel(bg= white)
        anchor = 410
        heigth = 330
        w = window.winfo_screenwidth()
        h = window.winfo_screenheight()
        x = (w/2) - (anchor/2)
        y = (h/2) - (heigth/2)

        window.geometry("%dx%d+%d+%d" % (anchor, heigth, x, y))
        window.title("Readme")

        # Crear una etiqueta con un mensaje
        message = """This application is used to download 
    information from books that are    
    on the website books.toscrape.com,
    where the title, rating, availability, 
    and price of books from the chosen 
    category will be downloaded, and the 
    option to download their respective 
    description is also given.
        \nIn the advanced options, it is 
    possible to download all the books 
    on the website,and the option 
    to view the entire download 
    process can be set.
        \nThe output of this application 
    is an xlsx file with the 
    obtained information."""
        label = tk.Label(window, text=message, justify= 'center', font= styleTexto_h3, bg= white)
        label.pack(pady=15)

        # Crear un botón para cerrar la ventana
        button = tk.Button(window, text="Close", command=window.destroy, font= styleTexto_h3, bg= '#456990', fg= white, width= 10, activebackground='#114b5f', activeforeground= white)
        button.pack()

    def info():
        pass

    menubar = tk.Menu(root)
    menubar.add_command(label="Instructions", command=instruction, font= styleTexto_h3)
    menubar.add_command(label="About", command=info , font= styleTexto_h3)

    root.config(menu = menubar)
    
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


    comboboxCategoria= ttk.Combobox(myframe,values=categories, state="readonly", textvariable=VarCategory, style='Custom.TCombobox') # state= disabled para bloquear campo, state="readonly" para que el campo no sea editable (no se pueda escribir en el)
    comboboxCategoria.config(width=23,height=30, font= styleTexto_h3)
    comboboxCategoria.current(0) # Poner elemento por default
    #tipoDePago.configure()

    # Cambiar el color de fondo del elemento seleccionado y varias dinámicamente el valor del label referente a la cantidad de libros en la categoría
    def on_select(event):
        comboboxCategoria.configure(style='Custom.TCombobox')
        comboboxCategoria.selection_clear()

        selected_option = comboboxCategoria.get()
        VarNumBooks.set(categories_dictionary[selected_option])

        labelnumberBooks2.config(text= VarNumBooks.get())


    comboboxCategoria.bind('<<ComboboxSelected>>', on_select)
    comboboxCategoria.place(x=265, y=75)

    
    # ------------------------- Cantidad de elementos encontrados ---------------------------------------------------------------------------------

    labelnumberBooks= Label(myframe, text="found books:",bg= white, font= styleTexto_especial, fg=colorTexto)
    labelnumberBooks.place(x=140,y=110) # Posicionándo label

    labelnumberBooks2= Label(myframe, text=VarNumBooks.get() ,bg= '#fefffe', font= styleTexto_especial, fg=colorTexto)
    labelnumberBooks2.place(x=265,y=112) # Posicionándo label  
    
    
    
    # --------------------- Descripción del libro -----------------------------------------------------------

    labelDescription= Label(myframe, text="Download description?:",bg= white, font= styleTexto_especial, fg=colorTexto)
    labelDescription.place(x=48,y=140) # Posicionándo label 
    
    descriptionOpcionOne = Radiobutton(myframe, text="Yes", variable=VarDescription, value=True, background= white, font= styleTexto_h3, highlightthickness=0)
    descriptionOpcionOne.place(x=260, y=142)
    descriptionOpcionTwo = Radiobutton(myframe, text="No", variable=VarDescription, value=False, background= white, font= styleTexto_h3, highlightthickness= 0)
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
            h1 = 300
            root.geometry("%dx%d+%d+%d" % (w, h1, int(xActual), int(yActual)))

            camposIngresados= False
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
    myTipDownloadAll = Hovertip(downloadAll, 'Download the information \nfor all the books')

    watchProcess= Checkbutton(myframe,text="Watch process", font=styleTexto_h3, fg=colorTexto,variable=VarWatchProcess, highlightthickness=0, bg= white, compound="left",command=lambda: watchAllProcess())
    myTipWatchProcess = Hovertip(watchProcess, 'Select only if you want to watch how \nthe program download the information')


    # --------------------------------- botones de aceptar y cancelar -------------------------------------------------------------------------

    # def validacionVaribales():
    #     pass
    
    def cancelarOperacion():
        root.quit()
    
    botonAceptar= Button(myframe,text="Accept", width=15,font=styleTexto_h3, bg=colorAceptar, fg=white, bd=0.8, activebackground=colorAceptarClick, activeforeground= white, command=lambda:dowload_information(VarCategory.get(), categoriesDictionary_url,VarWatchProcess.get(), VarDescription.get()))

    botonAceptar.place(x=265,y=240)


    botonCancelar=Button(myframe,text="Cancel", width=15,font= styleTexto_h3, bg=colorCancelar, fg=white, bd=0.8, activebackground=colorCancelarClick, activeforeground=white, command=lambda:cancelarOperacion())

    botonCancelar.place(x=105,y=240)


    root.mainloop() # Fin de la ventana