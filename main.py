import os

from ui import *
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QThread

from ordinaria import NominaOrdinariaBase
from modelos.rutas_trabajo import Rutas
from archivos.lectura import ArchivoIQ, ReporteSap, ReporteTimbrado
from modelos.archivos_excel import ArchivoExcel



class ArchivoLayout():

	def __init__(self, ruta_archivos_trabajo):
		rutas              = Rutas(ruta_archivos_trabajo)
		self.rutas_trabajo = rutas.recuperar_rutas()

		self.excel = ArchivoExcel(self.rutas_trabajo['TRABAJO'])
		
   
	def escribir_layout(self, ruta_txt_xml, ruta_guardado):

		nom_ord 	 = NominaOrdinariaBase(ruta_txt_xml, )
		timbres_cfdi = nom_ord.depurar_archivos()
		
		for hoja_nombre, hoja_clave in  self.excel.hojas[0].items():
			if hoja_nombre == 'hoja trabajo':
				self.escribir_conceptos(hoja_nombre, hoja_clave)
				
			elif hoja_nombre == 'txt_sap':
				self.escribir_reporte_sap(hoja_nombre, hoja_clave)

			elif hoja_nombre == 'txt_n1':
				nom1_txt = timbres_cfdi["nom1_cfdi"]
				self.excel.escribir_en_hoja(nom1_txt, 0, hoja_clave)

			elif hoja_nombre == 'xml_n1':				
				retimbre_base1 = ReporteTimbrado(self.rutas_trabajo['REPORTE_B1_TIM'])
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

				nom4_xml = timbres_cfdi["nom4_timbres"]

				self.excel.escribir_en_hoja(nom4_xml, 0, hoja_clave)
				self.excel.escribir_en_hoja(uuid_base4, 3, hoja_clave)

				
		self.excel.guardar(ruta_guardado)

	def escribir_conceptos(self, hoja, clave_hoja): 

		titulos = self.excel.leer_titulos(hoja, 1)
		iq         = ArchivoIQ(self.rutas_trabajo['IQ'])                              
		iq_control = [iq.extraer_control()]
		conceptos    = iq.extraer_conceptos()


		

		Conceptos = [conceptos, conceptos, conceptos, conceptos, conceptos, conceptos]
		for titulo, numero_columna in titulos.items():

			if titulo == 'Control':
				self.excel.escribir_en_hoja(iq_control, numero_columna,
											 clave_hoja, 0)

			elif titulo == 'Recalculo':
				self.excel.escribir_en_hoja()
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

class EscribirLayout(QThread):
	def __init__(self, ruta, ruta_txt_xml, ruta_guardado):
		super().__init__()
		self.ruta = ruta
		self.ruta_txt_xml = ruta_txt_xml
		self.ruta_guardado = ruta_guardado


	def run(self):		
		archivo_retim = ArchivoLayout(self.ruta)
		archivo_retim.escribir_layout(self.ruta_txt_xml, self.ruta_guardado)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.ejecutar()


	def ejecutar(self):    

		self.btn_comenzar.clicked.connect(self.ejecutar_escritura)

	def ejecutar_escritura(self):
		ruta_trabajo = self.archivos_trab_ruta.text()
		ruta_txt_xml = self.rutas_archivos.text()
		nombre_excel = self.ruta_archivo_excel.text()
		extencion    = self.extencion_archivo.text()
		ruta_completa_excel = nombre_excel + extencion

		"""self.escribir = EscribirLayout(ruta_trabajo, 
											ruta_txt_xml, 
											ruta_completa_excel
										)

		self.escribir.finished.connect(self.del_ejecucion)
		self.escribir.start()"""

		archivo_retim = ArchivoLayout(ruta_trabajo)
		archivo_retim.escribir_layout(ruta_txt_xml, ruta_completa_excel)

	def del_ejecucion(self):	
		del self.escribir


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


		
