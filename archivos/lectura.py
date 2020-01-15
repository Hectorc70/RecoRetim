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
        self.hoja = 0                                      #Hoja de lectura
        self.fila = 2                                      #Fila que omite la lectura

        self.leer_titulos(self.hoja, 2)

    def extraer_control(self):
        """Almacena el Numero de control del IQ"""


        self.control = list() 
       
        COLUMNA = self.claves_columnas['No. Control']    #Columna que lee

        hoja_lectura = self.hojas_lista[self.hoja] 
        titulos = hoja_lectura[COLUMNA]

        for titulo in range(self.fila, len(titulos)):       
             
            self.control.append([titulos[titulo].value])

      
        self.cerrar_doc()

class ArchivoRetimbre(Archivo_excel):
    """lee layout excel para el retimbre"""

    def __init__(self, ruta):
        self.ruta_archivo = ruta
        Archivo_excel.__init__(self, self.ruta_archivo)

    
    
    def leer(self):
        pass










