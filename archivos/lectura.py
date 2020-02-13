from tkinter.filedialog import askdirectory

from archivos.modelos.archivo_excel import Archivo_excel
#rom archivos.ayuda.rutas_trabajo import Rutas




#archivo = Rutas(askdirectory()) 
#rutas_lectura = archivo.recuperar_rutas()

class ArchivoIQ(Archivo_excel):
    "Extrae informacion del ARCHIVO IQ"

    def __init__(self, ruta_iq):

        self.ruta = ruta_iq
        Archivo_excel.__init__(self, self.ruta)
        self.hoja = 0
        self.hoja_lectura = self.hojas_lista[self.hoja]        #Hoja de lectura                     

        self.leer_titulos(self.hoja, 2)

    def extraer_control(self):
        """Almacena el Numero de control del IQ"""


        self.control = list() 
       
        COLUMNA = self.claves_columnas['No. Control']    #Columna que lee
        FILA    = self.columnas_i['No. Control']         #Fila que omite la lectura
                
        titulos =  self.hoja_lectura[COLUMNA]

        for titulo in range(FILA, len(titulos)):            
            
            control = [titulos[titulo].value]
            self.control.append(control[0])
        

        return self.control
      
        
    def extraer_ccn_1401(self):

        self.ccn_1401 = list() 
        titulo = '1401'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
           
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]
           
            for titulo in range(FILA, len(titulos)):   
                ccn_1401 = [titulos[titulo].value] 
                  
                if ccn_1401[0] == None:
                    self.ccn_1401.append("")
                    continue
                else:                       
                    self.ccn_1401.append(ccn_1401[0])
        else:
            pass

        return self.ccn_1401

    def extraer_ccn_1409(self):

        self.ccn_1409 = list() 
        titulo = '1409'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                ccn_1409 = [titulos[titulo].value]
                if ccn_1409[0] == None:
                    self.ccn_1409.append("")
                    continue
                else:
                    self.ccn_1409.append(ccn_1409[0])
        else:
            pass

        return self.ccn_1409

    def extraer_ccn_2240(self):

        self.ccn_2240 = list() 
        titulo = '2240'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                ccn_2240 = [titulos[titulo].value]
                if ccn_2240[0] == None:
                    self.ccn_2240.append("")
                    continue
                else:
                    self.ccn_2240.append(ccn_2240[0])
        else:
            pass


        return self.ccn_2240

    def extraer_ccn_2566(self):
        self.ccn_2566 = list() 
        titulo = '2566'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                ccn_2566 = [titulos[titulo].value]
                if ccn_2566[0] == None:
                    self.ccn_2566.append("")
                    continue
                else:
                    self.ccn_2566.append(ccn_2566[0])
        else:
            pass

        return self.ccn_2566

        
    def extraer_ccn_481(self):

        self.ccn_481 = list() 
        titulo = '/481'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                ccn_481 = [titulos[titulo].value]
                if ccn_481[0] == None:
                    self.ccn_481.append("")
                    continue
                else:
                    self.ccn_481.append(ccn_481[0])
        else:
            pass

        return self.ccn_481


    def extraer_ccn_559(self):
        
        self.ccn_559 = list() 
        titulo = '/559'

        if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
        
            COLUMNA = self.columnas_ccn[titulo]    #Columna que lee
            FILA    = self.columnas_i_ccn[titulo]         #Fila que omite la lectura
            
            titulos =  self.hoja_lectura[COLUMNA]

            for titulo in range(FILA, len(titulos)):       
                ccn_559 = [titulos[titulo].value]
                if ccn_559[0] == None:
                    self.ccn_559.append("")
                    continue
                else:
                    self.ccn_559.append(ccn_559[0])
        else:
            pass

        return self.ccn_559
    




class ReporteSap(Archivo_excel):

    def __init__(self, ruta):
        
        self.ruta = ruta
        Archivo_excel.__init__(self, self.ruta)

        self.hoja = 0
        self.hoja_lectura = self.hojas_lista[self.hoja]

        self.leer_titulos(self.hoja, 1)

    def obtener_control(self):

        self.control = list() 
       
        COLUMNA = self.claves_columnas['NO CONTROL']    #Columna que lee
        FILA    = self.columnas_i['NO CONTROL']         #Fila que omite la lectura
                
        titulos =  self.hoja_lectura[COLUMNA]

        for titulo in range(FILA, len(titulos)):       
            control = [titulos[titulo].value]
            self.control.append(control[0])

        return self.control


    def obtener_nom1(self):

        self.nom1 = list() 
       
        COLUMNA = self.claves_columnas['NOM1']    #Columna que lee
        FILA    = self.columnas_i['NOM1']         #Fila que omite la lectura
                
        titulos =  self.hoja_lectura[COLUMNA]

        for titulo in range(FILA, len(titulos)):       
            nom1 = [titulos[titulo].value]
            self.nom1.append(nom1[0])

        return self.nom1
    
    def obtener_nom4(self):

        self.nom4 = list() 
       
        COLUMNA = self.claves_columnas['NOM4']    #Columna que lee
        FILA    = self.columnas_i['NOM4']         #Fila que omite la lectura
                
        titulos =  self.hoja_lectura[COLUMNA]

        for titulo in range(FILA, len(titulos)):       
            nom4 = [titulos[titulo].value]
            self.nom4.append(nom4[0])

        return self.nom4










class ArchivoRetimbre(Archivo_excel):
    """lee layout excel para el retimbre"""

    def __init__(self, ruta):
        self.ruta_archivo = ruta
        Archivo_excel.__init__(self, self.ruta_archivo)

        self.hoja = 0
        self.hoja_lectura = self.hojas_lista[self.hoja]

        self.leer_titulos(self.hoja, 1)
    
    
    def obtener_uuid(self):
        self.uuid = list()
        
        COLUMNA = self.claves_columnas['UUID']    #Columna que lee
        FILA    = self.columnas_i['UUID']         #Fila que omite la lectura
                
        titulos =  self.hoja_lectura[COLUMNA]

        for titulo in range(FILA, len(titulos)):       
            uuid = [titulos[titulo].value]
            self.uuid.append(uuid[0])

        return self.uuid

   