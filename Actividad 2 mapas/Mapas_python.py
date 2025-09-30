import tkinter as tk

estudiantes = {}

def guardar_estudiante():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    edad = entrada_edad.get()
    telefono = entrada_telefono.get()
    correo = entrada_correo.get()
    asignatura = asignaturas.get()

    datos = f"nombre: {nombre} {apellido}, edad: {edad}, teléfono: {telefono}, asignatura: {asignatura}"

    estudiantes[correo] = datos

    entrada_nombre.delete(0, tk.END)
    entrada_apellido.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_telefono.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    asignaturas.set(asignatura_opciones[0])

def listar_estudiantes():
      texto_completo = "\n".join(estudiantes.values())
      panel_listado.config(text=texto_completo)

ventana = tk.Tk()
ventana.title("formulario estudiantes")
ventana.geometry("650x450")

tk.Label(ventana, text="nombre").place(x=30, y=30)
tk.Label(ventana, text="apellido").place(x=30, y=70)
tk.Label(ventana, text="edad").place(x=30, y=110)
tk.Label(ventana, text="teléfono").place(x=30, y=150)
tk.Label(ventana, text="correo").place(x=30, y=190)
tk.Label(ventana, text="asignatura").place(x=30, y=230)

entrada_nombre = tk.Entry(ventana, width=30)
entrada_apellido = tk.Entry(ventana, width=30)
entrada_edad = tk.Entry(ventana, width=30)
entrada_telefono = tk.Entry(ventana, width=30)
entrada_correo = tk.Entry(ventana, width=30)

entrada_nombre.place(x=150, y=30)
entrada_apellido.place(x=150, y=70)
entrada_edad.place(x=150, y=110)
entrada_telefono.place(x=150, y=150)
entrada_correo.place(x=150, y=190)

asignatura_opciones = ["matemáticas", "español", "inglés", "física"]
asignaturas = tk.StringVar(ventana)
asignaturas.set(asignatura_opciones[0])

menu_asignaturas = tk.OptionMenu(ventana, asignaturas, *asignatura_opciones)
menu_asignaturas.place(x=150, y=230)

tk.Button(ventana, text="guardar", command=guardar_estudiante).place(x=150, y=270)
tk.Button(ventana, text="listar", command=listar_estudiantes).place(x=220, y=270)

panel_listado = tk.Label(ventana, text="", justify="left", width=70, height=10)
panel_listado.place(x=30, y=310)

ventana.mainloop()
