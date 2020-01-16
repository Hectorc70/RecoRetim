

from timbres_txt.ordinaria import CarpetaNomina 
from archivos.lectura import ArchivoIQ, ReporteSap

def obtener_rutas_archivos():
    CarpetaNomina(askdirectory())

    
def lectura_excel():
    #iq = ArchivoIQ()
    #iq.extraer_control()
    #iq.extraer_ccn_1401()
    #iq.extraer_ccn_1409()
    sap = ReporteSap()
    sap.obtener_control()

#obtener_rutas_archivos()

lectura_excel()

