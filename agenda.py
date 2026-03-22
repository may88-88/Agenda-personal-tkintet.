import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# FRAME 1: LISTA DE EVENTOS
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# Crear tabla (TreeView)
tabla = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show="headings")

tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripcion", text="Descripción")

tabla.pack()


# FRAME 2: ENTRADAS
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Labels y entradas
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
entrada_fecha = tk.Entry(frame_entrada)
entrada_fecha.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entrada_descripcion = tk.Entry(frame_entrada)
entrada_descripcion.grid(row=2, column=1)


# FUNCIONES


# Función para agregar evento
def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Error", "Completa todos los campos")
    else:
        tabla.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos
        entrada_fecha.delete(0, tk.END)
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)


# Función para eliminar evento
def eliminar_evento():
    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning("Error", "Selecciona un evento")
    else:
        confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento?")
        if confirmar:
            tabla.delete(seleccion)


# FRAME 3: BOTONES
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
btn_salir.grid(row=0, column=2, padx=5)

# Ejecutar aplicación
ventana.mainloop()