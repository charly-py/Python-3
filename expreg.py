import re

# Creamos la clase Validar.
class Validar:
    """Esta clase valida que los datos ingresados
    al sistema concuerden con los parámetros establecidos."""

    def __init__(self, validar):
        """Este es inicializador de clase."""
        self.validar = validar

    @classmethod
    def chkdni(cls, datos):
        """Método de clase para verificar
        que el DNI ingresado sea correcto."""
        chk_dni = str(datos[0])
        exp_reg = "^[1-9][0-9]{7,7}$"
        if re.match(exp_reg, chk_dni):
            return datos[0]

    @classmethod
    def chkdom(cls, datos):
        """Método de clase para verificar
        que el dominio ingresado tenga el formato correcto."""
        chk_dni = str(datos[5])
        exp_reg = "^([A-Z]{2}\d{2,2})\s*?(\d[A-Z]{2})$"
        if re.match(exp_reg, chk_dni):
            return datos[5]
