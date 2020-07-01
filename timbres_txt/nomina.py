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

        self.rutas_timbres_ord   = dict()


        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:  

                extencion = os.path.splitext(archivo)
                if extencion[-1] == '.xml':
                    tipo_de_nomina    = ruta.split("\\")[5]                   

                    if tipo_de_nomina.split("_")[0] != 'BASE4':                    
                        ruta_completa = ruta + "\\" + archivo
                        control = int(archivo.split("_")[0])

                        self.rutas_timbres_ord[str(control)] = ruta_completa
        
        return self.rutas_timbres_ord
    


    def recuperar_txt(self):
        """Recupera archivos txt(CFDI) de la nomina"""

        self.rutas_cfdi_ord = dict()
        

        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:

                extencion = os.path.splitext(archivo)
                control = archivo.split("_")[0]
                if extencion[-1] == '.txt' and len(control) == 8:                    
                    tipo_de_nomina    = ruta.split("\\")[5] 

                    if tipo_de_nomina.split("_")[0] != 'BASE4':

                        ruta_completa = ruta + "\\" + archivo
                        numero_de_control = int(control)
                        self.rutas_cfdi_ord[str(numero_de_control)] = ruta_completa

        return self.rutas_cfdi_ord


class Nomina4():
    """NOMINA CON TICKET 4(APORTACION) """
    def __init__(self, ruta):
        self.ruta = ruta


    def recuperar_timbres_nom4(self):

        """Recupera archivos xml(TIMBRES de los CFDI) de la nomina4 de los
            empleados"""

        self.rutas_timbres4   = dict()      

        
        for ruta, carpetas, archivos in os.walk(self.ruta, topdown = True):  

            for archivo in archivos:               
                extencion = os.path.splitext(archivo)

                if extencion[-1] == '.xml':
                    carpeta_de_nomina = ruta.split("\\")[4]
                    tipo_de_nomina    = ruta.split("\\")[5]

                    if (carpeta_de_nomina.split("_")[0] == 'ORDINARIA' and
                        tipo_de_nomina.split("_")[0] == 'BASE4'):                   
                        ruta_completa = ruta + "\\" + archivo
                        control = int(archivo.split("_")[0])

                        
                        self.rutas_timbres4[str(control)] = ruta_completa
        
        return self.rutas_timbres4
    

    def recuperar_txt_nom4(self):
        """Recupera archivos txt(CFDI) de la nomina 4"""       

        self.rutas_cfdi4 = dict()
       



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
                        
                        self.rutas_cfdi4[control]  = ruta_completa

        return  self.rutas_cfdi4
