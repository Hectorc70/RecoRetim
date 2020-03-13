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

        self.rutas_timbres_ord   = list()
        self.control_timbres_ord = list()
        self.timbres_nom1        = []

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:  

                extencion = os.path.splitext(archivo)
                if extencion[-1] == '.xml':
                    carpeta_de_nomina = ruta.split("\\")[4]
                    tipo_de_nomina    = ruta.split("\\")[5]                   

                    if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                        tipo_de_nomina.split("_")[0] == 'BASE'):                    
                        ruta_completa = ruta + "\\" + archivo
                        control = archivo.split("_")[0]

                        self.control_timbres_ord.append(int(control))
                        self.rutas_timbres_ord.append(ruta_completa)
        
        return [self.control_timbres_ord, self.rutas_timbres_ord]
    


    def recuperar_txt(self):
        """Recupera archivos txt(CFDI) de la nomina"""

        self.rutas_cfdi_ord = list()
        self.control_cfdi_ord = list()


        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                extencion = os.path.splitext(archivo)
                control = archivo.split("_")[0]
                if extencion[-1] == '.txt' and len(control) == 8:

                    carpeta_de_nomina = ruta.split("\\")[4]
                    tipo_de_nomina    = ruta.split("\\")[5] 

                    if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                        tipo_de_nomina.split("_")[0] == 'BASE'):
                        
                        ruta_completa = ruta + "\\" + archivo
                        self.control_cfdi_ord.append(int(control))
                        self.rutas_cfdi_ord.append(ruta_completa)

        return [self.control_cfdi_ord, self.rutas_cfdi_ord]


class Nomina4():
    """NOMINA CON TICKET 4(APORTACION) """
    def __init__(self, ruta):
        self.ruta = ruta


    def recuperar_timbres_nom4(self):

        """Recupera archivos xml(TIMBRES de los CFDI) de la nomina4 de los
            empleados"""

        self.rutas_timbres4   = list()
        self.control_timbres4 = list()

        
        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:               
                extencion = os.path.splitext(archivo)

                if extencion[-1] == '.xml':
                    carpeta_de_nomina = ruta.split("\\")[4]
                    tipo_de_nomina    = ruta.split("\\")[5]

                    if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                        tipo_de_nomina.split("_")[0] == 'BASE4'):                   
                        ruta_completa = ruta + "\\" + archivo
                        control = archivo.split("_")[0]

                        self.control_timbres4.append(int(control))
                        self.rutas_timbres4.append(ruta_completa)
        
        return [self.control_timbres4, self.rutas_timbres4]
    

    def recuperar_txt_nom4(self):
        """Recupera archivos txt(CFDI) de la nomina 4"""       

        self.rutas_cfdi4 = list()
        self.control_cfdi4 = list()



        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                extencion = os.path.splitext(archivo)
                control = archivo.split("_")[0]

                if extencion[-1] == '.txt' and len(control) == 8:
                    carpeta_de_nomina = ruta.split("\\")[4]
                    tipo_de_nomina    = ruta.split("\\")[5] 

                    if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                        tipo_de_nomina.split("_")[0] == 'BASE4'):                    
                    
                        ruta_completa = ruta + "\\" + archivo
                        self.control_cfdi4.append(int(control))
                        self.rutas_cfdi4.append(ruta_completa)

        return [self.control_cfdi4, self.rutas_cfdi4]

class NominaConfianza():
    """NOMINA DE CONFIANZA TICKET 5"""


    def __init__(self, ruta):
        self.ruta = ruta


    def recuperar_timbres_nom5(self):

        """Recupera archivos xml(TIMBRES de los CFDI) de la nomina 5(confianza)
           de los empleados"""

        self.rutas_timbres5 = list()
        self.control_timbres5 = list()

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:
               
                extencion = os.path.splitext(archivo)
                if extencion[-1] == '.xml':
                    carpeta_de_nomina = ruta.split("\\")[4]
                    tipo_de_nomina    = ruta.split("\\")[5]

                if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                    tipo_de_nomina.split("_")[0] == 'CONFIANZA'):                    
                        ruta_completa = ruta + "\\" + archivo
                        control = archivo.split("_")[0]

                        self.control_timbres5.append(int(control))
                        self.rutas_timbres5.append(ruta_completa)

        return [self.control_timbres5, self.rutas_timbres5]
    

    def recuperar_txt_nom5(self):
        """Recupera archivos txt(CFDI) de la nomina de confianza"""       

        self.rutas_cfdi5 = list()
        self.control_cfdi5 = list()


        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                extencion = os.path.splitext(archivo)
                control = archivo.split("_")[0]
                if extencion[-1] == '.txt' and len(control) == 8:
                    carpeta_de_nomina = ruta.split("\\")[4]
                    tipo_de_nomina    = ruta.split("\\")[5] 

                    if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                        tipo_de_nomina.split("_")[0] == 'CONFIANZA'):                   
                        ruta_completa = ruta + "\\" + archivo
                        self.control_cfdi5.append(int(control))
                        self.rutas_cfdi5.append(ruta_completa)

        return [self.control_cfdi5, self.rutas_cfdi5]


