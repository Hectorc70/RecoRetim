from tkinter.filedialog import askdirectory

#from archivos.modelos.archivo_excel import Archivo_excel
from modelos.archivo_excel import Archivo_excel
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
    
   

    def obtener_datos_iq(self):
        """Almacena el Numero de empleado  del IQ con sus respectivo
        conceptos que se utilizan en el retimbrado"""


        self.datos_empleado = dict() 
       
        COLUMNA = self.claves_columnas['No. Control']    #Columna que lee
        FILA    = self.columnas_i['No. Control']         #Fila que omite la lectura
                
        titulos =  self.hoja_lectura[COLUMNA]

        for titulo in range(FILA, len(titulos)):            
            conceptos = self.extraer_conceptos(titulo)
            control = [titulos[titulo].value]
            self.datos_empleado[control[0]] = conceptos
        

        return self.control
      
        
    def extraer_conceptos(self, fila):      
        conceptos_conte = dict()
        conceptos = ['1401', '1409','2240', '2566',
                     '/481', '/559']

        fila_lectura = fila+1 
        for titulo in conceptos:
            if titulo in self.columnas_ccn and titulo in self.columnas_i_ccn:
            
                columna = self.columnas_ccn[titulo]    #Columna que lee               
                
                contenido_celda =  self.hoja_lectura[columna+str(fila_lectura)].value
                              
                if contenido_celda == None:
                        
                    conceptos_conte[titulo] = ''
                    continue
                else:                       
                   conceptos_conte[titulo] = contenido_celda               
               
            else:
                pass 

        return conceptos_conte



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



class ArchivoRecalculoBaseMun(Archivo_excel):
    """Lee el archivo de recalculo del periodo"""
    def __init__(self, ruta):
        self.ruta_archivo = ruta
        Archivo_excel.__init__(self, self.ruta_archivo)

        self.hoja = 0
        self.hoja_lectura = self.hojas_lista[self.hoja]

        self.leer_titulos(self.hoja, 1)

    def extraer_importes(self):
        self.datos = dict()
        
        COLUMNA_CONTROL = self.claves_columnas['CONTROL']    #Columna que lee
        COLUMNA_IMPORTE = self.claves_columnas['RECALCULO CON REDONDEO']    #Columna que lee
        
        FILA    = self.columnas_i['CONTROL']         #Fila que omite la lectura
                
        titulo_control =  self.hoja_lectura[COLUMNA_CONTROL]
        titulo_importe =  self.hoja_lectura[COLUMNA_IMPORTE]

        for control, importe in zip(range(FILA, len(titulo_control)),
                                    range(FILA, len(titulo_importe))):

            control = [titulo_control[control].value]
            importe = [titulo_importe[importe].value]
          
            self.datos[control[0]] = importe[0]

        return self.datos




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



#recalculo = ArchivoRecalculoBaseMun()
"""ruta = "C:\\Users\\Usuario\\Documents\\RETIMBRE\\2020\\archivos_entrada\\RECALCULO_202010.xlsx"
recalculo = ArchivoRecalculoBaseMun(ruta)
recalculo.extraer_importes()
"""

#IQ
""" ruta = "C:\\Users\\Usuario\\Documents\\RETIMBRE\\2020\\archivos_entrada\\IQ_202010_ORDINARIAv3.xlsx"
iq = ArchivoIQ(ruta)
iq.extraer_control() """

