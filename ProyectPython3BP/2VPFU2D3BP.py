import tkinter as tk
from PIL import Image, ImageTk

ventanas = {}
fondo_tk_dict = {}
image_path = r"E:\ProyectPython3BP\fondo.jpg"  # Fondo común

# -------------------- FUNCIONES GENERALES --------------------
def actualizar_fondo(ventana_obj, label_fondo, img_original_obj, event=None):
    img = img_original_obj.resize((ventana_obj.winfo_width(), ventana_obj.winfo_height()))
    foto = ImageTk.PhotoImage(img)
    label_fondo.config(image=foto)
    fondo_tk_dict[label_fondo] = foto

def mostrar_ventana(nombre):
    for v in ventanas.values():
        v.withdraw()
    ventanas[nombre].deiconify()

# -------------------- MENÚ HAMBURGUESA --------------------
def Boton_hamburguesa(ventana):
    menu = tk.Frame(ventana, width=150, bg="lightgray")
    menu_visible = [False]  # flag para mostrar/ocultar

    opciones = [("Home", "principal"), ("Login", "login"), ("Inicio", "inicio"),
                ("Contacto", "contacto"), ("Registro", "registro"), ("Salida", "salida")]
    botones_menu = []

    for texto, ventana_destino in opciones:
        btn = tk.Button(menu, text=texto, width=15,
                        command=lambda v=ventana_destino: mostrar_ventana(v),
                        relief="raised", bg="#f0f0f0", activebackground="#d9d9d9")
        btn.pack(pady=5, anchor="nw")
        botones_menu.append(btn)

    # Ocultar menú al inicio
    menu.place_forget()

    # Función para mostrar/ocultar menú
    def mostrar_ocultar():
        if menu_visible[0]:
            menu.place_forget()
            menu_visible[0] = False
        else:
            menu.place(x=10, y=60)  # debajo del botón hamburguesa
            menu_visible[0] = True

    # Botón hamburguesa fijo
    boton = tk.Button(ventana, text="☰", font=("Arial", 12, "bold"),
                      command=mostrar_ocultar,
                      relief="raised", bg="#f0f0f0", activebackground="#d9d9d9")
    boton.place(x=10, y=20)  # posición fija con pady ~20

