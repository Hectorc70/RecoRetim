from tkinter.filedialog import askdirectory

from archivos.modelos.archivo_excel import Archivo_excel
from archivos.ayuda.rutas_trabajo import Rutas




archivo = Rutas(askdirectory()) 
rutas_lectura = archivo.recuperar_rutas()

class ArchivoIQ(Archivo_excel):
    "ARCHIVO IQ"

    def __init__(self):

        self.ruta = rutas_lectura['IQ']
        Archivo_excel.__init__(self, self.ruta)

    def leer(self):
        
        self.leer_titulos(0, 1)
        print(self.titulos_columnas)        




class ArchivoRetimbre(Archivo_excel):
    """lee layout excel para el retimbre"""

    def __init__(self, ruta):
        self.ruta_archivo = ruta
        Archivo_excel.__init__(self, self.ruta_archivo)

    
    
    def leer(self):
        pass










