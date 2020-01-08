from tkinter.filedialog import askdirectory

from carpetas import CarpetaNomina


def obtener_rutas_archivos():
    CarpetaNomina(askdirectory())
    
obtener_rutas_archivos()