# -------------------- CREACIÓN DE VENTANAS --------------------
def crear_principal():
    img_original = Image.open(image_path)

    # -------------------- VENTANA PRINCIPAL --------------------
    principal = tk.Tk()
    principal.title("Ventana Principal")
    principal.geometry("850x500")

    fondo_label = tk.Label(principal)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    principal.bind("<Configure>", lambda e: actualizar_fondo(principal, fondo_label, img_original))
    actualizar_fondo(principal, fondo_label, img_original)

    Boton_hamburguesa(principal)

    cont_principal = tk.Frame(principal, bg=None)
    cont_principal.pack(expand=True)
    tk.Label(cont_principal, text="Bienvenido", font=("Arial", 14, "bold"), fg="black", bg=None).pack(pady=10)
    ventanas["principal"] = principal

    # -------------------- LOGIN --------------------
    login = tk.Toplevel(principal)
    login.title("Login")
    login.geometry("850x500")

    fondo_label_login = tk.Label(login)
    fondo_label_login.place(x=0, y=0, relwidth=1, relheight=1)
    login.bind("<Configure>", lambda e: actualizar_fondo(login, fondo_label_login, img_original))
    actualizar_fondo(login, fondo_label_login, img_original)

    Boton_hamburguesa(login)

    contenido_login = tk.Frame(login, bg=None)
    contenido_login.pack(expand=True)

    # Login centrado y uniforme
    tk.Label(contenido_login, text="Tipo de usuario:", fg="black", bg=None).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    usuario_entry = tk.Entry(contenido_login, width=25)
    usuario_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(contenido_login, text="Contraseña:", fg="black", bg=None).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    contrasena_entry = tk.Entry(contenido_login, width=25, show="*")
    contrasena_entry.grid(row=1, column=1, padx=10, pady=10)

    mensaje_login = tk.Label(contenido_login, text="", fg="blue", bg=None)
    mensaje_login.grid(row=2, column=0, columnspan=2, pady=10)

    tk.Button(contenido_login, text="Aceptar", width=20, command=lambda: verificar_login(usuario_entry, contrasena_entry, mensaje_login)).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(contenido_login, text="¿Se te olvido el correo?", width=25).grid(row=4, column=0, columnspan=2, pady=5)
    tk.Button(contenido_login, text="¿Se te olvido la contraseña?", width=25).grid(row=5, column=0, columnspan=2, pady=5)
    tk.Button(contenido_login, text="Cambiar perfil", width=25).grid(row=6, column=0, columnspan=2, pady=5)

    login.withdraw()
    ventanas["login"] = login

    # -------------------- REGISTRO --------------------
    registro = tk.Toplevel(principal)
    registro.title("Registro")
    registro.geometry("850x500")

    fondo_label_registro = tk.Label(registro)
    fondo_label_registro.place(x=0, y=0, relwidth=1, relheight=1)
    registro.bind("<Configure>", lambda e: actualizar_fondo(registro, fondo_label_registro, img_original))
    actualizar_fondo(registro, fondo_label_registro, img_original)

    Boton_hamburguesa(registro)

    cont_registro = tk.Frame(registro, bg=None)
    cont_registro.pack(expand=True)

    # Registro centrado y uniforme
    tk.Label(cont_registro, text="Nombre de Usuario:", fg="black", bg=None).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    nombre_entry = tk.Entry(cont_registro, width=25)
    nombre_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(cont_registro, text="Contraseña:", fg="black", bg=None).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    contraseña_entry = tk.Entry(cont_registro, width=25, show="*")
    contraseña_entry.grid(row=1, column=1, padx=10, pady=10)

    mensaje_registro = tk.Label(cont_registro, text="", fg="green", bg=None)
    mensaje_registro.grid(row=2, column=0, columnspan=2, pady=10)

    tk.Button(cont_registro, text="Registrar", width=20, command=lambda: registrar_usuario(nombre_entry, contraseña_entry, mensaje_registro)).grid(row=3, column=0, columnspan=2, pady=10)

    registro.withdraw()
    ventanas["registro"] = registro

    # -------------------- INICIO --------------------
    inicio = tk.Toplevel(principal)
    inicio.title("Inicio")
    inicio.geometry("850x500")

    fondo_label_inicio = tk.Label(inicio)
    fondo_label_inicio.place(x=0, y=0, relwidth=1, relheight=1)
    inicio.bind("<Configure>", lambda e: actualizar_fondo(inicio, fondo_label_inicio, img_original))
    actualizar_fondo(inicio, fondo_label_inicio, img_original)

    Boton_hamburguesa(inicio)

    cont_inicio = tk.Frame(inicio, bg=None)
    cont_inicio.pack(expand=True)

    tk.Label(cont_inicio, text="Bienvenida a la aplicación", font=("Arial", 12, "bold"), fg="black", bg=None).pack(pady=10)
    tk.Label(cont_inicio, text="Conoce más sobre nosotros:", fg="black", bg=None).pack(pady=5)
    tk.Label(cont_inicio, text="Nuestra misión: Brindar a nuestros clientes una experiencia variada, de calidad y precios accesibles.",
             fg="black", bg=None, wraplength=800, justify="center").pack(pady=2)
    tk.Label(cont_inicio, text="Nuestra visión: Ser una página reconocida por su atención personalizada y compromiso.",
             fg="black", bg=None, wraplength=800, justify="center").pack(pady=2)
    tk.Label(cont_inicio, text="Correo electrónico: villamillucasluismanuel@gmail.com", fg="black", bg=None).pack(pady=2)
    tk.Label(cont_inicio, text="Dirección: Av.117pte. 706, Zona Guadalupe Hidalgo", fg="black", bg=None).pack(pady=2)

    imagen1 = Image.open(r"E:\ProyectPython3BP\ubicacion.jpg")
    imagen1 = imagen1.resize((150, 150))
    foto1 = ImageTk.PhotoImage(imagen1)
    tk.Label(cont_inicio, image=foto1, bg=None).pack(pady=10)
    cont_inicio.foto1 = foto1

    inicio.withdraw()
    ventanas["inicio"] = inicio

    # -------------------- CONTACTO --------------------
    contacto = tk.Toplevel(principal)
    contacto.title("Contacto")
    contacto.geometry("850x500")

    fondo_label_contacto = tk.Label(contacto)
    fondo_label_contacto.place(x=0, y=0, relwidth=1, relheight=1)
    contacto.bind("<Configure>", lambda e: actualizar_fondo(contacto, fondo_label_contacto, img_original))
    actualizar_fondo(contacto, fondo_label_contacto, img_original)

    Boton_hamburguesa(contacto)

    cont_contacto = tk.Frame(contacto, bg=None)
    cont_contacto.pack(expand=True)

    tk.Label(cont_contacto, text="Nombre de Usuario", fg="black", bg=None).pack(pady=5)
    usuario_form_entry = tk.Entry(cont_contacto, width=30)
    usuario_form_entry.pack(pady=5)
    tk.Label(cont_contacto, text="Comentario", fg="black", bg=None).pack(pady=5)
    comentario_entry = tk.Entry(cont_contacto, width=50)
    comentario_entry.pack(pady=5)
    mensaje_contacto = tk.Label(cont_contacto, text="", fg="blue", bg=None)
    mensaje_contacto.pack(pady=5)

    tk.Button(cont_contacto, text="Aceptar", width=20, command=lambda: enviar_comentario(usuario_form_entry, mensaje_contacto)).pack(pady=10)
    contacto.withdraw()
    ventanas["contacto"] = contacto

    # -------------------- SALIDA --------------------
    salida = tk.Toplevel(principal)
    salida.title("Salida")
    salida.geometry("850x500")

    fondo_label_salida = tk.Label(salida)
    fondo_label_salida.place(x=0, y=0, relwidth=1, relheight=1)
    salida.bind("<Configure>", lambda e: actualizar_fondo(salida, fondo_label_salida, img_original))
    actualizar_fondo(salida, fondo_label_salida, img_original)

    Boton_hamburguesa(salida)

    cont_salida = tk.Frame(salida, bg=None)
    cont_salida.pack(expand=True)
    tk.Label(cont_salida, text="Gracias por visitarnos. ¡Hasta pronto!", font=("Arial", 12, "bold"), fg="black", bg=None).pack(pady=10)

    salida.withdraw()
    ventanas["salida"] = salida

    principal.mainloop()

