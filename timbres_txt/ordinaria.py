
import os
import os.path
from tkinter.filedialog import asksaveasfilename
from os.path import splitext

from timbres_txt.modelos.nomina import Nomina
from timbres_txt.modelos.nomina import Nomina4





class NominaOrdinariaBase(Nomina, Nomina4):

    def __init__(self, ruta):

        self.ruta_nominas = ruta

        Nomina.__init__(self, self.ruta_nominas)
        self.recuperar_timbres()
        self.recuperar_txt()

        Nomina4.__init__(self, self.ruta_nominas)
        self.recuperar_timbres_nom4()
        self.recuperar_txt_nom4()

    def validar(self):
        pass
        
    
        
