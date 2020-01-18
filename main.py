from tkinter.filedialog import askdirectory
import os

from timbres_txt.nomina import Nomina, Nomina4



class ArchivoLayout():

    def __init__(self):
        pass

    
    
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


                elif tipo_de_nomina.split("_")[0] == "COMPLEMENTARIA":
                    print("sdsdd")

                nomina_mayusc = tipo_de_nomina.upper()
                self.carpetas_nom[nomina_mayusc] = ruta_completa_nomina

        return self.carpetas_nom



        pass

    




layout = ArchivoLayout()
layout.escribir_rutas_archivos(askdirectory())