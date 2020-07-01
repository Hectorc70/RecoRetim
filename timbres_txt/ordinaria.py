
import os

from timbres_txt.nomina import Nomina
from timbres_txt.nomina import Nomina4





class NominaOrdinariaBase(Nomina, Nomina4):

	def __init__(self, ruta):

		self.ruta_nominas = ruta

		
	def depurar_archivos(self):

		ruta_nomina = self.ruta_nominas.replace('/', '\\') + '\\' + 'ORDINARIA'

		nom1 = Nomina(ruta_nomina)

		nom1_timbres = nom1.recuperar_timbres()
		nom1_cfdi    = nom1.recuperar_txt()

		nom4 = Nomina4(ruta_nomina)
		nom4_timbres = nom4.recuperar_timbres_nom4()
		nom4_cfdi    = nom4.recuperar_txt_nom4()    

		
		""" self.archivos_nom["nom1_timbres"] = nom1_timbres
		self.archivos_nom["nom1_cfdi"]    = nom1_cfdi

		self.archivos_nom["nom4_timbres"] = nom4_timbres
		self.archivos_nom["nom4_cfdi"]    = nom4_cfdi  """

	

		
		

		""" if tipo_de_nomina.split("_")[0] == "ORDINARIA":

			nom1 = Nomina(ruta_completa_nomina)

			# obtener rutas de xml y txt
			nom1_timbres = nom1.recuperar_timbres()
			nom1_cfdi    = nom1.recuperar_txt()

			nom4 = Nomina4(ruta_completa_nomina)
			nom4_timbres = nom4.recuperar_timbres_nom4()
			nom4_cfdi    = nom4.recuperar_txt_nom4()       
 """
			
		#return self.archivos_nom
		
