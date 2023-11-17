import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from res.theme.Colors import verde, rojo, marron, rojo_oscuro
import res.theme.Strings as textos
import time
import requests
import json
from types import SimpleNamespace
import res.api.config as api
import res.db.models
from res.db.models import Usuario

from res.usercases import getAllPaisesUC, getAllFuerzaUC, getAllMunicipiosUC, getAllPuntosIUC, verifyUser


def load_frame1():

    def refresh_cont(j):
        barra_progreso["value"] = j  # Actualiza el valor de la barra de progreso
        etiqueta_estado.config(text=f"Cargando... {j}%")
        frame1.update_idletasks()  # Actualiza la ventana para mostrar el progreso

    frame1.tkraise()
    frame1.pack_propagate(False)

    root.overrideredirect(True)

    def comenzar_progreso():
        refresh_cont(10)
        getAllPaisesUC()

        refresh_cont(20)
        getAllMunicipiosUC()

        refresh_cont(30)
        getAllPuntosIUC()

        refresh_cont(40)
        getAllFuerzaUC()
        

    # Inicia la barra de progreso con una actualización cada 10 milisegundos
        for i in range(0, 101, 4):
            barra_progreso["value"] = i  # Actualiza el valor de la barra de progreso
            etiqueta_estado.config(text=f"Cargando... {i}%")
            frame1.update_idletasks()  # Actualiza la ventana para mostrar el progreso
            time.sleep(0.05)  # Simula una tarea de carga

        etiqueta_estado.config(text="Carga completa")
        load_frame2()

    tk.Label(
        frame1,
        text=textos.Splash_label1,
        bg=verde,
        fg="white",
        font=("Arial", 30)
    ).pack(pady=(10,25))

    tk.Label(
        frame1,
        text=textos.Splash_label2,
        bg=verde,
        fg="white",
        font=("Arial", 12)
    ).pack(pady=(0,0))

    tk.Label(
        frame1,
        text=textos.Splash_label3,
        bg=verde,
        fg="white",
        font=("Arial", 12)
    ).pack(pady=15)

    tk.Label(
        frame1,
        text=textos.Splash_label4,
        bg=verde,
        fg=marron,
        font=("Arial", 15)
    ).pack(pady=(10,25))

    imageINM = Image.open("res/drawable/inami.png")
    width_i, height_i = imageINM.size
    imageINM = imageINM.resize((width_i//3, height_i//3))
    logo = ImageTk.PhotoImage(imageINM)
    logo_widget = tk.Label(frame1, image=logo, background=verde)
    logo_widget.image = logo
    logo_widget.pack()

    tk.Label(
        frame1,
        text=textos.Splash_label5,
        bg=verde,
        fg="white",
        font=("Arial", 10)
    ).pack(pady=(20,0))

    etiqueta_estado = tk.Label(frame1, text="", bg=verde, fg=marron)
    etiqueta_estado.pack(pady=(10,0))

    barra_progreso = ttk.Progressbar(frame1, orient="horizontal", length=200, mode="determinate")
    barra_progreso.pack(pady=(0,10))

    comenzar_progreso()

def load_frame2():

    root.overrideredirect(False)
    frame2.tkraise()
    frame2.pack_propagate(False)

    root.title("Inicio de Sesión")

    def iniciar_sesion():
        usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()

        if verifyUser(Usuario(nickname=usuario, password=contraseña)):
            print("usuario correcto") 
            etiqueta_estado.config(text="Inicio de sesión Correcto")           
        else:
            etiqueta_estado.config(text="Inicio de sesión Fallido")


    etiqueta_usuario = tk.Label(frame2, text="Usuario:", bg=verde, fg="white", font=("Arial", 24))
    etiqueta_usuario.pack(pady=(100,0))

    entrada_usuario = tk.Entry(frame2, font=("Arial", 20))
    entrada_usuario.pack(pady=(0,50))

    etiqueta_contraseña = tk.Label(frame2, text="Contraseña:", bg=verde, fg="white", font=("Arial", 24))
    etiqueta_contraseña.pack()

    entrada_contraseña = tk.Entry(frame2, show="*", font=("Arial", 20))
    entrada_contraseña.pack()

    boton_iniciar_sesion = tk.Button(frame2, 
                                     text="Iniciar Sesión", font=("Arial", 20),
                                     fg="white", activeforeground=verde,
                                     bg=rojo, activebackground=rojo_oscuro,
                                     cursor="hand2",  
                                     command=iniciar_sesion)
    boton_iniciar_sesion.pack(pady=(100,50))

    etiqueta_estado = tk.Label(frame2, text="")
    etiqueta_estado.pack()

    etiqueta_info = tk.Label(frame2, text="")
    etiqueta_info.pack()

    print("iniciando ventana 2")

root = tk.Tk()
# titulo
root.title('Bienvenidos')
# ubicacion de la ventana
# root.eval("tk::PlaceWindow . center")
#quitar barra de navegacion
# root.overrideredirect(True)

x = int(root.winfo_screenwidth() * 0.25)
y = int(root.winfo_screenheight() * 0.05)
root.geometry(f"500x700+{x}+{y}" )

imagen = Image.open("res/drawable/logo.ico")  # Reemplaza con la ruta de tu imagen
imagen = imagen.resize((24, 24))  # Cambiar el tamaño si es necesario
icono = ImageTk.PhotoImage(imagen)
root.tk.call('wm', 'iconphoto', root._w, icono)

frame1 = tk.Frame(root, width=500, height=700, bg=verde)
frame2 = tk.Frame(root, width=500, height=700, bg=verde)
frame1.grid(row=0,column=0)
frame2.grid(row=0,column=0)


load_frame1()

#run app
root.mainloop()