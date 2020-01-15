

from carpetas import CarpetaNomina
from archivos.lectura import ArchivoIQ

def obtener_rutas_archivos():
    CarpetaNomina(askdirectory())

    
def lectura_excel():
    iq = ArchivoIQ()
    iq.leer()
#obtener_rutas_archivos()

lectura_excel()

