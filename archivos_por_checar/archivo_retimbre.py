




from archivo_iq import IQ
from modelos.archivo_excel import Archivo_excel



excel_l = Archivo_excel('layaout')

class Layaout_Retimbre(IQ, Archivo_excel):
    """Archivo donde se concentra toda la informacion
        recuperada"""

    def __init__(self):

        Archivo_excel.__init__(self,'')     
        IQ.__init__(self)





    def escribir_hoja_trabajo(self):
        #print(self.hojas_nombres)
        pass






















retimbre = Layaout_Retimbre()
retimbre.escribir_trabajo()
