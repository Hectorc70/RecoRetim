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
    
    def obtener_importes_txt(self):
        self.datos = dict()
        
        COLUMNA_CONTROL = self.claves_columnas['CONTROL']    #Columna que lee
        COLUMNA_NOM1 = self.claves_columnas['NOM1']    #Columna que lee
        COLUMNA_NOM4 = self.claves_columnas['NOM4']    #Columna que lee
        
        FILA    = self.columnas_i['CONTROL']         #Fila que omite la lectura
                
        titulo_control =  self.hoja_lectura[COLUMNA_CONTROL]
        titulo_nom1 =  self.hoja_lectura[COLUMNA_NOM1]
        titulo_nom4 =  self.hoja_lectura[COLUMNA_NOM4]

        for control, nom1, nom4 in zip(range(FILA, len(titulo_control)),
                                    range(FILA, len(titulo_nom1)),
                                    range(FILA, len(titulo_nom4))):

            control = [titulo_control[control].value]
            importe_nom1 = [titulo_nom1[nom1].value]
            importe_nom4 = [titulo_nom4[nom4].value]
          
            self.datos[control[0]] = [importe_nom1[0], importe_nom4[0]]

        return self.datos
   
 



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




class ReporteTimbrado(Archivo_excel):
    """lee layout excel para el retimbre"""

    def __init__(self, ruta):
        self.ruta_archivo = ruta
        Archivo_excel.__init__(self, self.ruta_archivo)

        self.hoja = 0
        self.hoja_lectura = self.hojas_lista[self.hoja]

        self.leer_titulos(self.hoja, 1)
    
    
    def obtener_uuid(self):
        self.uuid = dict()
        
        COLUMNA_CONTROL = self.claves_columnas['ARCHIVO']    #Columna que lee
        COLUMNA_UUID = self.claves_columnas['UUID']    #Columna que lee
        FILA    = self.columnas_i['ARCHIVO']         #Fila que omite la lectura
                
        colum_control =  self.hoja_lectura[COLUMNA_CONTROL]
        colum_uuid =  self.hoja_lectura[COLUMNA_UUID]

        for control, uuid in zip(range(FILA, len(colum_control)),range(FILA, len(colum_uuid))):
            nombre_archivo = [colum_control[control].value]
            control = int(nombre_archivo[0].split('_')[0])    
            uuid_celda    = [colum_uuid[uuid].value]

            self.uuid[str(control)] = uuid_celda[0]

        return self.uuid



#recalculo = ArchivoRecalculoBaseMun()
"""ruta = "C:\\Users\\Usuario\\Documents\\RETIMBRE\\2020\\archivos_entrada\\RECALCULO_202010.xlsx"
recalculo = ArchivoRecalculoBaseMun(ruta)
recalculo.extraer_importes()
"""

#IQ
"""ruta = "C:\\Users\\Usuario\\Documents\\RETIMBRE\\2020\\archivos_entrada\\IQ_202010_ORDINARIAv3.xlsx"
iq = ArchivoIQ(ruta)
iq.extraer_control() """
"""ruta = "C:\\Users\\Usuario\\Documents\\RETIMBRE\\2020\\archivos_entrada\\ReporteSAP_Base_202010.xlsx"
sap = ReporteSap(ruta)
sap.obtener_importes_txt()"""

ruta = "C:\\Users\\Usuario\\Documents\\RETIMBRE\\2020\\archivos_entrada\\ReporteTimbrado_BASE_102020.xlsx"
retim = ReporteTimbrado(ruta)
retim.obtener_uuid()