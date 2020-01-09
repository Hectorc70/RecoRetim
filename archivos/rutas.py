import os
import os.path



class Rutas():

    def __init__(self, ruta):
        self.ruta_obtener_carpeta = ruta
     
    def recuperar_rutas(self):
        """Recupera las Rutas de los archivos que contienen los datos"""     
    
        

        for ruta, carpetas, documentos in os.walk(self.ruta_obtener_carpeta,topdown = True):                      
          
            
            for documento in documentos:
            

                extencion_archivo = os.path.splitext(archivo)

                if  extencion_archivo[-1] == '.xlsx':
                    

                   
    
    
    
    