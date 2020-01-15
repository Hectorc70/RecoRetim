

from carpetas import CarpetaNomina
from archivos.lectura import ArchivoIQ

def obtener_rutas_archivos():
    CarpetaNomina(askdirectory())

    
def lectura_excel():
    iq = ArchivoIQ()
    iq.extraer_control()
#obtener_rutas_archivos()

lectura_excel()

