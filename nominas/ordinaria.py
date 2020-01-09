import os
import os.path
from tkinter.filedialog import asksaveasfilename

from os.path import splitext
from nominas.ayuda.archivo_txt import crear_archivo_txt



class NominaOrdinaria:

    def __init__(self, ruta):
        self.ruta = ruta
        self.recuperar_timbres()

    def recuperar_timbres(self):
        """Recupera archivos xml de la nomina"""

        self.rutas_timbres_ord = 

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                extencion = os.path.splitext(archivo)

                if carpeta_de_nomina.split("_")[0] == 'ORDINARIA':
                    if extencion[-1] == '.xml':
                        
        print("Terminado")




    def recuperar_txt(self):
        pass

class NominaComplementaria(NominaOrdinaria):
    pass