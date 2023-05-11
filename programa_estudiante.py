from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from tkinter import Toplevel

##funciones
def validar_numero_input(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False

def abrir_ventana_academico():
    global ventana_academico
    ventana_academico = Toplevel(ventana_principal)
    ventana_academico.title("Ventana Academico")
    ventana_academico.geometry("500x460")
    ventana_academico.resizable(0,0)
    
    #imagen de fondo
    label_fondo3 = Label(ventana_academico, image=imagen_tk)
    label_fondo3.place(x=0, y=0, relwidth=1, relheight=1)
    
    #variables 
    calculo = StringVar()
    algebra = StringVar()
    quimica = StringVar()
    programacion = StringVar()
    lenguaje = StringVar()
    fisica = StringVar()
    catedra = StringVar ()

    ##Frame 1
    frame_titulo2 = Frame(ventana_academico)
    frame_titulo2.config(bg="aquamarine2", width=480, height=60)
    frame_titulo2.place(x=10, y=10)

    lb_titulo2 = Label(frame_titulo2, text ="Estado Académico del Estudiante")
    lb_titulo2.config(font=("System", 18), bg="aquamarine2", fg="black")
    lb_titulo2.place(relx=0.5, rely=0.5, anchor=CENTER)

    ## Frame ejemplo notas
    frame_ejemplo = Frame(ventana_academico)
    frame_ejemplo.config(bg="aquamarine2", width=480, height=80)
    frame_ejemplo.place(x=10, y=80)

    lb_ejemplo = Label(frame_ejemplo, text ="Ejemplo de como debe digitar la nota:")
    lb_ejemplo.config(font=("System", 15), bg="aquamarine2", fg="black")
    lb_ejemplo.place(x=10, y=5)    

    lb_ejemplo1 = Label(frame_ejemplo, text ="Nota de XXXXXX: [10 - 50]")
    lb_ejemplo1.config(font=("System", 15), bg="aquamarine2", fg="black")
    lb_ejemplo1.place(x=130, y=36)    
    
    ## Frame datos
    frame_datos = Frame(ventana_academico)
    frame_datos.config(bg="aquamarine2", width=480, height=280)
    frame_datos.place(x=10, y=170)

    label_imagen2 = Label(frame_datos, image=imagen_2, width=150, height=260)
    label_imagen2.place(x=320, y=10)

    lb_calculo = Label(frame_datos, text ="Nota de cálculo:")
    lb_calculo.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_calculo.place(x=10, y=10)

    entry_calculo = Entry(frame_datos, textvariable=calculo, validate="key", validatecommand=vcmd)
    entry_calculo.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_calculo.place(x=230,y=10)

    lb_algebra = Label(frame_datos, text ="Nota de álgebra:")
    lb_algebra.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_algebra.place(x=10, y=40)

    entry_algebra = Entry(frame_datos, textvariable=algebra, validate="key", validatecommand=vcmd)
    entry_algebra.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_algebra.place(x=230,y=40)

    lb_quimica = Label(frame_datos, text ="Nota de química:")
    lb_quimica.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_quimica.place(x=10, y=70)

    entry_quimica = Entry(frame_datos, textvariable=quimica, validate="key", validatecommand=vcmd)
    entry_quimica.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_quimica.place(x=230,y=70)

    lb_programacion = Label(frame_datos, text ="Nota de programación:")
    lb_programacion.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_programacion.place(x=10, y=100)

    entry_programacion = Entry(frame_datos, textvariable=programacion, validate="key", validatecommand=vcmd)
    entry_programacion.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_programacion.place(x=230,y=100)

    lb_lenguaje = Label(frame_datos, text ="Nota de taller de lenguaje:")
    lb_lenguaje.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_lenguaje.place(x=10, y=130)

    entry_lenguaje = Entry(frame_datos, textvariable=lenguaje, validate="key", validatecommand=vcmd)
    entry_lenguaje.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_lenguaje.place(x=230,y=130)

    lb_fisica = Label(frame_datos, text ="Nota de cultura física:")
    lb_fisica.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_fisica.place(x=10, y=160)

    entry_fisica = Entry(frame_datos, textvariable=fisica, validate="key", validatecommand=vcmd)
    entry_fisica.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_fisica.place(x=230,y=160)

    lb_catedra = Label(frame_datos, text ="Nota de cátedra:")
    lb_catedra.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_catedra.place(x=10, y=190)

    entry_catedra = Entry(frame_datos, textvariable=catedra, validate="key", validatecommand=vcmd)
    entry_catedra.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_catedra.place(x=230,y=190)

    #botones
    btn_guardar_academico = Button(frame_datos, text="Guardar", command=lambda: calcular_promedio_academico(calculo, algebra, quimica, programacion, lenguaje, fisica, catedra))
    btn_guardar_academico.config(bg="white", fg="black", font=("System", 12), width=12)
    btn_guardar_academico.place(x=10, y=230)

    btn_borrar_academico = Button(frame_datos, text="Borrar datos", command=lambda: borrar_datos_academico(entry_calculo, entry_algebra, entry_quimica, entry_programacion, entry_lenguaje, entry_fisica, entry_catedra))
    btn_borrar_academico.config(bg="white", fg="black", font=("System", 12), width=12)
    btn_borrar_academico.place(x=170, y=230)
    
def calcular_promedio_academico(*args):
    global promedio
    notas = []
    for arg in args:
        nota = arg.get()
        if nota:
            nota = float(nota)
            if nota < 0 or nota > 50:
                messagebox.showerror("Error", "El valor de la nota debe estar entre 0 y 50.")
                return
            notas.append(nota)
        else:
            messagebox.showerror("Error", "No se ha ingresado un valor para una nota.")
            return
    if notas:
        promedio = sum(notas) / len(notas)
        messagebox.showinfo("Promedio", "Se ha calculado el promedio.")
        ventana_academico.destroy()
    else:
        promedio = None


def borrar_datos_academico(*args):
    for arg in args:
        arg.delete(0, END)

def abrir_ventana_medico():
    ventana_medico = Toplevel(ventana_principal)
    ventana_medico.title("Ventana Medico")
    ventana_medico.geometry("500x460")
    ventana_medico.resizable(0,0)

    #imagen de fondo
    label_fondo3 = Label(ventana_medico, image=imagen_tk)
    label_fondo3.place(x=0, y=0, relwidth=1, relheight=1)

    #variables 
    peso = StringVar()
    estatura = StringVar()
    sangre = ["O+", "O-", "AB+", "AB-", "A+", "A-", "B+", "B-"]

    ##Frame 1
    frame_titulo3 = Frame(ventana_medico)
    frame_titulo3.config(bg="aquamarine2", width=480, height=60)
    frame_titulo3.place(x=10, y=10)

    lb_titulo3 = Label(frame_titulo3, text ="Estado Médico del Estudiante")
    lb_titulo3.config(font=("System", 18), bg="aquamarine2", fg="black")
    lb_titulo3.place(relx=0.5, rely=0.5, anchor=CENTER)

    ## Frame ejemplo peso estatura
    frame_ejemplo2 = Frame(ventana_medico)
    frame_ejemplo2.config(bg="aquamarine2", width=480, height=80)
    frame_ejemplo2.place(x=10, y=80)

    lb_ejemplo2 = Label(frame_ejemplo2, text ="Ejemplo de como debe digitar los datos (en cm y en kg):")
    lb_ejemplo2.config(font=("System", 15), bg="aquamarine2", fg="black")
    lb_ejemplo2.place(x=10, y=5)    

    lb_ejemplo3 = Label(frame_ejemplo2, text ="Peso(kg):50")
    lb_ejemplo3.config(font=("System", 15), bg="aquamarine2", fg="black")
    lb_ejemplo3.place(x=90, y=36)    

    lb_ejemplo4 = Label(frame_ejemplo2, text ="Estatura(cm):175")
    lb_ejemplo4.config(font=("System", 15), bg="aquamarine2", fg="black")
    lb_ejemplo4.place(x=230, y=36)   

    ## Frame datos
    frame_datos2 = Frame(ventana_medico)
    frame_datos2.config(bg="aquamarine2", width=480, height=280)
    frame_datos2.place(x=10, y=170)

    label_imagen3 = Label(frame_datos2, image=imagen_3, width=150, height=260)
    label_imagen3.config(bg="aquamarine2")
    label_imagen3.place(x=320, y=10)

    lb_peso = Label(frame_datos2, text ="Peso:")
    lb_peso.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_peso.place(x=10, y=10)

    entry_peso = Entry(frame_datos2, textvariable=peso, validate="key", validatecommand=vcmd)
    entry_peso.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_peso.place(x=230,y=10)

    lb_algebra = Label(frame_datos2, text ="Estatura:")
    lb_algebra.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_algebra.place(x=10, y=60)

    entry_algebra = Entry(frame_datos2, textvariable=estatura, validate="key", validatecommand=vcmd)
    entry_algebra.config(bg="white", fg="black", font=("System", 12), width=8)
    entry_algebra.place(x=230,y=60)

    lb_sangre = Label(frame_datos2, text ="Tipo de sangre:")
    lb_sangre.config(bg="aquamarine2", fg="black", font=("System", 16))
    lb_sangre.place(x=10, y=110)

    cmb_sangre = ttk.Combobox(frame_datos2, textvariable=sangre, values=sangre, font=("Helvetica", 12), width=4)
    cmb_sangre.place(x=230, y=110)

    #botones
    btn_guardar_academico = Button(frame_datos2, text="Guardar", command=lambda: calcular_promedio_academico(calculo, algebra, quimica, programacion, lenguaje, fisica, catedra))
    btn_guardar_academico.config(bg="white", fg="black", font=("System", 12), width=12)
    btn_guardar_academico.place(x=10, y=200)

    btn_borrar_academico = Button(frame_datos2, text="Borrar datos", command=lambda: borrar_datos_academico(entry_algebra, entry_quimica, entry_programacion, entry_lenguaje, entry_fisica, entry_catedra))
    btn_borrar_academico.config(bg="white", fg="black", font=("System", 12), width=12)
    btn_borrar_academico.place(x=170, y=200)

def abrir_ventana_informe():
    ventana_informe = Toplevel(ventana_principal)
    ventana_informe.title("Ventana Medico")
    ventana_informe.geometry("500x460")
    ventana_informe.resizable(0,0)

    #imagen de fondo
    label_fondo3 = Label(ventana_medico, image=imagen_tk)
    label_fondo3.place(x=0, y=0, relwidth=1, relheight=1)

##ventana principal
ventana_principal = Tk()

ventana_principal.title("Estado del estudiante")
ventana_principal.geometry("500x600")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="deep sky blue")

