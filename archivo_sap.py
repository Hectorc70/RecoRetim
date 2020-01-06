



#from rutas import Rutas


class Archivo_SAP:


    def __init__(self):
        """Trabaja con el Archivo txt de SAP de los
            CFDI de BASE Y BASE4"""


        self.ruta = "C:/Users/USUARIO/Documents/RETIMBRE-2019/RECOP_DATOS_RETIMBRE/ARCHIVOS_IN/ReporteTXT_BASE_201918.txt"
        self.abrir = open(self.ruta, 'r')

        


    def leer_txt(self):
        lista_conte = list()

        leer = self.abrir.readlines()

        for linea in leer:
            lista_conte.append(linea)

        
                

        for datos in lista_conte:
            
            print(datos.split('|'))




        


sap = Archivo_SAP()


sap.leer_txt()
