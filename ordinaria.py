
import os

from timbres_txt.nomina import Nomina
from timbres_txt.nomina import Nomina4

from archivos.lectura import ArchivoIQ, ReporteSap, ReporteTimbrado, ArchivoRecalculoBaseMun




class NominaOrdinariaBase(Nomina, Nomina4):

	def __init__(self, ruta, rutas_archivos):

		self.ruta_nominas = ruta
		self.ruta_iq = rutas_archivos["IQ"]
		self.ruta_recalculo = rutas_archivos["RECALCULO"]
		self.ruta_sap = rutas_archivos["REPORTE_SAP"]
		self.ruta_tim = rutas_archivos["REPORTE_B1_TIM"]
		self.ruta_tim4 = rutas_archivos["REPORTE_B4_TIM"]
		
		self.recalculo = ArchivoRecalculoBaseMun(self.ruta_recalculo)
		self.iq = ArchivoIQ(self.ruta_iq) 
		self.sap = ReporteSap(self.ruta_sap)
		self.timbrado = ReporteTimbrado(self.ruta_tim)
		self.timbrado_nom4 = ReporteTimbrado(self.ruta_tim4)

		
	def depurar_archivos(self):
		archivos = dict()
		ruta_nomina = self.ruta_nominas.replace('/', '\\') + '\\' + 'ORDINARIA'

		nom1 = Nomina(ruta_nomina)

		nom1_timbres = nom1.recuperar_timbres()
		nom1_cfdi    = nom1.recuperar_txt()

		nom4 = Nomina4(ruta_nomina)
		nom4_timbres = nom4.recuperar_timbres_nom4()
		nom4_cfdi    = nom4.recuperar_txt_nom4()    

		archivos['txt_nom1'] = nom1_cfdi
		archivos['xml_nom1'] = nom1_timbres

		archivos['txt_nom4'] = nom4_cfdi
		archivos['xml_nom4'] = nom4_timbres

		return archivos
		
	def validar_empleados(self):	
		"""Solo deja los datos de los empleados que 
		estan en el archivo de recalculo"""	
	
		para_retimbre = dict()

		archivos = self.depurar_archivos()

		importes_recalculo = self.recalculo.extraer_importes()
		empleados_iq = self.iq.obtener_datos_iq()
		sap_importes = self.sap.obtener_importes_txt()
		uuid_nom1    = self.timbrado.obtener_uuid()
		uuid_nom4    = self.timbrado_nom4.obtener_uuid()

		for empleado, recalculo in importes_recalculo.items():
			
			if (empleado in empleados_iq and empleado in sap_importes,
				empleado in uuid_nom1 and empleado in uuid_nom4):

				datos = [empleados_iq[empleado], sap_importes[empleado],
						uuid_nom1[empleado], uuid_nom4[empleado]]
			
				para_retimbre[empleado] = datos
			
			else:
				para_retimbre['NO SE ENCONTRO'] = empleado
				continue
					
		return para_retimbre



