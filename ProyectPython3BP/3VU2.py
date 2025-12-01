import tkinter as tk
from PIL import Image, ImageTk

ventanas = {}
fondo_tk_dict = {}
image_path = r"E:\ProyectPython3BP\fondo.jpg"

# -------------------- MAPA DE VENTANAS --------------------
ventana_secundaria_map = {
    "perfil de usuario": ["login", "modificacion de perfil"],
    "atencion al usuario": ["datos y logros de la empresa", "contacto"],
    "editor del auto": ["editor de piezas", "editor de logos", "software"],
    "diseño concluido": ["firmas de contrato", "modificacion del diseño", "historial de versiones"],
    "produccion": ["documentacion de aceptacion para produccion"]
}

# -------------------- FUNCIONES GENERALES --------------------
def actualizar_fondo(ventana_obj, label_fondo, img_original_obj, event=None):
    img = img_original_obj.resize((ventana_obj.winfo_width(), ventana_obj.winfo_height()))
    foto = ImageTk.PhotoImage(img)
    label_fondo.config(image=foto)
    fondo_tk_dict[label_fondo] = foto

def mostrar_ventana(clave):
    # Ocultar todas
    for v in ventanas.values():
        try:
            v.withdraw()
        except:
            pass
    ventanas[clave].deiconify()

# -------------------- MENÚ HAMBURGUESA --------------------
def Boton_hamburguesa(ventana, opciones):
    menu = tk.Frame(ventana, width=180, bg="lightgray")
    menu_visible = [False]

    for texto, ventana_destino in opciones:
        if texto.lower() == "salida":
            btn = tk.Button(menu, text=texto, width=20, bg="white", command=lambda: ventanas["principal"].destroy())
        elif texto.lower() == "regresar":
            btn = tk.Button(menu, text=texto, width=20, bg="white",
                            command=lambda v=ventana_destino: regresar_ventana(ventana, v))
        else:
            btn = tk.Button(menu, text=texto, width=20, bg="white",
                            command=lambda v=ventana_destino: abrir_ventana_dinamica(v))
        btn.pack(pady=5, anchor="w", padx=10)

    menu.place_forget()

    def mostrar_ocultar():
        if menu_visible[0]:
            menu.place_forget()
            menu_visible[0] = False
        else:
            menu.place(x=10, y=60)
            menu_visible[0] = True

    boton = tk.Button(ventana, text="☰", font=("Arial", 12, "bold"),
                      command=mostrar_ocultar, bg="white")
    boton.place(x=10, y=20)

# -------------------- FUNCION REGRESAR --------------------
def regresar_ventana(ventana_actual, destino):
    ventana_actual.withdraw()
    mostrar_ventana(destino)

# -------------------- CREAR VENTANA --------------------
def crear_ventana(nombre, img_original, ventana_padre=None):
    clave = nombre.lower().replace(" ", "_")
    if clave in ventanas:
        mostrar_ventana(clave)
        return ventanas[clave]

    ventana = tk.Toplevel()
    ventana.title(nombre)
    ventana.geometry("930x530")

    # Fondo
    fondo_label = tk.Label(ventana)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    actualizar_fondo(ventana, fondo_label, img_original)
    ventana.bind("<Configure>", lambda e: actualizar_fondo(ventana, fondo_label, img_original))

    # Configuración menú hamburguesa
    opciones_hamburguesa = []

    if ventana_padre is None:
        # Principal
        botones_principal = ["Perfil de usuario", "Atencion al usuario", "Editor del auto",
                             "Diseño concluido", "Produccion", "Salida"]
        opciones_hamburguesa = [(b, b.lower()) for b in botones_principal]
    elif ventana_padre in ventana_secundaria_map:
        # Secundaria: todos los botones terciarias + regresar
        botones_secundaria = ventana_secundaria_map[ventana_padre]
        opciones_hamburguesa = [(b, b.lower().replace(" ", "_")) for b in botones_secundaria]
        opciones_hamburguesa.append(("Regresar", "principal"))
    else:
        # Terciaria: todos los botones de la secundaria + regresar
        for sec, botones in ventana_secundaria_map.items():
            if clave in [b.lower().replace(" ", "_") for b in botones]:
                opciones_hamburguesa = [(b, b.lower().replace(" ", "_")) for b in botones]
                opciones_hamburguesa.append(("Regresar", sec.lower().replace(" ", "_")))
                break

    if opciones_hamburguesa:
        Boton_hamburguesa(ventana, opciones_hamburguesa)

    ventanas[clave] = ventana
    mostrar_ventana(clave)
    return ventana

# -------------------- ABRIR VENTANA DINAMICA --------------------
def abrir_ventana_dinamica(nombre):
    nombre_lc = nombre.lower().replace(" ", "_")

    # Ventana secundaria
    if nombre_lc in [k.replace(" ", "_") for k in ventana_secundaria_map.keys()]:
        # Normalizamos clave
        sec_key = [k for k in ventana_secundaria_map.keys() if k.replace(" ", "_") == nombre_lc][0]
        crear_ventana(sec_key, img_original_global, ventana_padre=sec_key)
        return

    # Ventana terciaria
    for sec, botones in ventana_secundaria_map.items():
        for b in botones:
            if nombre_lc == b.lower().replace(" ", "_"):
                crear_ventana(b, img_original_global, ventana_padre=sec)
                return

# -------------------- CREAR VENTANA PRINCIPAL --------------------
def crear_principal():
    global img_original_global
    img_original_global = Image.open(image_path)

    principal = tk.Tk()
    principal.title("Principal")
    principal.geometry("930x530")
    ventanas["principal"] = principal

    # Fondo
    fondo_label = tk.Label(principal)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    actualizar_fondo(principal, fondo_label, img_original_global)
    principal.bind("<Configure>", lambda e: actualizar_fondo(principal, fondo_label, img_original_global))

    # Botón hamburguesa principal
    botones_principal = ["Perfil de usuario", "Atencion al usuario", "Editor del auto",
                         "Diseño concluido", "Produccion", "Salida"]
    Boton_hamburguesa(principal, [(b, b.lower()) for b in botones_principal])

    principal.mainloop()

# -------------------- EJECUCIÓN --------------------
if __name__ == "__main__":
    crear_principal()
