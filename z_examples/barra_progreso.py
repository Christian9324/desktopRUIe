import tkinter as tk
from tkinter import ttk
import time

def comenzar_progreso():
    progreso.start(10)  # Inicia la barra de progreso con una actualización cada 10 milisegundos
    for i in range(101):
        barra_progreso["value"] = i  # Actualiza el valor de la barra de progreso
        etiqueta_estado.config(text=f"Cargando... {i}%")
        ventana.update_idletasks()  # Actualiza la ventana para mostrar el progreso
        time.sleep(0.1)  # Simula una tarea de carga

    progreso.stop()  # Detiene la barra de progreso al llegar al 100%
    etiqueta_estado.config(text="Carga completa")

ventana = tk.Tk()
ventana.title("Ejemplo de Barra de Progreso")

etiqueta_estado = tk.Label(ventana, text="")
etiqueta_estado.pack(pady=10)

barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate")
barra_progreso.pack(pady=20)

boton_iniciar = tk.Button(ventana, text="Iniciar carga", command=comenzar_progreso)
boton_iniciar.pack(pady=10)

progreso = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="indeterminate")
progreso.pack(pady=20)

ventana.mainloop()