import tkinter as tk
usuarios = []
usuarios_texto = ""

def guardar():
    global usuarios_texto

    nombre = txtnombre.get()
    apellido = txtapellido.get()
    email = txtemail.get()
    clave = txtclave.get()

    usuario = [nombre, apellido, email, clave]
    usuarios.append(usuario)

    usuarios_texto += f"nombre: {nombre}, apellido: {apellido}, email: {email}, clave: {clave}\n"

    txtnombre.delete(0, tk.END)
    txtapellido.delete(0, tk.END)
    txtemail.delete(0, tk.END)
    txtclave.delete(0, tk.END)

def listar():
 panelListado.config(text=usuarios_texto)

ventana = tk.Tk()
ventana.title("formulario usuarios")
ventana.geometry("600x400")

inicio = tk.Label(ventana, text="formulario de registro", bg="blue", font=("Arial", 24))
inicio.place(x=70, y=20)

tk.Label(ventana, text="nombre").place(x=30, y=60)
tk.Label(ventana, text="apellido").place(x=30, y=100)
tk.Label(ventana, text="email").place(x=30, y=140)
tk.Label(ventana, text="clave").place(x=30, y=180)

txtnombre = tk.Entry(ventana, width=25)
txtapellido = tk.Entry(ventana, width=25)
txtemail = tk.Entry(ventana, width=25)
txtclave = tk.Entry(ventana, width=25)

txtnombre.place(x=130, y=60)
txtapellido.place(x=130, y=100)
txtemail.place(x=130, y=140)
txtclave.place(x=130, y=180)

tk.Button(ventana, text="guardar", command=guardar).place(x=130, y=220)
tk.Button(ventana, text="listar", command=listar).place(x=200, y=220)

panelListado = tk.Label(ventana, text="", bg="white", width=50)
panelListado.place(x=130, y=260)

ventana.mainloop()
