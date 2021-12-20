"""Importamos las librerías necesarias."""
from tkinter import Tk
from vista import Ventana


class Controller:
    """Esta clase es la puerta de acceso al programa."""

    def __init__(self, panelc):
        """Este método es inicializador de clase."""
        self.panel_c = panelc
        obj = Ventana(self.panel_c)


if __name__ == "__main__":
    """Crea una instancia de Controller y de la vista."""
    panel_c = Tk()
    objeto = Controller(panel_c)
    panel_c.mainloop()
