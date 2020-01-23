
import os
import os.path
from tkinter.filedialog import asksaveasfilename
from os.path import splitext

from timbres_txt.modelos.nomina import Nomina
from timbres_txt.modelos.nomina import Nomina4





class NominaOrdinariaBase(Nomina, Nomina4):

    def __init__(self, ruta):

        self.ruta_nominas = ruta

        
    def recuperar(self):


        nom1_timbres = list()
        nom1_cfdi    = list()
        nom4_timbres = list()
        nom4_cfdi    = list()



        for ruta, carpetas, documentos in os.walk(self.ruta_nominas, topdown = True):

            for tipo_de_nomina in carpetas:
                    ruta_completa_nomina = ruta.replace("/", "\\") + "\\" + tipo_de_nomina

                    if tipo_de_nomina.split("_")[0] == "ORDINARIA":
                        
    
        