# -------------------- FUNCIONES AUXILIARES --------------------
def verificar_login(usuario_entry, contrasena_entry, mensaje_label):
    usuario = usuario_entry.get().strip()
    contrasena = contrasena_entry.get().strip()
    if usuario == "Diseñadora" and contrasena == "11425":
        mensaje_label.config(text=f"Bienvenida {usuario}.", fg="green")
    else:
        mensaje_label.config(text="Usuario o contraseña incorrectos.", fg="red")

def registrar_usuario(nombre_entry, contraseña_entry, mensaje_label):
    nombre = nombre_entry.get().strip()
    contra = contraseña_entry.get().strip()
    if nombre and contra:
        mensaje_label.config(text=f"Bienvenido {nombre}, tu registro fue exitoso.", fg="green")
    else:
        mensaje_label.config(text="Por favor, completa todos los campos.", fg="red")

def enviar_comentario(usuario_entry, mensaje_label):
    nombre = usuario_entry.get().strip()
    if nombre:
        mensaje_label.config(text=f"Gracias {nombre}, tu comentario ha sido enviado.", fg="green")
    else:
        mensaje_label.config(text="Por favor, ingresa tu nombre de usuario.", fg="red")

# -------------------- EJECUCIÓN --------------------
if __name__ == "__main__":
    crear_principal()

