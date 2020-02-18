from tkinter.filedialog import askdirectory, asksaveasfilename
import os

from timbres_txt.ordinaria import NominaOrdinariaBase
from modelos.rutas_trabajo import Rutas
from archivos.lectura import ArchivoIQ, ReporteSap, ArchivoRetimbre
from modelos.archivos_excel import ArchivoExcel



class ArchivoLayout():

	def __init__(self):
		rutas              = Rutas(askdirectory())
		self.rutas_trabajo = rutas.recuperar_rutas()

		self.excel = ArchivoExcel(self.rutas_trabajo['TRABAJO'])
		
   
	def escribir_layout(self):

		nom_ord 	 = NominaOrdinariaBase (askdirectory())
		timbres_cfdi = nom_ord.recuperar_nom()
		
		for hoja_nombre, hoja_clave in  self.excel.hojas[0].items():
			if hoja_nombre == 'hoja trabajo':
				self.escribir_conceptos(hoja_nombre, hoja_clave)
				
			elif hoja_nombre == 'txt_sap':
				self.escribir_reporte_sap(hoja_nombre, hoja_clave)

			elif hoja_nombre == 'txt_n1':
				nom1_txt = timbres_cfdi["nom1_cfdi"]
				self.excel.escribir_en_hoja(nom1_txt, 0, hoja_clave)

			elif hoja_nombre == 'xml_n1':				
				retimbre_base1 = ArchivoRetimbre(self.rutas_trabajo['REPORTE_B1_TIM'])
				uuid_base1     = [retimbre_base1.obtener_uuid()]

				nom1_xml = timbres_cfdi["nom1_timbres"]
				
				self.excel.escribir_en_hoja(nom1_xml, 0, hoja_clave)
				self.excel.escribir_en_hoja(uuid_base1, 3, hoja_clave)
			
			elif hoja_nombre == 'txt_n4':
				nom4_txt = timbres_cfdi["nom4_cfdi"]
				self.excel.escribir_en_hoja(nom4_txt, 0, hoja_clave)

			elif hoja_nombre == 'xml_n4':
				retimbre_base4 = ArchivoRetimbre(self.rutas_trabajo['REPORTE_B4_TIM'])
				uuid_base4     = [retimbre_base4.obtener_uuid()]

				nom4_xml = timbres_cfdi["nom4_cfdi"]

				self.excel.escribir_en_hoja(nom4_xml, 0, hoja_clave)
				self.excel.escribir_en_hoja(uuid_base4, 3, hoja_clave)


			

				

		guardar_archivo = asksaveasfilename (title = "Guardar Archivo Retimbrado",
											 filetypes = (("Libro Excel", "* .xlsx" ))) 
		self.excel.guardar(guardar_archivo)

	def escribir_conceptos(self, hoja, clave_hoja): 

		titulos = self.excel.leer_titulos(hoja, 1)
		iq         = ArchivoIQ(self.rutas_trabajo['IQ'])                              
		iq_control = [iq.extraer_control()]
		iq_1401    = iq.extraer_ccn_1401()
		iq_1409    = iq.extraer_ccn_1409()
		iq_2240    = iq.extraer_ccn_2240()
		iq_2566    = iq.extraer_ccn_2566()
		iq_481     = iq.extraer_ccn_481()
		iq_559     = iq.extraer_ccn_559()

		Conceptos = [iq_1401, iq_1409, iq_2240, iq_2566, iq_481, iq_559]
		for titulo, numero_columna in titulos.items():

			if titulo == 'Control':
				self.excel.escribir_en_hoja(iq_control, numero_columna,
											 clave_hoja, 0)
			elif titulo == 'UUID_NOM1':                 
				self.excel.escribir_en_hoja(Conceptos, numero_columna,
											 clave_hoja, 0)
		
			
					
		
		
	

	
	def escribir_reporte_sap(self, hoja, clave_hoja):      

		reportesap = ReporteSap(self.rutas_trabajo['REPORTE_SAP'])

		sap_control = reportesap.obtener_control()
		sap_nom1    = reportesap.obtener_nom1()
		sap_nom4    = reportesap.obtener_nom4()

		datos_sap = [sap_control, sap_nom1, sap_nom4]
		TITULOS = ["CONTROL", "NOM1", "NOM4"]

		self.excel.escribir_titulo(TITULOS, 1, clave_hoja)
		self.excel.escribir_en_hoja(datos_sap, 0, clave_hoja)

		



	def escribir_rutas_archivos(self, ruta_nominas):
		
		self.carpetas_nom = dict()
		


		


		for ruta, carpetas, documentos in os.walk(ruta_nominas, topdown = True):


			for tipo_de_nomina in carpetas:
				ruta_completa_nomina = ruta.replace("/", "\\") + "\\" + tipo_de_nomina

				if tipo_de_nomina.split("_")[0] == "ORDINARIA":
					
					

					

					#obtener uuid de los timbres
					

					
					self.archivos_nom["nom1_uuid"] = uuid_base1
					self.archivos_nom["nom4_uuid"] = uuid_base4

					#Escribe todas las rutas de los xml y cfdi
				
					


				elif tipo_de_nomina.split("_")[0] == "COMPLEMENTARIA":
					pass

				nomina_mayusc = tipo_de_nomina.upper()
				self.carpetas_nom[nomina_mayusc] = ruta_completa_nomina

		return self.carpetas_nom






		
			




		

	




layout = ArchivoLayout()
layout.escribir_layout()

