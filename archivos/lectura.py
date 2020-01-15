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
        self.hoja = 0
        self.hoja_lectura = self.hojas_lista[self.hoja]        #Hoja de lectura                     

        self.leer_titulos(0, 2)

    def extraer_control(self):
        """Almacena el Numero de control del IQ"""


        self.control = list() 
       
        COLUMNA = self.claves_columnas['No. Control']    #Columna que lee
        FILA    = self.columnas_i['No. Control']         #Fila que omite la lectura
                
        titulos =  self.hoja_lectura[COLUMNA]

        for titulo in range(FILA, len(titulos)):       
             
            self.control.append([titulos[titulo].value])

      
        self.cerrar_doc()
    def extraer_ccn_1401(self):

        self.ccn_1401 = list() 
        titulo = '1401'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
           
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                
                self.ccn_1401.append([titulos[titulo].value])
        else:
            pass
    def extraer_ccn_1409(self):

        self.ccn_1409 = list() 
        titulo = '1409'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                
                self.ccn_1409.append([titulos[titulo].value])
        else:
            pass

    def extraer_ccn_2240(self):

        self.ccn_2240 = list() 
        titulo = '2240'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                
                self.ccn_2240.append([titulos[titulo].value])
        else:
            pass

    def extraer_ccn_2566(self):
        self.ccn_2566 = list() 
        titulo = '2566'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                
                self.ccn_2566.append([titulos[titulo].value])
        else:
            pass

        
    def extraer_ccn_481(self):

        self.ccn_481 = list() 
        titulo = '/481'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                
                self.ccn_481.append([titulos[titulo].value])
        else:
            pass


    def extraer_ccn_559(self):
        
        self.ccn_559 = list() 
        titulo = '/559'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                
                self.ccn_559.append([titulos[titulo].value])
        else:
            pass
    



class ArchivoRetimbre(Archivo_excel):
    """lee layout excel para el retimbre"""

    def __init__(self, ruta):
        self.ruta_archivo = ruta
        Archivo_excel.__init__(self, self.ruta_archivo)

    
    
    def leer(self):
        pass










