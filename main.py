from tkinter.filedialog import askdirectory

from carpetas import CarpetaNomina
from archivos.rutas import Rutas


def obtener_rutas_archivos():
    CarpetaNomina(askdirectory())

def obtener_documentos():
    Rutas(askdirectory())


#obtener_rutas_archivos()

obtener_rutas_archivos()

