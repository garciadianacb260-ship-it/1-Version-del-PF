import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox  

ventanas = {}

def mostrar_ventana(nombre):
    for v in ventanas.values():
        v.withdraw()
        for widget in v.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_ismapped() and widget.winfo_width() == 150:
                widget.pack_forget()
    ventanas[nombre].deiconify()

def Boton_hamburguesa(ventana):
    menu = tk.Frame(ventana, width=150)
    tk.Button(menu, text="Home", command=lambda: mostrar_ventana("principal")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Login", command=lambda: mostrar_ventana("login")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Inicio", command=lambda: mostrar_ventana("inicio")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Contacto", command=lambda: mostrar_ventana("contacto")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Registro", command=lambda: mostrar_ventana("registro")).pack(anchor="w", pady=5, padx=10)
    tk.Button(menu, text="Salida", command=lambda: mostrar_ventana("salida")).pack(anchor="w", pady=5, padx=10)  

    def mostrar_ocultar():
        if menu.winfo_ismapped():
            menu.pack_forget()
        else:
            menu.pack(side="left", fill="y")

    boton = tk.Button(ventana, text="☰", command=mostrar_ocultar)
    boton.pack(anchor="nw", padx=5, pady=5)

def encabezado_y_pie(ventana):
    encabezado = tk.Frame(ventana, height=60)
    encabezado.pack(fill="x")
    tk.Label(encabezado, text="🚗 LRMOTORDRIVE", font=("Arial", 16, "bold")).pack(pady=2)
    tk.Label(encabezado, text="Encuentra, elige y conduce al mejor precio").pack()
    pie = tk.Frame(ventana, height=40)
    pie.pack(side="bottom", fill="x")
    tk.Label(pie, text="©️2025 LRMOTORDRIVE. Todos los derechos reservados. 🌐 Facebook 📸 Instagram").pack(pady=5)

