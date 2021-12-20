from tkinter import *
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import modelo
import os
from estilos import settings as formato
from tkinter import messagebox as mb
import string


class Ventana:
    """Esta clase crea la ventana principal
    y el notebook con sus marcos.
    Se definen las rutas de acceso a las imágenes y logos.
    Permite el flujo de información entre el usuario
    y la base de datos."""

    def __init__(self, window):
        """Este método es el inicializador de la clase."""
        """Define la ruta de las diferentes carpetas."""
        DIR_CARP = os.path.dirname((os.path.abspath(__file__)))
        CARP_LOG = os.path.join(DIR_CARP, "logo")

        """Crea una instancia de la clase Abmc."""
        self.req_data = modelo.Abmc()

        """Crea una instancia de la ventana panel_c
        y define sus caraterísticas."""
        self.panel_c = window
        self.panel_c.title("ABMC - Clientes")
        self.panel_c.iconbitmap(CARP_LOG + "\\pyteamlogo.ico")
        self.fichero = ttk.Notebook(self.panel_c)
        self.f_alta()
        self.f_consulta()
        self.f_modific()
        self.f_baja()
        self.list_todos()
        self.treeview()
        self.fichero.pack(expand=1, fill="both")
        self.fichero.grid(column=0, row=0, padx=10, pady=10)
        self.fichero.pressed_index = None

        """Define el estilo del Notebook y del treeview."""
        self.Style = ttk.Style()
        self.settings = formato
        self.Style.theme_create("formatos", parent="alt", settings=self.settings)
        self.Style.theme_use("formatos")

    def f_alta(self):
        """Este método define las etiquetas
        y botones del Frame f-altas."""

        def caps(event):
            """Este método evita que se ingresen
            letras minúsculas en el dominio."""
            self.dominio_a.set(self.dominio_a.get().upper())

        def validate_entry(text):
            """Este método evitamos el ingreso de texto
            en los campos DNI y teléfono."""
            return text.isdecimal()

        self.ficha1 = tkinter.Frame(self.fichero, background="#F8F9F9")
        self.fichero.add(self.ficha1, text="Alta de Cliente")
        self.etqmarco1 = tkinter.LabelFrame(
            self.ficha1, text="Ingrese los datos del Cliente", background="#F8F9F9"
        )
        self.etqmarco1.grid(column=0, row=0, padx=5, pady=10)
        self.etq_1a = ttk.Label(self.etqmarco1, text="DNI:", background="#F8F9F9")
        self.etq_1a.grid(column=0, row=0, padx=4, pady=4)
        self.etq_1at = ttk.Label(
            self.etqmarco1, text="", width=30, background="#F8F9F9"
        )
        self.etq_1at.grid(column=2, row=0, padx=4, pady=4)
        self.dni_a = tk.StringVar()
        self.entrydni_a = ttk.Entry(
            self.etqmarco1,
            validate="key",
            validatecommand=(self.etqmarco1.register(validate_entry), "%S"),
            textvariable=self.dni_a,
        )
        self.entrydni_a.grid(column=1, row=0, padx=4, pady=4, sticky="w")
        self.etq_2a = ttk.Label(self.etqmarco1, text="Nombre:", background="#F8F9F9")
        self.etq_2a.grid(column=0, row=1, padx=4, pady=4)
        self.nombre_a = tk.StringVar()
        self.entrynombre_a = ttk.Entry(
            self.etqmarco1, textvariable=self.nombre_a, width=40
        )
        self.entrynombre_a.grid(column=1, row=1, padx=4, pady=4)
        self.etq_3a = ttk.Label(self.etqmarco1, text="Apellido:", background="#F8F9F9")
        self.etq_3a.grid(column=0, row=2, padx=4, pady=4)
        self.apellido_a = tk.StringVar()
        self.entryapellido_a = ttk.Entry(
            self.etqmarco1, textvariable=self.apellido_a, width=40
        )
        self.entryapellido_a.grid(column=1, row=2, padx=4, pady=4)
        self.etq_4a = ttk.Label(self.etqmarco1, text="Marca:", background="#F8F9F9")
        self.etq_4a.grid(column=0, row=3, padx=4, pady=4)
        self.marca_a = tk.StringVar()
        self.entrymarca_a = ttk.Entry(
            self.etqmarco1, textvariable=self.marca_a, width=40
        )
        self.entrymarca_a.grid(column=1, row=3, padx=4, pady=4)
        self.etq_5a = ttk.Label(self.etqmarco1, text="Modelo:", background="#F8F9F9")
        self.etq_5a.grid(column=0, row=4, padx=4, pady=4)
        self.modelo_a = tk.StringVar()
        self.entrymodelo_a = ttk.Entry(
            self.etqmarco1, textvariable=self.modelo_a, width=40
        )
        self.entrymodelo_a.grid(column=1, row=4, padx=4, pady=4)
        self.etq_6a = ttk.Label(self.etqmarco1, text="Dominio:", background="#F8F9F9")
        self.etq_6a.grid(column=0, row=5, padx=4, pady=4)
        self.dominio_a = tk.StringVar()
        self.entrydominio_a = ttk.Entry(self.etqmarco1, textvariable=self.dominio_a)
        self.entrydominio_a.grid(column=1, row=5, padx=4, pady=4, sticky="w")
        self.entrydominio_a.bind("<KeyRelease>", caps)
        self.etq_7a = ttk.Label(self.etqmarco1, text="Calle:", background="#F8F9F9")
        self.etq_7a.grid(column=0, row=6, padx=4, pady=4)
        self.calle_a = tk.StringVar()
        self.entrycalle_a = ttk.Entry(
            self.etqmarco1, textvariable=self.calle_a, width=40
        )
        self.entrycalle_a.grid(column=1, row=6, padx=4, pady=4)
        self.etq_8a = ttk.Label(self.etqmarco1, text="Altura:", background="#F8F9F9")
        self.etq_8a.grid(column=0, row=7, padx=4, pady=4)
        self.altura_a = tk.StringVar()
        self.entryaltura_a = ttk.Entry(self.etqmarco1, textvariable=self.altura_a)
        self.entryaltura_a.grid(column=1, row=7, padx=4, pady=4, sticky="w")
        self.etq_9a = ttk.Label(self.etqmarco1, text="Piso:", background="#F8F9F9")
        self.etq_9a.grid(column=0, row=8, padx=4, pady=4)
        self.piso_a = tk.StringVar()
        self.entrypiso_a = ttk.Entry(self.etqmarco1, textvariable=self.piso_a)
        self.entrypiso_a.grid(column=1, row=8, padx=4, pady=4, sticky="w")
        self.etq_10a = ttk.Label(
            self.etqmarco1, text="Departamento:", background="#F8F9F9"
        )
        self.etq_10a.grid(column=0, row=9, padx=4, pady=4)
        self.depto_a = tk.StringVar()
        self.entrydepto_a = ttk.Entry(self.etqmarco1, textvariable=self.depto_a)
        self.entrydepto_a.grid(column=1, row=9, padx=4, pady=4, sticky="w")
        self.etq_11a = ttk.Label(
            self.etqmarco1, text="Localidad:", background="#F8F9F9"
        )
        self.etq_11a.grid(column=0, row=10, padx=4, pady=4)
        self.loc_a = tk.StringVar()
        self.entryloc_a = ttk.Entry(self.etqmarco1, textvariable=self.loc_a, width=40)
        self.entryloc_a.grid(column=1, row=10, padx=4, pady=4)
        self.etq12 = ttk.Label(self.etqmarco1, text="email:", background="#F8F9F9")
        self.etq12.grid(column=0, row=11, padx=4, pady=4)
        self.email_a = tk.StringVar()
        self.entryemail_a = ttk.Entry(self.etqmarco1, textvariable=self.email_a)
        self.entryemail_a.grid(column=1, row=11, padx=4, pady=4, sticky="w")
        self.etq13 = ttk.Label(self.ficha1, text="", background="#F8F9F9")
        self.etq13.grid(column=0, row=12, padx=4, pady=8)
        self.boton_ac = Button(
            self.ficha1,
            text="Confirmar",
            command=lambda: [self.alta_datos(), self.limpia_lt(), self.limpia_tv()],
            relief="raised",
            width=10,
        )
        self.boton_ac.place(x=366, y=362)
        self.boton_ac = Button(
            self.ficha1,
            text="Limpiar",
            command=self.limpia_a,
            relief="raised",
            width=10,
        )
        self.boton_ac.place(x=460, y=362)

    def alta_datos(self):
        """Este método envía la iformación necesaria
        para insertar un nuevo registro en la tabla clientes."""
        datos = (
            self.dni_a.get(),
            string.capwords(self.nombre_a.get()),
            string.capwords(self.apellido_a.get()),
            string.capwords(self.marca_a.get()),
            string.capwords(self.modelo_a.get()),
            self.dominio_a.get(),
            string.capwords(self.calle_a.get()),
            self.altura_a.get(),
            self.piso_a.get(),
            self.depto_a.get().upper(),
            string.capwords(self.loc_a.get()),
            self.email_a.get().lower(),
        )
        self.req_data.alta(
            datos,
            self.dni_a,
            self.nombre_a,
            self.apellido_a,
            self.marca_a,
            self.modelo_a,
            self.dominio_a,
            self.calle_a,
            self.altura_a,
            self.piso_a,
            self.depto_a,
            self.loc_a,
            self.email_a,
        )

    def limpia_a(self):
        """Este método limpia los campos
        del formulario de altas."""
        self.dni_a.set("")
        self.nombre_a.set("")
        self.apellido_a.set("")
        self.dominio_a.set("")
        self.marca_a.set("")
        self.modelo_a.set("")
        self.calle_a.set("")
        self.altura_a.set("")
        self.piso_a.set("")
        self.depto_a.set("")
        self.loc_a.set("")
        self.email_a.set("")

    def f_consulta(self):
        """Este método define las etiquetas
        y botones del Frame f-consultas."""
        self.ficha2 = tkinter.Frame(self.fichero, background="#F8F9F9")
        self.fichero.add(self.ficha2, text="Consulta por DNI")
        self.etqmarco2 = tkinter.LabelFrame(
            self.ficha2, text="Ingrese el DNI a consultar", background="#F8F9F9"
        )
        self.etqmarco2.grid(column=0, row=0, padx=5, pady=10)
        self.etq_1c = ttk.Label(self.etqmarco2, text="DNI:", background="#F8F9F9")
        self.etq_1c.grid(column=0, row=0, padx=4, pady=4)
        self.etq_1ct = ttk.Label(
            self.etqmarco2, text="", width=30, background="#F8F9F9"
        )
        self.etq_1ct.grid(column=2, row=0, padx=4, pady=4)
        self.dni_c = tk.StringVar()
        self.entrydni = ttk.Entry(self.etqmarco2, textvariable=self.dni_c)
        self.entrydni.grid(column=1, row=0, padx=4, pady=4, sticky="w")
        self.etq_2c = ttk.Label(self.etqmarco2, text="Nombre:", background="#F8F9F9")
        self.etq_2c.grid(column=0, row=1, padx=4, pady=4)
        self.nombre_c = tk.StringVar()
        self.entrynombre = ttk.Entry(
            self.etqmarco2, textvariable=self.nombre_c, state="readonly", width=40
        )
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.etq_3c = ttk.Label(self.etqmarco2, text="Apellido:", background="#F8F9F9")
        self.etq_3c.grid(column=0, row=2, padx=4, pady=4)
        self.apellido_c = tk.StringVar()
        self.entryapellido = ttk.Entry(
            self.etqmarco2, textvariable=self.apellido_c, state="readonly", width=40
        )
        self.entryapellido.grid(column=1, row=2, padx=4, pady=4)
        self.etq_4c = ttk.Label(self.etqmarco2, text="Marca:", background="#F8F9F9")
        self.etq_4c.grid(column=0, row=3, padx=4, pady=4)
        self.marca_c = tk.StringVar()
        self.entrymarca = ttk.Entry(
            self.etqmarco2, textvariable=self.marca_c, state="readonly", width=40
        )
        self.entrymarca.grid(column=1, row=3, padx=4, pady=4)
        self.etq_5c = ttk.Label(self.etqmarco2, text="Modelo:", background="#F8F9F9")
        self.etq_5c.grid(column=0, row=4, padx=4, pady=4)
        self.modelo_c = tk.StringVar()
        self.entrymodelo = ttk.Entry(
            self.etqmarco2, textvariable=self.modelo_c, state="readonly", width=40
        )
        self.entrymodelo.grid(column=1, row=4, padx=4, pady=4)
        self.etq_6c = ttk.Label(self.etqmarco2, text="Dominio:", background="#F8F9F9")
        self.etq_6c.grid(column=0, row=5, padx=4, pady=4)
        self.dominio_c = tk.StringVar()
        self.entrydominio = ttk.Entry(
            self.etqmarco2, textvariable=self.dominio_c, state="readonly", width=40
        )
        self.entrydominio.grid(column=1, row=5, padx=4, pady=4)
        self.etq_7c = ttk.Label(self.etqmarco2, text="Calle:", background="#F8F9F9")
        self.etq_7c.grid(column=0, row=6, padx=4, pady=4)
        self.calle_c = tk.StringVar()
        self.entrycalle = ttk.Entry(
            self.etqmarco2, textvariable=self.calle_c, state="readonly", width=40
        )
        self.entrycalle.grid(column=1, row=6, padx=4, pady=4)
        self.etq_8c = ttk.Label(self.etqmarco2, text="Altura:", background="#F8F9F9")
        self.etq_8c.grid(column=0, row=7, padx=4, pady=4)
        self.altura_c = tk.StringVar()
        self.entryaltura = ttk.Entry(
            self.etqmarco2, textvariable=self.altura_c, state="readonly"
        )
        self.entryaltura.grid(column=1, row=7, padx=4, pady=4, sticky="w")
        self.etq_9c = ttk.Label(self.etqmarco2, text="Piso:", background="#F8F9F9")
        self.etq_9c.grid(column=0, row=8, padx=4, pady=4)
        self.piso_c = tk.StringVar()
        self.entrypiso = ttk.Entry(
            self.etqmarco2, textvariable=self.piso_c, state="readonly"
        )
        self.entrypiso.grid(column=1, row=8, padx=4, pady=4, sticky="w")
        self.etq_10c = ttk.Label(
            self.etqmarco2, text="Departamento:", background="#F8F9F9"
        )
        self.etq_10c.grid(column=0, row=9, padx=4, pady=4)
        self.depto_c = tk.StringVar()
        self.entrydepto = ttk.Entry(
            self.etqmarco2, textvariable=self.depto_c, state="readonly"
        )
        self.entrydepto.grid(column=1, row=9, padx=4, pady=4, sticky="w")
        self.etq_11c = ttk.Label(
            self.etqmarco2, text="Localidad:", background="#F8F9F9"
        )
        self.etq_11c.grid(column=0, row=10, padx=4, pady=4)
        self.loc_c = tk.StringVar()
        self.entryloc = ttk.Entry(
            self.etqmarco2, textvariable=self.loc_c, state="readonly", width=40
        )
        self.entryloc.grid(column=1, row=10, padx=4, pady=4)
        self.etq12 = ttk.Label(self.etqmarco2, text="email:", background="#F8F9F9")
        self.etq12.grid(column=0, row=11, padx=4, pady=4)
        self.email_c = tk.StringVar()
        self.entryemail = ttk.Entry(
            self.etqmarco2, textvariable=self.email_c, state="readonly"
        )
        self.entryemail.grid(column=1, row=11, padx=4, pady=4, sticky="w")
        self.boton_cb = Button(
            self.ficha2,
            text="Buscar",
            command=self.consultar,
            relief="raised",
            width=10,
        )
        self.boton_cb.place(x=366, y=362)
        self.boton_cl = Button(
            self.ficha2,
            text="Limpiar",
            command=self.limpia_c,
            relief="raised",
            width=10,
        )
        self.boton_cl.place(x=460, y=362)

    def consultar(self):
        """Este método envía la iformación necesaria
        para consultar los datos asociados a un DNI."""
        datos = (self.dni_c.get(),)
        respuesta = self.req_data.consulta(datos)
        """Genera una ventana cuando
        no se encuentra el DNI en la base de datos."""
        if not respuesta:
            mb.showinfo(
                "Atención",
                "El DNI ingresado no se encuentra en la base de datos",
            )
        if respuesta:
            """Inserta los datos en el f-consulta."""
            self.nombre_c.set(respuesta[0][0])
            self.apellido_c.set(respuesta[0][1])
            self.marca_c.set(respuesta[0][2])
            self.modelo_c.set(respuesta[0][3])
            self.dominio_c.set(respuesta[0][4])
            self.calle_c.set(respuesta[0][5])
            self.altura_c.set(respuesta[0][6])
            self.piso_c.set(respuesta[0][7])
            self.depto_c.set(respuesta[0][8])
            self.loc_c.set(respuesta[0][9])
            self.email_c.set(respuesta[0][10])

    def limpia_c(self):
        """Este método limpia los campos
        de entrada de datos del formulario
        de consultas."""
        self.dni_c.set("")
        self.nombre_c.set("")
        self.apellido_c.set("")
        self.marca_c.set("")
        self.modelo_c.set("")
        self.dominio_c.set("")
        self.calle_c.set("")
        self.altura_c.set("")
        self.piso_c.set("")
        self.depto_c.set("")
        self.loc_c.set("")
        self.email_c.set("")

    def f_modific(self):
        """Este método define las etiquetas
        y botones del Frame f-modificaciones."""
        self.ficha3 = tkinter.Frame(self.fichero, background="#F8F9F9")
        self.fichero.add(self.ficha3, text="Modificaciones")
        self.etqmarco3 = tkinter.LabelFrame(
            self.ficha3, text="Ingrese el DNI a buscar", background="#F8F9F9"
        )
        self.etqmarco3.grid(column=0, row=0, padx=5, pady=10)
        self.etq_1m = ttk.Label(self.etqmarco3, text="DNI:", background="#F8F9F9")
        self.etq_1m.grid(column=0, row=0, padx=4, pady=4)
        self.etq_1mt = ttk.Label(
            self.etqmarco3, text="", width=30, background="#F8F9F9"
        )
        self.etq_1mt.grid(column=2, row=0, padx=4, pady=4)
        self.dni_m = tk.StringVar()
        self.entrydni_m = ttk.Entry(self.etqmarco3, textvariable=self.dni_m)
        self.entrydni_m.grid(column=1, row=0, padx=4, pady=4, sticky="w")
        self.etq_2m = ttk.Label(self.etqmarco3, text="Nombre:", background="#F8F9F9")
        self.etq_2m.grid(column=0, row=1, padx=4, pady=4)
        self.nombre_m = tk.StringVar()
        self.entrynombre_m = ttk.Entry(
            self.etqmarco3, textvariable=self.nombre_m, width=40
        )
        self.entrynombre_m.grid(column=1, row=1, padx=4, pady=4)
        self.etq_3m = ttk.Label(self.etqmarco3, text="Apellido:", background="#F8F9F9")
        self.etq_3m.grid(column=0, row=2, padx=4, pady=4)
        self.apellido_m = tk.StringVar()
        self.entryapellido_m = ttk.Entry(
            self.etqmarco3, textvariable=self.apellido_m, width=40
        )
        self.entryapellido_m.grid(column=1, row=2, padx=4, pady=4)
        self.etq_4m = ttk.Label(self.etqmarco3, text="Marca:", background="#F8F9F9")
        self.etq_4m.grid(column=0, row=3, padx=4, pady=4)
        self.marca_m = tk.StringVar()
        self.entrymarca_m = ttk.Entry(
            self.etqmarco3, textvariable=self.marca_m, width=40
        )
        self.entrymarca_m.grid(column=1, row=3, padx=4, pady=4)
        self.etq_5m = ttk.Label(self.etqmarco3, text="Modelo:", background="#F8F9F9")
        self.etq_5m.grid(column=0, row=4, padx=4, pady=4)
        self.modelo_m = tk.StringVar()
        self.entrymodelo_m = ttk.Entry(
            self.etqmarco3, textvariable=self.modelo_m, width=40
        )
        self.entrymodelo_m.grid(column=1, row=4, padx=4, pady=4)
        self.etq_6m = ttk.Label(self.etqmarco3, text="Dominio:", background="#F8F9F9")
        self.etq_6m.grid(column=0, row=5, padx=4, pady=4)
        self.dominio_m = tk.StringVar()
        self.entrydominio_m = ttk.Entry(self.etqmarco3, textvariable=self.dominio_m)
        self.entrydominio_m.grid(column=1, row=5, padx=4, pady=4, sticky="w")
        self.etq_7m = ttk.Label(self.etqmarco3, text="Calle:", background="#F8F9F9")
        self.etq_7m.grid(column=0, row=6, padx=4, pady=4)
        self.calle_m = tk.StringVar()
        self.entrycalle_m = ttk.Entry(
            self.etqmarco3, textvariable=self.calle_m, width=40
        )
        self.entrycalle_m.grid(column=1, row=6, padx=4, pady=4)
        self.etq_8m = ttk.Label(self.etqmarco3, text="Altura:", background="#F8F9F9")
        self.etq_8m.grid(column=0, row=7, padx=4, pady=4)
        self.altura_m = tk.StringVar()
        self.entryaltura_m = ttk.Entry(self.etqmarco3, textvariable=self.altura_m)
        self.entryaltura_m.grid(column=1, row=7, padx=4, pady=4, sticky="w")
        self.etq_9m = ttk.Label(self.etqmarco3, text="Piso:", background="#F8F9F9")
        self.etq_9m.grid(column=0, row=8, padx=4, pady=4)
        self.piso_m = tk.StringVar()
        self.entrypiso_m = ttk.Entry(self.etqmarco3, textvariable=self.piso_m)
        self.entrypiso_m.grid(column=1, row=8, padx=4, pady=4, sticky="w")
        self.etq_10m = ttk.Label(
            self.etqmarco3, text="Departamento:", background="#F8F9F9"
        )
        self.etq_10m.grid(column=0, row=9, padx=4, pady=4)
        self.depto_m = tk.StringVar()
        self.entrydepto_m = ttk.Entry(self.etqmarco3, textvariable=self.depto_m)
        self.entrydepto_m.grid(column=1, row=9, padx=4, pady=4, sticky="w")
        self.etq_11m = ttk.Label(
            self.etqmarco3, text="Localidad:", background="#F8F9F9"
        )
        self.etq_11m.grid(column=0, row=10, padx=4, pady=4)
        self.loc_m = tk.StringVar()
        self.entryloc_m = ttk.Entry(self.etqmarco3, textvariable=self.loc_m, width=40)
        self.entryloc_m.grid(column=1, row=10, padx=4, pady=4)
        self.etq12m = ttk.Label(self.etqmarco3, text="email:", background="#F8F9F9")
        self.etq12m.grid(column=0, row=11, padx=4, pady=4)
        self.email_m = tk.StringVar()
        self.entryemail_m = ttk.Entry(self.etqmarco3, textvariable=self.email_m)
        self.entryemail_m.grid(column=1, row=11, padx=4, pady=4, sticky="w")
        self.boton_mb = Button(
            self.ficha3, text="Buscar", command=self.buscar_m, relief="raised", width=10
        )
        self.boton_mb.place(x=366, y=362)
        self.boton_mm = Button(
            self.ficha3,
            text="Modificar",
            command=lambda: [
                self.modific(),
                self.limpia_lt(),
                self.limpia_tv(),
            ],
            relief="raised",
            width=10,
        )
        self.boton_mm.place(x=460, y=362)

    def buscar_m(self):
        """Este método envía la iformación necesaria
        para consultar los datos asociados a un DNI."""
        datos = (self.dni_m.get(),)
        respuesta = self.req_data.consulta(datos)
        """Genera una ventana cuando
        no se encuentra el DNI en la base de datos."""
        if not respuesta:
            mb.showinfo(
                "Atención",
                "El DNI ingresado no se encuentra en la base de datos",
            )
        if respuesta:
            """Inserta los datos en el f-modificaciones."""
            self.nombre_m.set(respuesta[0][0])
            self.apellido_m.set(respuesta[0][1])
            self.marca_m.set(respuesta[0][2])
            self.modelo_m.set(respuesta[0][3])
            self.dominio_m.set(respuesta[0][4])
            self.calle_m.set(respuesta[0][5])
            self.altura_m.set(respuesta[0][6])
            self.piso_m.set(respuesta[0][7])
            self.depto_m.set(respuesta[0][8])
            self.loc_m.set(respuesta[0][9])
            self.email_m.set(respuesta[0][10])
            self.entrydni_m.configure(state="disabled")

    def modific(self):
        """Este método envía la iformación necesaria
        para modificar los datos asociados a un DNI."""
        datos = (
            string.capwords(self.nombre_m.get()),
            string.capwords(self.apellido_m.get()),
            string.capwords(self.marca_m.get()),
            string.capwords(self.modelo_m.get()),
            string.capwords(self.calle_m.get()),
            self.dominio_m.get().upper(),
            self.altura_m.get(),
            self.piso_m.get(),
            self.depto_m.get().upper(),
            string.capwords(self.loc_m.get()),
            self.email_m.get().lower(),
            self.dni_m.get(),
        )
        self.req_data.modific(
            datos,
            self.dni_m,
            self.nombre_m,
            self.apellido_m,
            self.dominio_m,
            self.marca_m,
            self.modelo_m,
            self.calle_m,
            self.altura_m,
            self.piso_m,
            self.depto_m,
            self.loc_m,
            self.email_m,
        )
        self.entrydni_m.configure(state="enabled")

    def f_baja(self):
        """Este método define las etiquetas
        y botones del Frame f-bajas."""
        self.ficha4 = tkinter.Frame(self.fichero, background="#F8F9F9")
        self.fichero.add(self.ficha4, text="Bajas por DNI")
        self.etqmarco4 = tkinter.LabelFrame(
            self.ficha4, text="Ingrese el DNI a buscar", background="#F8F9F9"
        )
        self.etqmarco4.grid(column=0, row=0, padx=5, pady=10)
        self.etq_1b = ttk.Label(self.etqmarco4, text="DNI:", background="#F8F9F9")
        self.etq_1b.grid(column=0, row=0, padx=4, pady=4)
        self.etq_1bt = ttk.Label(
            self.etqmarco4, text="", width=30, background="#F8F9F9"
        )
        self.etq_1bt.grid(column=2, row=0, padx=4, pady=4)
        self.dni_b = tk.StringVar()
        self.entrydni_b = ttk.Entry(self.etqmarco4, textvariable=self.dni_b)
        self.entrydni_b.grid(column=1, row=0, padx=4, pady=4, sticky="w")
        self.etq_2b = ttk.Label(self.etqmarco4, text="Nombre:", background="#F8F9F9")
        self.etq_2b.grid(column=0, row=1, padx=4, pady=4)
        self.nombre_b = tk.StringVar()
        self.entrynombre_b = ttk.Entry(
            self.etqmarco4, textvariable=self.nombre_b, state="readonly", width=40
        )
        self.entrynombre_b.grid(column=1, row=1, padx=4, pady=4)
        self.etq_3b = ttk.Label(self.etqmarco4, text="Apellido:", background="#F8F9F9")
        self.etq_3b.grid(column=0, row=2, padx=4, pady=4)
        self.apellido_b = tk.StringVar()
        self.entryapellido_b = ttk.Entry(
            self.etqmarco4, textvariable=self.apellido_b, state="readonly", width=40
        )
        self.entryapellido_b.grid(column=1, row=2, padx=4, pady=4)
        self.etq_4b = ttk.Label(self.etqmarco4, text="Marca:", background="#F8F9F9")
        self.etq_4b.grid(column=0, row=3, padx=4, pady=4)
        self.marca_b = tk.StringVar()
        self.entrymarca_b = ttk.Entry(
            self.etqmarco4, textvariable=self.marca_b, state="readonly", width=40
        )
        self.entrymarca_b.grid(column=1, row=3, padx=4, pady=4)
        self.etq_5b = ttk.Label(self.etqmarco4, text="Modelo:", background="#F8F9F9")
        self.etq_5b.grid(column=0, row=4, padx=4, pady=4)
        self.modelo_b = tk.StringVar()
        self.entrymodelo_b = ttk.Entry(
            self.etqmarco4, textvariable=self.modelo_b, state="readonly", width=40
        )
        self.entrymodelo_b.grid(column=1, row=4, padx=4, pady=4)
        self.etq_6b = ttk.Label(self.etqmarco4, text="Dominio:", background="#F8F9F9")
        self.etq_6b.grid(column=0, row=5, padx=4, pady=4)
        self.dominio_b = tk.StringVar()
        self.entrydominio_b = ttk.Entry(
            self.etqmarco4, textvariable=self.dominio_b, state="readonly"
        )
        self.entrydominio_b.grid(column=1, row=5, padx=4, pady=4, sticky="w")
        self.etq_7b = ttk.Label(self.etqmarco4, text="Calle:", background="#F8F9F9")
        self.etq_7b.grid(column=0, row=6, padx=4, pady=4)
        self.calle_b = tk.StringVar()
        self.entrycalle_b = ttk.Entry(
            self.etqmarco4, textvariable=self.calle_b, state="readonly", width=40
        )
        self.entrycalle_b.grid(column=1, row=6, padx=4, pady=4)
        self.etq_8b = ttk.Label(self.etqmarco4, text="Altura:", background="#F8F9F9")
        self.etq_8b.grid(column=0, row=7, padx=4, pady=4)
        self.altura_b = tk.StringVar()
        self.entryaltura_b = ttk.Entry(
            self.etqmarco4, textvariable=self.altura_b, state="readonly"
        )
        self.entryaltura_b.grid(column=1, row=7, padx=4, pady=4, sticky="w")
        self.etq_9b = ttk.Label(self.etqmarco4, text="Piso:", background="#F8F9F9")
        self.etq_9b.grid(column=0, row=8, padx=4, pady=4)
        self.piso_b = tk.StringVar()
        self.entrypiso_b = ttk.Entry(
            self.etqmarco4, textvariable=self.piso_b, state="readonly"
        )
        self.entrypiso_b.grid(column=1, row=8, padx=4, pady=4, sticky="w")
        self.etq_10b = ttk.Label(
            self.etqmarco4, text="Departamento:", background="#F8F9F9"
        )
        self.etq_10b.grid(column=0, row=9, padx=4, pady=4)
        self.depto_b = tk.StringVar()
        self.entrydepto_b = ttk.Entry(
            self.etqmarco4, textvariable=self.depto_b, state="readonly"
        )
        self.entrydepto_b.grid(column=1, row=9, padx=4, pady=4, sticky="w")
        self.etq_11b = ttk.Label(
            self.etqmarco4, text="Localidad:", background="#F8F9F9"
        )
        self.etq_11b.grid(column=0, row=10, padx=4, pady=4)
        self.loc_b = tk.StringVar()
        self.entryloc_b = ttk.Entry(
            self.etqmarco4, textvariable=self.loc_b, state="readonly", width=40
        )
        self.entryloc_b.grid(column=1, row=10, padx=4, pady=4)
        self.etq12 = ttk.Label(self.etqmarco4, text="email:", background="#F8F9F9")
        self.etq12.grid(column=0, row=11, padx=4, pady=4)
        self.email_b = tk.StringVar()
        self.entryemail_b = ttk.Entry(
            self.etqmarco4, textvariable=self.email_b, state="readonly"
        )
        self.entryemail_b.grid(column=1, row=11, padx=4, pady=4, sticky="w")
        self.boton_bb = Button(
            self.ficha4, text="Buscar", command=self.buscarb, relief="raised", width=10
        )
        self.boton_bb.place(x=366, y=362)
        self.boton_be = Button(
            self.ficha4,
            text="Eliminar",
            command=lambda: [
                self.baja(),
                self.limpia_lt(),
                self.limpia_tv(),
            ],
            relief="raised",
            width=10,
        )
        self.boton_be.place(x=460, y=362)

    def buscarb(self):
        """Este método envía la iformación necesaria
        para consultar los datos asociados a un DNI."""
        datos = (self.dni_b.get(),)
        respuesta = self.req_data.consulta(datos)

        """Genera una ventana cuando
        no se encuentra el DNI en la base de datos."""
        if not respuesta:
            mb.showinfo(
                "Atención",
                "El DNI ingresado no se encuentra en la base de datos",
            )
        if respuesta:
            """Inserta los datos en el f-bajas."""
            self.nombre_b.set(respuesta[0][0])
            self.apellido_b.set(respuesta[0][1])
            self.marca_b.set(respuesta[0][2])
            self.modelo_b.set(respuesta[0][3])
            self.dominio_b.set(respuesta[0][4])
            self.calle_b.set(respuesta[0][5])
            self.altura_b.set(respuesta[0][6])
            self.piso_b.set(respuesta[0][7])
            self.depto_b.set(respuesta[0][8])
            self.loc_b.set(respuesta[0][9])
            self.email_b.set(respuesta[0][10])

    def baja(self):
        """Este método envía la iformación necesaria
        para borrar de la base los datos
        asociados a un DNI y el DNI mismo."""
        datos = (self.dni_b.get(),)
        self.req_data.baja(
            datos,
            self.dni_b,
            self.nombre_b,
            self.apellido_b,
            self.marca_b,
            self.modelo_b,
            self.dominio_b,
            self.calle_b,
            self.altura_b,
            self.piso_b,
            self.depto_b,
            self.loc_b,
            self.email_b,
        )

    def limpia_b(self):
        """Limpia los campos de entrada
        de datos del formulario de bajas."""
        self.dni_b.set("")
        self.nombre_b.set("")
        self.apellido_b.set("")
        self.marca_b.set("")
        self.modelo_b.set("")
        self.dominio_b.set("")
        self.calle_b.set("")
        self.altura_b.set("")
        self.piso_b.set("")
        self.depto_b.set("")
        self.loc_b.set("")
        self.email_b.set("")

    def list_todos(self):
        """Este método define las etiquetas
        y botones del Frame del listado (ScrolledText)."""
        self.ficha5 = tkinter.Frame(self.fichero, background="#F8F9F9")
        self.fichero.add(self.ficha5, text="Consultas Globales")
        self.etqmarco5 = tkinter.LabelFrame(
            self.ficha5,
            text="Lista de Clientes",
            background="#F8F9F9",
        )
        self.etqmarco5.grid(column=0, row=0, padx=10, pady=10)
        self.boton_ltlt = Button(
            self.ficha5,
            text="Listar Todos",
            command=self.listar,
            relief="raised",
            width=10,
        )
        self.boton_ltlt.place(x=366, y=362)
        self.boton_ltl = Button(
            self.ficha5,
            text="Limpiar",
            command=self.limpia_lt,
            relief="raised",
            width=10,
        )
        self.boton_ltl.place(x=460, y=362)
        self.listado = st.ScrolledText(self.etqmarco5, width=53, height=19)
        self.listado.grid(column=0, row=0, padx=4, pady=10)

    def limpia_lt(self):
        """Este método borra los datos
        del listado (ScrolledText)."""
        self.listado.delete("1.0", tk.END)

    def listar(self):
        """Este método envía los datos necesarios
        para insertar los registros
        en el listado (ScrolledText)."""
        self.req_data.recuperar_todos(self.listado)

    def treeview(self):
        """Este método define las etiquetas
        y botones del Frame del listado (Treeview)."""
        self.ficha6 = tkinter.Frame(self.fichero, background="#F8F9F9")
        self.fichero.add(self.ficha6, text="Treeview")
        self.etqmarco6 = tkinter.LabelFrame(
            self.ficha6,
            text="Lista Treeview",
            background="#F8F9F9",
        )
        self.etqmarco6.grid(column=0, row=0, padx=10, pady=10)
        self.boton_tvlt = Button(
            self.ficha6,
            text="Listar Todos",
            command=self.lista_tv,
            relief="raised",
            width=10,
        )
        self.boton_tvlt.place(x=366, y=362)
        self.boton_tvl = Button(
            self.ficha6,
            text="Limpiar",
            command=self.limpia_tv,
            relief="raised",
            width=10,
        )
        self.boton_tvl.place(x=460, y=362)
        self.datosc = ttk.Treeview(
            self.etqmarco6,
            column=(
                "col1",
                "col2",
                "col3",
                "col4",
                "col5",
                "col6",
            ),
            show="headings",
        )
        self.datosc.heading("#1", text="DNI")
        self.datosc.heading("#2", text="Nombre")
        self.datosc.heading("#3", text="Apellido")
        self.datosc.heading("#4", text="Dominio")
        self.datosc.heading("#5", text="Marca")
        self.datosc.heading("#6", text="Modelo")
        self.datosc.column("col1", width=83, minwidth=83)
        self.datosc.column("col2", width=83, minwidth=83)
        self.datosc.column("col3", width=83, minwidth=83)
        self.datosc.column("col4", width=83, minwidth=83)
        self.datosc.column("col5", width=83, minwidth=83)
        self.datosc.column("col6", width=83, minwidth=83)

        """Establecemos la posición de los controles del Treeview"""
        self.datosc.grid(column=0, row=0, padx=1, pady=10)
        self.datoscsb = ttk.Scrollbar(
            self.etqmarco6, orient="vertical", command=self.datosc.yview
        )
        self.datoscsb.grid(row=0, column=1, sticky="NW", pady=10, padx=1, ipady=100)

    def limpia_tv(self):
        """Este método borra los datos
        del listado (ScrolledText)."""
        self.datosc.delete(*self.datosc.get_children())

    def lista_tv(self):
        """Este método envía los datos necesarios
        para insertar los registros
        en el listado (Treeview)."""
        self.req_data.lista_tree(self.datosc)
