

from carpetas import CarpetaNomina
from archivos.lectura import ArchivoIQ

def obtener_rutas_archivos():
    CarpetaNomina(askdirectory())

    
def lectura_excel():
    iq = ArchivoIQ()
    #iq.extraer_control()
    #iq.extraer_ccn_1401()
    #iq.extraer_ccn_1409()
#obtener_rutas_archivos()

lectura_excel()

