import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

ventanas = {}

# Función para mostrar la ventana deseada
def mostrar_ventana(nombre):
    for v in ventanas.values():
        v.withdraw()
        for widget in v.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_ismapped() and widget.winfo_width() == 150:
                widget.pack_forget()
    ventanas[nombre].deiconify()

# Función del menú hamburguesa
def Boton_hamburguesa(ventana):
    menu = tk.Frame(ventana, width=150, bg="#cccccc")
    tk.Button(menu, text="Perfil de usuario", command=lambda: mostrar_ventana("perfil de usuario")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Atención al usuario", command=lambda: mostrar_ventana("atencion al usuario")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Editor de auto", command=lambda: mostrar_ventana("editor de auto")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Diseño concluido", command=lambda: mostrar_ventana("diseño concluido")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Producción", command=lambda: mostrar_ventana("produccion")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Salida", command=lambda: mostrar_ventana("salida")).pack(anchor="w", pady=5, padx=10)

    def mostrar_ocultar():
        if menu.winfo_ismapped():
            menu.pack_forget()
        else:
            menu.pack(side="left", fill="y")

    boton = tk.Button(ventana, text="☰", command=mostrar_ocultar)
    boton.pack(anchor="nw", padx=5, pady=5)

# Función para crear fondo adaptable a la ventana
def agregar_fondo(ventana, ruta_imagen):
    ventana.update()
    ancho, alto = ventana.winfo_width(), ventana.winfo_height()
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((ancho, alto))
    foto = ImageTk.PhotoImage(imagen)
    fondo_label = tk.Label(ventana, image=foto)
    fondo_label.image = foto
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    return fondo_label

def main():
    # ------------------- Perfil de usuario -------------------
    perfil = tk.Tk()
    perfil.title("Perfil de usuario")
    perfil.geometry("650x500")
    agregar_fondo(perfil, r"E:\ProyectPython3BP\fondo.jpg")
    Boton_hamburguesa(perfil)

    contenido = tk.Frame(perfil, bg="", bd=0)
    contenido.pack(side="right", fill="both", expand=True)

    tk.Label(contenido, text="Bienvenido", font=("Arial", 10, "bold")).pack(pady=10)

    # Botones adicionales
    tk.Button(contenido, text="Login").pack(pady=5)
    tk.Button(contenido, text="Modificación de perfil").pack(pady=5)
    tk.Button(contenido, text="Modificar").pack(pady=5)
    tk.Button(contenido, text="Eliminar").pack(pady=5)

    # Campos de login dentro del perfil
    tk.Label(contenido, text="Tipo de usuario:").pack(pady=5)
    usuario_entry = tk.Entry(contenido, width=20)
    usuario_entry.pack(pady=5)

    tk.Label(contenido, text="Contraseña:").pack(pady=5)
    contrasena_entry = tk.Entry(contenido, width=20, show="*")
    contrasena_entry.pack(pady=5)

    mensaje_login = tk.Label(contenido, text="", fg="blue")
    mensaje_login.pack(pady=10)

    def verificar_login():
        usuario = usuario_entry.get().strip()
        contrasena = contrasena_entry.get().strip()
        if usuario == "Diana" and contrasena == "11425":
            mensaje_login.config(text=f"Bienvenida {usuario}.", fg="green")
        else:
            mensaje_login.config(text="Usuario o contraseña incorrectos.", fg="red")

    tk.Button(contenido, text="Aceptar", command=verificar_login).pack(pady=10)

    # Imagen ejemplo
    imagen2 = Image.open(r"E:\ProyectPython3BP\carro.jpg")
    imagen2 = imagen2.resize((200, 200))
    foto = ImageTk.PhotoImage(imagen2)
    etiqueta2 = tk.Label(contenido, image=foto)
    etiqueta2.image = foto
    etiqueta2.pack(pady=10)

    ventanas["perfil de usuario"] = perfil

    # ------------------- Atención al usuario -------------------
    atencion = tk.Toplevel(perfil)
    atencion.title("Atención al usuario")
    atencion.geometry("650x500")
    agregar_fondo(atencion, r"E:\ProyectPython3BP\fondo.jpg")
    Boton_hamburguesa(atencion)

    contenido_login = tk.Frame(atencion)
    contenido_login.pack(side="right", fill="both", expand=True)

    tk.Label(contenido_login, text="Tipo de usuario:").pack(pady=5)
    usuario_entry2 = tk.Entry(contenido_login, width=20)
    usuario_entry2.pack(pady=5)

    tk.Label(contenido_login, text="Contraseña:").pack(pady=5)
    contrasena_entry2 = tk.Entry(contenido_login, width=20, show="*")
    contrasena_entry2.pack(pady=5)

    tk.Button(contenido_login, text="Datos y logros de la empresa").pack(pady=5)
    tk.Button(contenido_login, text="Contacto").pack(pady=5)

    mensaje_login2 = tk.Label(contenido_login, text="", fg="blue")
    mensaje_login2.pack(pady=10)

    def verificar_login2():
        usuario = usuario_entry2.get().strip()
        contrasena = contrasena_entry2.get().strip()
        if usuario == "Diana" and contrasena == "11425":
            mensaje_login2.config(text=f"Bienvenida {usuario}.", fg="green")
        else:
            mensaje_login2.config(text="Usuario o contraseña incorrectos.", fg="red")

    tk.Button(contenido_login, text="Aceptar", command=verificar_login2).pack(pady=10)

    atencion.withdraw()
    ventanas["atencion al usuario"] = atencion

    # ------------------- Editor de auto -------------------
    editor = tk.Toplevel(perfil)
    editor.title("Editor de auto")
    editor.geometry("650x500")
    agregar_fondo(editor, r"E:\ProyectPython3BP\fondo.jpg")
    Boton_hamburguesa(editor)

    contenido_inicio = tk.Frame(editor)
    contenido_inicio.pack(side="right", fill="both", expand=True)

    tk.Button(contenido_inicio, text="Editor de piezas").pack(pady=5)
    tk.Button(contenido_inicio, text="Editor de logos").pack(pady=5)
    tk.Button(contenido_inicio, text="Software").pack(pady=5)
    tk.Button(contenido_inicio, text="Modificar").pack(pady=5)
    tk.Button(contenido_inicio, text="Eliminar").pack(pady=5)
    
    editor.withdraw()
    ventanas["editor de auto"] = editor

    # ------------------- Diseño concluido -------------------
    diseño = tk.Toplevel(perfil)
    diseño.title("Diseño concluido")
    diseño.geometry("650x500")
    agregar_fondo(diseño, r"E:\ProyectPython3BP\fondo.jpg")
    Boton_hamburguesa(diseño)

    contenido_contacto = tk.Frame(diseño)
    contenido_contacto.pack(side="right", fill="both", expand=True)

    tk.Button(contenido_contacto, text="Firma de contratos").pack(pady=5)
    tk.Button(contenido_contacto, text="Modificación de diseño").pack(pady=5)
    tk.Button(contenido_contacto, text="Historial de versiones").pack(pady=5)
    tk.Button(contenido_contacto, text="Modificar").pack(pady=5)
    tk.Button(contenido_contacto, text="Eliminar").pack(pady=5)

    diseño.withdraw()
    ventanas["diseño concluido"] = diseño

    # ------------------- Producción -------------------
    produccion = tk.Toplevel(perfil)
    produccion.title("Producción")
    produccion.geometry("650x500")
    agregar_fondo(produccion, r"E:\ProyectPython3BP\fondo.jpg")
    Boton_hamburguesa(produccion)

    contenido_registro = tk.Frame(produccion)
    contenido_registro.pack(side="right", fill="both", expand=True)

    tk.Button(contenido_registro, text="Documento de aceptación para producción").pack(pady=5)
    tk.Button(contenido_registro, text="Modificar").pack(pady=5)
    tk.Button(contenido_registro, text="Eliminar").pack(pady=5)

    produccion.withdraw()
    ventanas["produccion"] = produccion

    # ------------------- Salida -------------------
    salida = tk.Toplevel(perfil)
    salida.title("Salida")
    salida.geometry("650x500")
    agregar_fondo(salida, r"E:\ProyectPython3BP\fondo.jpg")
    Boton_hamburguesa(salida)

    contenido_salida = tk.Frame(salida)
    contenido_salida.pack(side="right", fill="both", expand=True)

    def mensaje_despedida():
        messagebox.showinfo("Despedida", "Gracias por visitarnos. ¡Hasta pronto!")
        perfil.destroy()

    tk.Label(contenido_salida, text="Hasta luego :)", font=("Arial", 12, "bold")).pack(pady=30)
    tk.Button(contenido_salida, text="Despedirse", command=mensaje_despedida).pack(pady=10)

    salida.withdraw()
    ventanas["salida"] = salida

    perfil.mainloop()

if __name__ == "__main__":
    main()
