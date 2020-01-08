import os
from os.path import splitext


class CarpetaNomina():
    """CLASE que obtiene la ruta de cada nomina, debe seleccionarse la
        carpeta del periodo en que se va a recuperar"""

    def __init__(self, ruta):
        self.ruta_obtener_carpeta = ruta
        self.recuperar_rutas()
    

    def recuperar_rutas(self):
        """Recupera las carpeta de las nominas""" 

        self.carpetas_nom = dict()
       
        

        for ruta, carpetas, documentos in os.walk(self.ruta_obtener_carpeta,topdown = True):                      
          
            
            for tipo_de_nomina in carpetas:

                nomina_mayusc = tipo_de_nomina.upper()
                self.carpetas_nom[ nomina_mayusc] = ruta.replace("/", "\\") + "\\" + tipo_de_nomina

                
                

                

                

                    

    
    
              

                        




        


