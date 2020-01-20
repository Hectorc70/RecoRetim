from tkinter.filedialog import askdirectory, asksaveasfile
import os

from timbres_txt.nomina import Nomina, Nomina4
from modelos.log import Log
from modelos.rutas_trabajo import Rutas


class ArchivoLayout():

    def __init__(self):
        rutas               = Rutas(askdirectory())
        self.archivo_excel = rutas.recuperar_rutas()

    
    
    def escribir_conceptos(self):
        pass

    
    def escribir_reporte_sap(self):
        pass


    def escribir_rutas_archivos(self, ruta_nominas):
        self.carpetas_nom = dict()



        for ruta, carpetas, documentos in os.walk(ruta_nominas, topdown = True):


            for tipo_de_nomina in carpetas:
                ruta_completa_nomina = ruta.replace("/", "\\") + "\\" + tipo_de_nomina

                if tipo_de_nomina.split("_")[0] == "ORDINARIA":
                    
                    nom1 = Nomina(ruta_completa_nomina)
                    nom1_timbres = nom1.recuperar_timbres()
                    nom1_cfdi    = nom1.recuperar_txt()
                    nom4 = Nomina4(ruta_completa_nomina)
                    nom4_timbres = nom4.recuperar_timbres_nom4()
                    nom4_cfdi    = nom4.recuperar_txt_nom4()

                    log = Log(self.archivo_excel['TRABAJO'])
                    #Escribe todas las rutas de los xml y cfdi
                    log.escribir_en_hoja(nom1_cfdi, 1, 4)
                    log.escribir_en_hoja(nom1_timbres, 1, 5)
                    log.escribir_en_hoja(nom4_cfdi, 1, 6)
                    log.escribir_en_hoja(nom4_timbres, 1, 7)
                    
                    log.guardar_archivo_log(asksaveasfile())


                elif tipo_de_nomina.split("_")[0] == "COMPLEMENTARIA":
                    pass

                nomina_mayusc = tipo_de_nomina.upper()
                self.carpetas_nom[nomina_mayusc] = ruta_completa_nomina

        return self.carpetas_nom



        

    




layout = ArchivoLayout()
layout.escribir_rutas_archivos(askdirectory())