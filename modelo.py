"""Importamos las librerías necesarias."""
import sqlite3
import os
import errno
import tkinter as tk
from tkinter import messagebox as mb
import expreg


class Abmc:
    """Esta clase representa la información con la cual el sistema opera.
    Gestiona todos los accesos a dicha información.
    Y permite efectuar consultas, altas, bajas y modificaciones de registros.
    En otras palabras contiene la lógica del programa."""

    def __init__(self):
        """Este método es el inicializador de la clase."""
        try:
            """Primero crea el directorio que se va a guardar
            la base de datos, si no existe."""
            os.mkdir("db")
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        """Luego define la ruta de las diferentes carpetas."""
        DIR_CARP = os.path.dirname((os.path.abspath(__file__)))
        CARP_DB = os.path.join(DIR_CARP, "db")
        """Conecta a la base de datos y crea el cursor."""
        conexion = sqlite3.connect(CARP_DB + "\\pm_basic.db")
        cursor = conexion.cursor()
        """Y crea la tabla clientes si no existe."""
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS clientes (
                    dni INTEGER PRIMARY KEY,
                    nombre VARCHAR(100),
                    apellido VARCHAR(100),
                    marca VARCHAR(100),
                    modelo VARCHAR(100),
                    dominio VARCHAR(7) UNIQUE,
                    calle VARCHAR(100),
                    altura INTEGER,
                    piso VARCHAR (3),
                    depto VARCHAR(5),
                    localidad VARCHAR(100),
                    email VARCHAR(100))"""
        )
        conexion.commit()

    def abrir(self):
        """Este método se conecta a la base de datos."""
        """Primero define la ruta de las diferentes carpetas."""
        DIR_CARP = os.path.dirname((os.path.abspath(__file__)))
        CARP_DB = os.path.join(DIR_CARP, "db")
        """Y luego conecta a la base de datos."""
        try:
            conexion = sqlite3.connect(CARP_DB + "\\pm_basic.db")
            return conexion
        except:
            mb.showerror("Error", "No se pudo conectar a la base.")

    def limpia_f_alta(
        self,
        dni_a,
        nombre_a,
        apellido_a,
        marca_a,
        modelo_a,
        dominio_a,
        calle_a,
        altura_a,
        piso_a,
        depto_a,
        loc_a,
        email_a,
    ):
        """Este método limpia los campos
        del formulario de altas."""
        dni_a.set("")
        nombre_a.set("")
        apellido_a.set("")
        dominio_a.set("")
        marca_a.set("")
        modelo_a.set("")
        calle_a.set("")
        altura_a.set("")
        piso_a.set("")
        depto_a.set("")
        loc_a.set("")
        email_a.set("")

    def alta(
        self,
        datos,
        dni_a,
        nombre_a,
        apellido_a,
        marca_a,
        modelo_a,
        dominio_a,
        calle_a,
        altura_a,
        piso_a,
        depto_a,
        loc_a,
        email_a,
    ):
        """Este método registra clientes nuevos en la base de datos."""
        """Primero conecta a la base de datos y crea el cursor."""
        conexion = self.abrir()
        cursor = conexion.cursor()
        """Luego chequea que el DNI y el Dominio tengan el formato correcto."""
        self.chk_dni = expreg.Validar.chkdni(datos)
        if not self.chk_dni:
            """Si el formato del DNI es incorrecto genera una ventana
            con el mensaje correspondiente."""
            mb.showinfo("Atención", "El DNI debe estar compuesto por ocho números.")
        self.chk_dom = expreg.Validar.chkdom(datos)
        if not self.chk_dom:
            """Si el formato del Dominio es incorrecto genera una ventana
            con el mensaje correspondiente."""
            mb.showinfo(
                "Atención", "El Dominio debe tener el siguiente formato AA000AA."
            )
        if self.chk_dni and self.chk_dom:
            """Antes de guardar el registro genera una ventana
            para que el usuario confirme el alta."""
            respuesta = mb.askokcancel(
                message="Va a dar de alta un nuevo cliente.\n¿Desea continuar?",
                title="Alta de Cliente",
            )
            if respuesta is True:
                try:
                    """Da de alta el nuevo registro."""
                    sql = "INSERT INTO clientes(dni, nombre, apellido, marca,\
                        modelo, dominio, calle, altura, piso, depto, localidad,\
                        email) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
                    cursor.execute(sql, datos)
                    """Genera un aviso inidicando que el registro
                    se guardo correctamente."""
                    mb.showinfo("Mensaje", "El registro fue guardado correctamente.")
                    self.limpia_f_alta(
                        dni_a,
                        nombre_a,
                        apellido_a,
                        marca_a,
                        modelo_a,
                        dominio_a,
                        calle_a,
                        altura_a,
                        piso_a,
                        depto_a,
                        loc_a,
                        email_a,
                    )
                except sqlite3.Error as e:
                    """Genera un aviso indicando que el DNI o el Dominio
                    ya existen en la base de datos."""
                    mb.showerror("Atención", "El DNI o el Dominio ya existen.")
            else:
                pass

        """Confirma los cambios y cierra la conexión."""
        conexion.commit()
        conexion.close()

    def consulta(self, datos):
        """Este método consulta clientes existentes.
        Conecta a la base de datos"""
        conexion = self.abrir()
        cursor = conexion.cursor()
        """Chequea que el DNI sea correcto."""
        self.chk_dni = expreg.Validar.chkdni(datos)
        if not self.chk_dni:
            """Si es incorrecto el DNI genera una ventana
            con el mensaje correspondiente."""
            mb.showinfo("Atención", "El DNI debe estar compuesto por ocho números.")
        if self.chk_dni:
            """Selecciona la información del DNI solicitado."""
            sql = "SELECT  nombre, apellido, marca, modelo, dominio,\
                    calle, altura, piso, depto, localidad, email FROM clientes WHERE dni=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()

        """Confirma los cambios y cierra la conexión."""
        conexion.commit()
        conexion.close()

    def limpia_f_modific(
        self,
        dni_m,
        nombre_m,
        apellido_m,
        dominio_m,
        marca_m,
        modelo_m,
        calle_m,
        altura_m,
        piso_m,
        depto_m,
        loc_m,
        email_m,
    ):
        """Este método limpia los campos de entrada de datos
        del formulario de modificaciones."""
        dni_m.set("")
        nombre_m.set("")
        apellido_m.set("")
        dominio_m.set("")
        marca_m.set("")
        modelo_m.set("")
        calle_m.set("")
        altura_m.set("")
        piso_m.set("")
        depto_m.set("")
        loc_m.set("")
        email_m.set("")

    def modific(
        self,
        datos,
        dni_m,
        nombre_m,
        apellido_m,
        dominio_m,
        marca_m,
        modelo_m,
        calle_m,
        altura_m,
        piso_m,
        depto_m,
        loc_m,
        email_m,
    ):
        """Este método efectúa modificaciones
        de los datos de los clientes."""
        """Primero conecta a la base de datos y crea el cursor."""
        conexion = self.abrir()
        cursor = conexion.cursor()
        """Luego chequea que el Dominio tenga el formato correcto."""
        self.chk_dom = expreg.Validar.chkdom(datos)
        if not self.chk_dom:
            """Genera una ventana de aviso si el Dominio es incorrecto."""
            mb.showinfo(
                "Atención", "El Dominio debe tener el siguiente formato AA000AA."
            )
        if self.chk_dom:
            """Antes de modificar el registro genera una ventana
            para que el usuario confirme los cambios."""
            respuesta = mb.askokcancel(
                message="Va a modificar los datos correpondientes al DNI: "
                + str(datos[11])
                + "\n¿Desea continuar?",
                title="Modificacion de Datos",
            )
            if respuesta is True:
                try:
                    """Modifica el registro seleccionado."""
                    sql = "UPDATE clientes SET nombre=?, apellido=?, marca=?,\
                        modelo=?, calle=?, dominio=?, altura=?, piso=?, depto=?,\
                        localidad=?, email=? WHERE dni=? "
                    cursor.execute(sql, datos)
                    mb.showinfo(
                        "Información", "Los datos fueron modificados correctamente."
                    )
                    self.limpia_f_modific(
                        dni_m,
                        nombre_m,
                        apellido_m,
                        dominio_m,
                        marca_m,
                        modelo_m,
                        calle_m,
                        altura_m,
                        piso_m,
                        depto_m,
                        loc_m,
                        email_m,
                    )
                except sqlite3.Error as e:
                    """Genera un aviso indicando que el DNI o
                    el Dominio ya existen en la base de datos."""
                    mb.showerror(
                        "Atención", "El Dominio ya existe en la base de datos."
                    )
            else:
                pass

        """Confirma los cambios y cierra la conexión."""
        conexion.commit()
        conexion.close()

    def limpia_f_baja(
        self,
        dni_b,
        nombre_b,
        apellido_b,
        marca_b,
        modelo_b,
        dominio_b,
        calle_b,
        altura_b,
        piso_b,
        depto_b,
        loc_b,
        email_b,
    ):
        """Limpia los campos de entrada
        de datos del formulario de bajas."""
        dni_b.set("")
        nombre_b.set("")
        apellido_b.set("")
        marca_b.set("")
        modelo_b.set("")
        dominio_b.set("")
        calle_b.set("")
        altura_b.set("")
        piso_b.set("")
        depto_b.set("")
        loc_b.set("")
        email_b.set("")

    def baja(
        self,
        datos,
        dni_b,
        nombre_b,
        apellido_b,
        marca_b,
        modelo_b,
        dominio_b,
        calle_b,
        altura_b,
        piso_b,
        depto_b,
        loc_b,
        email_b,
    ):
        """Este método da de baja clientes
        activos en la base de datos."""
        """Primero conecta a la base de datos y crea el cursor."""
        conexion = self.abrir()
        cursor = conexion.cursor()
        """Luego chequea que el DNI sea correcto."""
        self.chk_dni = expreg.Validar.chkdni(datos)
        if self.chk_dni:
            """Antes de eliminar el registro genera una ventana
            para que el usuario confirme la baja."""
            respuesta = mb.askokcancel(
                message="Va a dar de baja de la base de datos al DNI: "
                + str(datos[0])
                + "\n¿Desea continuar?",
                title="Modificacion de Datos",
            )
            if respuesta is True:
                """Borra el DNI indicado, de la base de datos."""
                sql = "DELETE FROM clientes WHERE dni=?"
                cursor.execute(sql, datos)
                mb.showinfo("Información", "El registro ha sido eliminado.")
                self.limpia_f_alta(
                    dni_b,
                    nombre_b,
                    apellido_b,
                    marca_b,
                    modelo_b,
                    dominio_b,
                    calle_b,
                    altura_b,
                    piso_b,
                    depto_b,
                    loc_b,
                    email_b,
                )
            else:
                pass
        if not self.chk_dni:
            mb.showinfo(
                "Atención", "El DNI ingresado no se encuentra en la base de datos"
            )

        """Confirma los cambios y cierra la conexión."""
        conexion.commit()
        conexion.close()

    def recuperar_todos(self, listado):
        """Este método lista (ScrolledText) la
        totalidad de los clientes activos."""
        """Primero conecta a la base de datos y crea el cursor."""
        conexion = self.abrir()
        cursor = conexion.cursor()
        """Borra el contenido del listado
        antes de cargar los nuevos datos."""
        listado.delete("1.0", tk.END)
        """Selecciona los datos de la base."""
        sql = "SELECT dni, nombre, apellido, marca, modelo, dominio,\
            calle, altura, piso, depto, localidad, email FROM clientes"
        cursor.execute(sql)
        respuesta = cursor.fetchall()
        """Inserta los datos en el listado (ScrolledText)."""
        for fila in respuesta:
            listado.insert(
                tk.END,
                "DNI:"
                + str(fila[0])
                + "\nNombre:"
                + fila[1]
                + "\nApellido:"
                + str(
                    fila[2]
                    + "\nMarca:"
                    + str(
                        fila[3]
                        + "\nModelo:"
                        + str(fila[4])
                        + "\nDominio:"
                        + str(fila[5])
                        + "\n----------------------------------------\n"
                    )
                ),
            )
        """Cierra la conexión con la base de datos."""
        conexion.close()

    def lista_tree(self, datosc):
        """Este método lista (Treeview) la
        totalidad de los clientes activos."""
        """Primero conecta a la base de datos y crea el cursor."""
        conexion = self.abrir()
        cursor = conexion.cursor()
        """Borra el contenido del Treeview
        antes de cargar los nuevos datos."""
        datosc.delete(*datosc.get_children())
        sql = "SELECT dni, nombre, apellido, marca, modelo, dominio,\
            calle, altura, piso, depto, localidad, email FROM clientes"
        cursor.execute(sql)
        respuesta = cursor.fetchall()
        """Inserta los datos en el Treeview."""
        for reg in respuesta:
            datosc.insert("", tk.END, values=reg)
        """Cierra la conexión con la base de datos."""
        conexion.close()