#imagen de fondo
global imagen_tk
imagen = Image.open("img/494.jpg")
imagen = imagen.resize((500, 600), Image.ANTIALIAS)
imagen_tk = ImageTk.PhotoImage(imagen)
label_fondo = Label(ventana_principal, image=imagen_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#imagen ventana academico
global imagen_2
imagen2 = Image.open("img/2.jpg")
imagen2 = imagen2.resize((150, 260), Image.ANTIALIAS)
imagen_2 = ImageTk.PhotoImage(imagen2)

global imagen_3
imagen3 = Image.open("img/3.png")
imagen3 = imagen3.resize((150, 250), Image.ANTIALIAS)
imagen_3 = ImageTk.PhotoImage(imagen3)

##Frame 1
frame_titulo = Frame(ventana_principal)
frame_titulo.config(bg="aquamarine2", width=480, height=60)
frame_titulo.place(x=10, y=10)

lb_titulo = Label(frame_titulo, text ="Estado del Estudiante")
lb_titulo.config(bg="aquamarine2", fg="black", font=("System", 20))
lb_titulo.place(relx=0.5, rely=0.5, anchor=CENTER)

##Frame 2
frame_subtitulo1 = Frame(ventana_principal)
frame_subtitulo1.config(bg="aquamarine2", width=480, height=30)
frame_subtitulo1.place(x=10, y=80)

lb_subtitulo1 = Label(frame_subtitulo1, text ="Datos Basicos del Estudiante")
lb_subtitulo1.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_subtitulo1.place(relx=0.5, rely=0.5, anchor=CENTER)

##Frame datos basicos del estudiante
frame_datos_basicos = Frame(ventana_principal)
frame_datos_basicos.config(bg="aquamarine2", width=480, height=130)
frame_datos_basicos.place(x=10, y=120)

#variables
vcmd = (ventana_principal.register(validar_numero_input), '%P')
nombre = StringVar()
codigo = str(StringVar())
edad = str(StringVar())
programa = ["ING Sitemas", "ING Civil", "ING Electrica", "ING Electronica", "ING Quimica", "ING Industrial", "ING Mecanica", "Turismo"]
programa_elegido = StringVar()
sexo = ["Masculino", "Femenino", "Helicoptero Apache"]
sexo_elegido = StringVar()

#nombre
lb_nombre = Label(frame_datos_basicos, text ="Nombre del estudiante:")
lb_nombre.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_nombre.place(x=10, y=10)

entry_nombre = Entry(frame_datos_basicos, textvariable=nombre)
entry_nombre.config(bg="white", fg="black", font=("System", 12), width=27)
entry_nombre.focus_set()
entry_nombre.place(x=200,y=10)

#codigo
lb_codigo = Label(frame_datos_basicos, text ="Codigo:")
lb_codigo.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_codigo.place(x=10, y=50)

entry_codigo = Entry(frame_datos_basicos, textvariable=codigo, validate="key", validatecommand=vcmd)
entry_codigo.config(bg="white", fg="black", font=("System", 12), width=8)
entry_codigo.place(x=80,y=50)

#edad
lb_edad = Label(frame_datos_basicos, text ="Edad:")
lb_edad.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_edad.place(x=180, y=50)

entry_edad = Entry(frame_datos_basicos, textvariable=edad, validate="key", validatecommand=vcmd)
entry_edad.config(bg="white", fg="black", font=("System", 12), width=3)
entry_edad.place(x=240,y=50)

#sexo
lb_sexo = Label(frame_datos_basicos, text ="Sexo:")
lb_sexo.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_sexo.place(x=280, y=50)

cmb_sexo = ttk.Combobox(frame_datos_basicos, textvariable=sexo_elegido, values=sexo, font=("Helvetica", 12), width=12)
cmb_sexo.place(x=330, y=50)

#programa academico
lb_programa = Label(frame_datos_basicos, text ="Programa academico:")
lb_programa.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_programa.place(x=10, y=90)

cmb_programa = ttk.Combobox(frame_datos_basicos, textvariable=programa_elegido, values=programa, font=("Helvetica", 12))
cmb_programa.place(x=200, y=90)

#frame subtitulo 2
frame_subtitulo2 = Frame(ventana_principal)
frame_subtitulo2.config(bg="aquamarine2", width=480, height=30)
frame_subtitulo2.place(x=10, y=260)

lb_subtitulo2 = Label(frame_subtitulo2, text ="Datos Académicos y Médicos del Estudiante")
lb_subtitulo2.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_subtitulo2.place(relx=0.5, rely=0.5, anchor=CENTER)

#frame datos académicos y médicos
frame_datos_academicos_medicos = Frame(ventana_principal)
frame_datos_academicos_medicos.config(bg="aquamarine2", width=480, height=95)
frame_datos_academicos_medicos.place(x=10, y=300)

#entrada y botones Académico y Médico
lb_academico = Label(frame_datos_academicos_medicos, text ="Ingresar datos académicos:")
lb_academico.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_academico.place(x=10, y=10)

btn_academico = Button(frame_datos_academicos_medicos, text="Académico", command=abrir_ventana_academico)
btn_academico.config(bg="white", fg="black", font=("System", 12), width=12)
btn_academico.place(x=300, y=10)

lb_medico = Label(frame_datos_academicos_medicos, text ="Ingresar datos médicos:")
lb_medico.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_medico.place(x=10, y=50)

btn_medico = Button(frame_datos_academicos_medicos, text="Médico", command=abrir_ventana_medico)
btn_medico.config(bg="white", fg="black", font=("System", 12), width=12)
btn_medico.place(x=300, y=50)

#frame subtitulo informe
frame_subtitulo_informe = Frame(ventana_principal)
frame_subtitulo_informe.config(bg="aquamarine2", width=480, height=30)
frame_subtitulo_informe.place(x=10, y=405)

lb_subtitulo3 = Label(frame_subtitulo_informe, text ="Generar Informe")
lb_subtitulo3.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_subtitulo3.place(relx=0.5, rely=0.5, anchor=CENTER)

#frame y botones informe
frame_informe = Frame(ventana_principal)
frame_informe.config(bg="aquamarine2", width=480, height=55)
frame_informe.place(x=10, y=445)

lb_informe = Label(frame_informe, text ="Generar informe:")
lb_informe.config(bg="aquamarine2", fg="black", font=("System", 16))
lb_informe.place(x=10, y=10)

btn_academico = Button(frame_informe, text="Informe", command=abrir_ventana_academico)
btn_academico.config(bg="white", fg="black", font=("System", 12), width=12)
btn_academico.place(x=300, y=10)

ventana_principal.mainloop()
