from tkinter.filedialog import askdirectory

from carpetas import CarpetaNomina
#from archivos.lectura import ArchivoIQ, ReporteSap

def obtener_rutas_archivos():
    CarpetaNomina(askdirectory())

    
def lectura_excel():
    #iq = ArchivoIQ()
    #iq.extraer_control()
    #iq.extraer_ccn_1401()
    #iq.extraer_ccn_1409()
    sap = ReporteSap()
    sap.obtener_control()

obtener_rutas_archivos()

#lectura_excel()


class ArchivoLayout():

    def __init__(self):
        pass

    
    
    def escribir_conceptos(self):
        pass

    
    def escribir_reporte_sap(self):
        pass


    def escribir_rutas_archivos(self):

        pass

    




