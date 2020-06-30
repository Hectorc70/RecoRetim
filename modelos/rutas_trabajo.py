import os
import os.path



class Rutas():

	def __init__(self, ruta):
		self.ruta_obtener_carpeta = ruta
		
	 
	def recuperar_rutas(self):
		"""Recupera las Rutas de los archivos que contienen los datos"""     

		self.archivos_excel = dict()
		

		for ruta, carpetas, documentos in os.walk(self.ruta_obtener_carpeta,topdown = True):                      
		  
			
			for documento in documentos:
			

				extencion_archivo = os.path.splitext(documento)

				if  extencion_archivo[-1] == '.xlsx':

					if (extencion_archivo[0].split("_")[0] == 'IQ' and
						extencion_archivo[0].split("_")[1] !='layout'):

						ruta_completa = ruta.replace("/", "\\") + "\\" + documento
						self.archivos_excel["IQ"] = ruta_completa

					elif extencion_archivo[0].split("_")[0] == "Layout":
						
						ruta_completa = ruta.replace("/", "\\") + "\\" + documento
						self.archivos_excel["TRABAJO"] = ruta_completa

					elif (extencion_archivo[0].split("_")[0] == "ReporteSAP" and
						extencion_archivo[0].split("_")[1] == "Base"):

						ruta_completa = ruta.replace("/", "\\") + "\\" + documento
						self.archivos_excel["REPORTE_SAP"] = ruta_completa

					elif (extencion_archivo[0].split("_")[0] == "ReporteTimbrado" and
						  extencion_archivo[0].split("_")[1] == "BASE"):

						ruta_completa = ruta.replace("/", "\\") + "\\" + documento
						self.archivos_excel["REPORTE_B1_TIM"] = ruta_completa
						

					elif (extencion_archivo[0].split("_")[0] == "ReporteTimbrado" and
						  extencion_archivo[0].split("_")[1] == "BASE4"):

						ruta_completa = ruta.replace("/", "\\") + "\\" + documento
						self.archivos_excel["REPORTE_B4_TIM"] = ruta_completa	

					elif extencion_archivo[0].split("_")[0] == "RECALCULO":
						ruta_completa = ruta.replace("/", "\\") + "\\" + documento
						self.archivos_excel["RECALCULO"] = ruta_completa	

					else:
						continue

						
		return self.archivos_excel
		
					

				   
	
	
	
	