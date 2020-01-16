import os
import os.path
from tkinter.filedialog import asksaveasfilename
from os.path import splitext

from timbres_txt.ayuda.log import Log



class Nomina:    
    """NOMINA con ticket 1"""

    def __init__(self, ruta):
        self.ruta = ruta
        

    def recuperar_timbres(self):
        """Recupera archivos xml(TIMBRES de los CFDI) de la nomina"""

        self.rutas_timbres_ord = list()

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                tipo_de_nomina    = ruta.split("\\")[4] 
                extencion = os.path.splitext(archivo)

                if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                    tipo_de_nomina.split("_")[0] == 'BASE'):

                    if extencion[-1] == '.xml':
                        ruta_completa = ruta + "\\" + archivo
                        self.control_nom1 = lambda 
                        self.rutas_timbres_ord.append(ruta_completa)
    


    def recuperar_txt(self):
        """Recupera archivos txt(CFDI) de la nomina"""

        self.rutas_cfdi_ord = list()

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                tipo_de_nomina    = ruta.split("\\")[4] 
                extencion = os.path.splitext(archivo)

                if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                    tipo_de_nomina.split("_")[0] == 'BASE'):

                    if extencion[-1] == '.txt':
                        ruta_completa = ruta + "\\" + archivo
                        self.rutas_cfdi_ord.append(ruta_completa)





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



class Nomina4():
    """NOMINA CON TICKET 4(APORTACION) """
    def __init__(self, ruta):
        self.ruta = ruta


    def recuperar_timbres_nom4(self):

        """Recupera archivos xml(TIMBRES de los CFDI) de la nomina4 de los
            empleados"""

        self.rutas_timbres4 = list()

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                tipo_de_nomina    = ruta.split("\\")[4]
                extencion = os.path.splitext(archivo)

                if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                    tipo_de_nomina.split("_")[0] == 'BASE4'):

                    if extencion[-1] == '.xml':
                        ruta_completa = ruta + "\\" + archivo
                        self.rutas_timbres4.append(ruta_completa)
    

    def recuperar_txt_nom4(self):
        """Recupera archivos txt(CFDI) de la nomina 4"""       

        self.rutas_cfdi4 = list()



        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                tipo_de_nomina    = ruta.split("\\")[4] 
                extencion = os.path.splitext(archivo)

                if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                    tipo_de_nomina.split("_")[0] == 'BASE4'):

                    if extencion[-1] == '.txt':
                        ruta_completa = ruta + "\\" + archivo
                        self.rutas_cfdi4.append(ruta_completa)

class NominaConfianza():
    """NOMINA DE CONFIANZA TICKET 5"""


    def __init__(self, ruta):
        self.ruta = ruta


    def recuperar_timbres_nom5(self):

        """Recupera archivos xml(TIMBRES de los CFDI) de la nomina 5(confianza)
           de los empleados"""

        self.rutas_timbres5 = list()

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                tipo_de_nomina    = ruta.split("\\")[4]
                extencion = os.path.splitext(archivo)

                if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                    tipo_de_nomina.split("_")[0] == 'CONFIANZA'):

                    if extencion[-1] == '.xml':
                        ruta_completa = ruta + "\\" + archivo
                        self.rutas_timbres5.append(ruta_completa)
    

    def recuperar_txt_nom5(self):
        """Recupera archivos txt(CFDI) de la nomina de confianza"""       

        self.rutas_cfdi5 = list()



        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                carpeta_de_nomina = ruta.split("\\")[3]
                tipo_de_nomina    = ruta.split("\\")[4] 
                extencion = os.path.splitext(archivo)

                if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                    tipo_de_nomina.split("_")[0] == 'CONFIANZA'):

                    if extencion[-1] == '.txt':
                        ruta_completa = ruta + "\\" + archivo
                        self.rutas_cfdi5.append(ruta_completa)


