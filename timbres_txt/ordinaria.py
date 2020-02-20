
import os

from timbres_txt.nomina import Nomina
from timbres_txt.nomina import Nomina4





class NominaOrdinariaBase(Nomina, Nomina4):

	def __init__(self, ruta):

		self.ruta_nominas = ruta

		
	def recuperar_nom(self):

		self.archivos_nom = dict()

		for ruta, carpetas, documentos in os.walk(self.ruta_nominas, topdown = True):

			for tipo_de_nomina in carpetas:
				ruta_completa_nomina = ruta.replace("/", "\\") + "\\" + tipo_de_nomina

				if tipo_de_nomina.split("_")[0] == "ORDINARIA":

					nom1 = Nomina(ruta_completa_nomina)

					# obtener rutas de xml y txt
					nom1_timbres = nom1.recuperar_timbres()
					nom1_cfdi    = nom1.recuperar_txt()

					nom4 = Nomina4(ruta_completa_nomina)
					nom4_timbres = nom4.recuperar_timbres_nom4()
					nom4_cfdi    = nom4.recuperar_txt_nom4()       

					self.archivos_nom["nom1_timbres"] = nom1_timbres
					self.archivos_nom["nom1_cfdi"]    = nom1_cfdi

					self.archivos_nom["nom4_timbres"] = nom4_timbres
					self.archivos_nom["nom4_cfdi"]    = nom4_cfdi
				
				nomina_complementaria = NominaComplementaria()
						
					




							

		return self.archivos_nom
			
class NominaComplementaria(NominaOrdinariaBase):

	

	def recuperar_nom(self):
		
		

		for ruta, carpetas, documentos in os.walk(self.ruta_nominas, topdown = True):

			for tipo_de_nomina in carpetas:
				ruta_completa_nomina = ruta.replace("/", "\\") + "\\" + tipo_de_nomina

				if tipo_de_nomina.split("_")[0] == "COMPLEMENTARIA":

					nom_comple1 = Nomina(ruta_completa_nomina)
					nom1_timbres = nom_comple1.recuperar_timbres()
					nom1_cfdi    = nom_comple1.recuperar_txt()

					nom_comple4 = Nomina4(ruta_completa_nomina)
					nom4_timbres = nom_comple4.recuperar_timbres_nom4()
					nom4_cfdi    = nom_comple4.recuperar_txt_nom4()  

					
					self.archivos_nom["nom1_timbres"] = nom1_timbres
					self.archivos_nom["nom1_cfdi"]    = nom1_cfdi

					self.archivos_nom["nom4_timbres"] = nom4_timbres
					self.archivos_nom["nom4_cfdi"]    = nom4_cfdi
				
				else:
					continue