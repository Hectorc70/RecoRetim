import os
import os.path
from tkinter.filedialog import asksaveasfilename
from os.path import splitext
from nominas.ayuda.log import Log



class NominaOrdinaria():

    def __init__(self, ruta):
        self.ruta = ruta
        

    def recuperar_timbres(self):
        """Recupera archivos xml de la nomina"""

        self.rutas_timbres_ord = list()

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                extencion = os.path.splitext(archivo)

                if carpeta_de_nomina.split("_")[0] == 'ORDINARIA':

                    if extencion[-1] == '.xml':
                        self.rutas_timbres_ord.append(archivo)

    def crear_log(self):

        self.recuperar_timbres()

        
        hoja_activa = 0
        columna_inicial = 1
        fila = 1
        datos_lista = [self.rutas_timbres_ord]

        log = Log()
        log.escribir_titulo("Archivo", fila, hoja_activa)
        log.escribir_en_hoja(datos_lista, columna_inicial, hoja_activa)
        log.guardar_archivo_log(asksaveasfilename())

       
        print("Terminado")




    def recuperar_txt(self):
        pass

class NominaComplementaria(NominaOrdinaria):
    pass