def main():
    principal = tk.Tk()
    principal.title("Ventana Principal")
    principal.geometry("600x450")
    encabezado_y_pie(principal)
    contenido = tk.Frame(principal)
    contenido.pack(side="right", fill="both", expand=True)
    Boton_hamburguesa(principal)
    tk.Label(contenido, text="Bienvenido", font=("Arial", 10, "bold")).pack(pady=10)
    ventanas["principal"] = principal
    imagen2 = Image.open(r"C:\Users\yovis\OneDrive\Escritorio\DOCS ACTUALES\3 de secundaria\DOCS ESCOLARES\carro.jpg")
    imagen2 = imagen2.resize((200, 200))
    foto = ImageTk.PhotoImage(imagen2)
    etiqueta2=tk.Label(contenido, image=foto)
    etiqueta2.image = foto
    etiqueta2.pack(pady=10)

    
    login = tk.Toplevel(principal)
    login.title("Login")
    login.geometry("400x500")
    encabezado_y_pie(login)
    contenido_login = tk.Frame(login)
    contenido_login.pack(side="right", fill="both", expand=True)
    Boton_hamburguesa(login)
    tk.Label(contenido_login, text="Tipo de usuario:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    usuario_entry = tk.Entry(contenido_login, width=20)
    usuario_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(contenido_login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    contrasena_entry = tk.Entry(contenido_login, width=20, show="*")
    contrasena_entry.grid(row=1, column=1, padx=10, pady=10)
    mensaje_login = tk.Label(contenido_login, text="", fg="blue")
    mensaje_login.grid(row=3, column=0, columnspan=2, pady=10)
    def verificar_login():
        usuario = usuario_entry.get().strip()
        contrasena = contrasena_entry.get().strip()
        if usuario == "Diana" and contrasena == "11425":
            mensaje_login.config(text=f"Bienvenida {usuario}.", fg="green")
        else:
            mensaje_login.config(text="Usuario o contraseña incorrectos.", fg="red")
    tk.Button(contenido_login, text="Aceptar", command=verificar_login).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(contenido_login, text="¿Se te olvido el correo?").grid(row=4, column=0, columnspan=2, pady=5)
    tk.Button(contenido_login, text="¿Se te olvido la contraseña?").grid(row=5, column=0, columnspan=2, pady=5)
    tk.Button(contenido_login, text="Cambiar perfil").grid(row=6, column=0, columnspan=2, pady=5)
    login.withdraw()
    ventanas["login"] = login

    inicio = tk.Toplevel(principal)
    inicio.title("Inicio")
    inicio.geometry("650x500")
    encabezado_y_pie(inicio)
    contenido_inicio = tk.Frame(inicio)
    contenido_inicio.pack(side="right", fill="both", expand=True)
    Boton_hamburguesa(inicio)
    tk.Label(contenido_inicio, text="Conoce más sobre nosotros:").pack(pady=5)
    tk.Label(contenido_inicio, text="Nuestra misión: Brindar a nuestros clientes una experiencia variada, de calidad y precios accesibles.").pack(pady=5)
    tk.Label(contenido_inicio, text="Nuestra visión: Ser una página reconocida por su atención personalizada y compromiso.").pack(pady=5)
    tk.Label(contenido_inicio, text="Correo electrónico: villamillucasluismanuel@gmail.com").pack(pady=5)
    tk.Label(contenido_inicio, text="Dirección: Av.117pte. 706, Zona Guadalupe Hidalgo").pack(pady=5)
    imagen1 = Image.open(r"C:\Users\yovis\OneDrive\Escritorio\DOCS ACTUALES\3 de secundaria\DOCS ESCOLARES\ubicacion.jpg")
    imagen1 = imagen1.resize((200, 200))
    foto = ImageTk.PhotoImage(imagen1)
    etiqueta1 = tk.Label(contenido_inicio, image=foto)
    etiqueta1.image = foto
    etiqueta1.pack(pady=10)
    tk.Label(contenido_inicio, text="Teléfono: 221-414-5015").pack(pady=5)
    tk.Label(contenido_inicio, text="Código Postal: 72480").pack(pady=5)
    inicio.withdraw()
    ventanas["inicio"] = inicio

    contacto = tk.Toplevel(principal)
    contacto.title("Contacto")
    contacto.geometry("500x550")
    encabezado_y_pie(contacto)
    contenido_contacto = tk.Frame(contacto)
    contenido_contacto.pack(side="right", fill="both", expand=True)
    Boton_hamburguesa(contacto)
    tk.Label(contenido_contacto, text="Nombre de Usuario").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    usuario_form_entry = tk.Entry(contenido_contacto, width=20)
    usuario_form_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(contenido_contacto, text="Comentario").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(contenido_contacto, width=50).grid(row=2, column=1, padx=10, pady=10)
    mensaje_contacto = tk.Label(contenido_contacto, text="", fg="blue")
    mensaje_contacto.grid(row=5, column=0, columnspan=2, pady=10)
    def enviar_contacto():
        nombre = usuario_form_entry.get().strip()
        if nombre:
            mensaje_contacto.config(text=f"Gracias {nombre}, tu comentario ha sido enviado.", fg="green")
        else:
            mensaje_contacto.config(text="Por favor, ingresa tu nombre de usuario.", fg="red")
    tk.Button(contenido_contacto, text="Aceptar", command=enviar_contacto).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Label(contenido_contacto, text="Soporte Técnico: soporte@empresa.com").grid(row=4, column=0, columnspan=2, pady=20)
    contacto.withdraw()
    ventanas["contacto"] = contacto

    registro = tk.Toplevel(principal)
    registro.title("Registro")
    registro.geometry("400x500")
    encabezado_y_pie(registro)
    contenido_registro = tk.Frame(registro)
    contenido_registro.pack(side="right", fill="both", expand=True)
    Boton_hamburguesa(registro)
    tk.Label(contenido_registro, text="Nombre de Usuario").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    nombre_entry = tk.Entry(contenido_registro, width=20)
    nombre_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(contenido_registro, text="Contraseña").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    contraseña_entry = tk.Entry(contenido_registro, width=20, show="*")
    contraseña_entry.grid(row=1, column=1, padx=10, pady=10)
    mensaje_label = tk.Label(contenido_registro, text="")
    mensaje_label.grid(row=3, column=0, columnspan=2, pady=10)
    def registrar():
        nombre = nombre_entry.get().strip()
        contra = contraseña_entry.get().strip()
        if nombre and contra:
            mensaje_label.config(text=f"Bienvenido {nombre}, tu registro fue exitoso.", fg="green")
        else:
            mensaje_label.config(text="Por favor, completa todos los campos.", fg="red")
    tk.Button(contenido_registro, text="Registrar", command=registrar).grid(row=2, column=0, columnspan=2, pady=20)
    registro.withdraw()
    ventanas["registro"] = registro

    
    salida = tk.Toplevel(principal)
    salida.title("Salida")
    salida.geometry("400x300")
    encabezado_y_pie(salida)
    contenido_salida = tk.Frame(salida)
    contenido_salida.pack(side="right", fill="both", expand=True)
    Boton_hamburguesa(salida)

    def mensaje_despedida():
        messagebox.showinfo("Despedida", "Gracias por visitarnos. ¡Hasta pronto!")
        principal.destroy() 

    tk.Label(contenido_salida, text="Hasta luego :)", font=("Arial", 12, "bold")).pack(pady=30)
    tk.Button(contenido_salida, text="Despedirse", command=mensaje_despedida).pack(pady=10)

    salida.withdraw()
    ventanas["salida"] = salida

    principal.mainloop()

if __name__ == "__main__":
    main()