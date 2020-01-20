import os
from timbres_txt.ordinaria import NominaOrdinariaBase 


class CarpetaNomina():
    """CLASE que obtiene la ruta de cada nomina, debe seleccionarse la
        carpeta del periodo en que se va a recuperar"""

    def __init__(self, ruta):
        self.ruta_obtener_carpeta = ruta
        self.recuperar_nominas()


    def recuperar_nominas(self):
        """Recupera las carpeta de las nominas"""

        self.carpetas_nom = dict()



        for ruta, carpetas, documentos in os.walk(self.ruta_obtener_carpeta,topdown = True):


            for tipo_de_nomina in carpetas:
                ruta_completa_nomina = ruta.replace("/", "\\") + "\\" + tipo_de_nomina

                if tipo_de_nomina.split("_")[0] == "ORDINARIA":
                    nom_base = NominaOrdinariaBase(ruta_completa_nomina)



                nomina_mayusc = tipo_de_nomina.upper()
                self.carpetas_nom[nomina_mayusc] = ruta_completa_nomina

        return self.carpetas_nom
