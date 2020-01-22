from tkinter.filedialog import askdirectory, asksaveasfilename
import os

from timbres_txt.nomina import Nomina, Nomina4
from modelos.log import Log
from modelos.rutas_trabajo import Rutas
from archivos.lectura import ArchivoIQ
from modelos.archivos_excel import ArchivoExcel



class ArchivoLayout():

    def __init__(self):
        rutas               = Rutas(askdirectory())
        self.rutas_trabajo = rutas.recuperar_rutas()

        self.excel = ArchivoExcel(self.rutas_trabajo['TRABAJO'])
        
   
    def escribir_layout (self):
       for hoja_nombre, hoja_clave in  self.excel.hojas[0].items():
           
            if hoja_nombre == 'hoja trabajo':
               self.escribir_conceptos(hoja_nombre, hoja_clave)


            elif hoja_nombre == '':
                pass

    def escribir_conceptos(self, hoja, clave_hoja): 

        titulos = self.excel.leer_titulos(hoja, 1)
        iq         = ArchivoIQ(self.rutas_trabajo['IQ'])


        for titulo, clave_columna in titulos.items():
            if titulo == 'Control':                
                iq_control = [iq.extraer_control()]
                self.excel.escribir_en_hoja(iq_control, clave_columna,
                                             clave_hoja)

                self.excel.guardar(asksaveasfilename())
            
                    
        
        iq_1401    = iq.extraer_ccn_1401()
        iq_1409    = iq.extraer_ccn_1409()
        iq_2240    = iq.extraer_ccn_2240()
        iq_2566    = iq.extraer_ccn_2566()
        iq_481     = iq.extraer_ccn_481()
        iq_559     = iq.extraer_ccn_559()

    

    
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

                    
                    #Escribe todas las rutas de los xml y cfdi
                    self.log.escribir_en_hoja(nom1_cfdi, 1, 4)
                    self.log.escribir_en_hoja(nom1_timbres, 1, 5)
                    self.log.escribir_en_hoja(nom4_cfdi, 1, 6)
                    self.log.escribir_en_hoja(nom4_timbres, 1, 7)
                    
                    self.log.guardar_archivo_log(asksaveasfile())


                elif tipo_de_nomina.split("_")[0] == "COMPLEMENTARIA":
                    pass

                nomina_mayusc = tipo_de_nomina.upper()
                self.carpetas_nom[nomina_mayusc] = ruta_completa_nomina

        return self.carpetas_nom



        

    




layout = ArchivoLayout()
layout.escribir_layout()
#layout.escribir_conceptos()
#layout.escribir_rutas_archivos(askdirectory())