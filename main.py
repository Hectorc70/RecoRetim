import os

from ui import *
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog, QTableView
from PyQt5.QtCore import QThread

from ordinaria import NominaOrdinariaBase
from modelos.rutas_trabajo import Rutas
from modelos.archivos_excel import ArchivoExcel



class ArchivoLayout():

	def __init__(self, ruta_archivos_trabajo):
		rutas              = Rutas(ruta_archivos_trabajo)
		self.rutas_trabajo = rutas.recuperar_rutas()

		self.excel = ArchivoExcel(self.rutas_trabajo['TRABAJO'])
		
	def comprobar_faltantes(self, ruta_txt_xml, ruta_guardado, anno, periodo):
		nom_ord 	 = NominaOrdinariaBase(ruta_txt_xml, self.rutas_trabajo)
		datos_para_retimbre = nom_ord.validar_empleados()

		if datos_para_retimbre['NO SE ENCONTRO']:

			return datos_para_retimbre['NO SE ENCONTRO']
			
		else:
			
			self.escribir_layout(ruta_txt_xml, ruta_guardado, datos_para_retimbre,  anno, periodo)
			return 'Correcto'

	def escribir_layout(self, ruta_txt_xml, ruta_guardado, datos, anno, periodo):
	
		
		for hoja_nombre, hoja_clave in  self.excel.hojas[0].items():
			if hoja_nombre == 'hoja trabajo':
				self.escribir_trabajo(hoja_nombre, hoja_clave, datos, anno, periodo)
				
			elif hoja_nombre == 'txt_sap':
				self.escribir_reporte_sap(hoja_nombre, hoja_clave)

			elif hoja_nombre == 'txt_n1':
				nom1_txt = datos["nom1_cfdi"]
				self.excel.escribir_en_hoja(nom1_txt, 0, hoja_clave)

			"""if hoja_nombre == 'xml_n1':				
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
				self.excel.escribir_en_hoja(uuid_base4, 3, hoja_clave)"""

				
		self.excel.guardar(ruta_guardado)

	def escribir_trabajo(self, hoja, clave_hoja, datos, anno, periodo): 

		titulos = self.excel.leer_titulos(hoja, 1)	

		""" 
		for titulo, numero_columna in titulos.items():

			if titulo == 'Control':
				self.excel.escribir_en_hoja(iq_control, numero_columna,
											 clave_hoja, 0)

			elif titulo == 'Recalculo':
				self.excel.escribir_en_hoja()
			elif titulo == 'UUID_NOM1':                 
				self.excel.escribir_en_hoja(Conceptos, numero_columna,
											 clave_hoja, 0)
			 """
			
						
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
		archivo_retim.comprobar_faltantes(self.ruta_txt_xml, self.ruta_guardado)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.ejecutar()
		
	def comprobar_rutas(self):
		ruta_trabajo = self.in_archivos_excel.text()
		ruta_txt_xml = self.in_xml_txt.text()
		ruta_guardado = self.in_guardado.text()	

		if ruta_trabajo != '' and ruta_txt_xml != '' and ruta_guardado != '':	
			return True
		else:
			return False	



	def ejecutar(self):    
		"""Ejecuta si se presiona un boton"""
		self.btn_start.clicked.connect(self.ejecutar_escritura)
		self.btn_excel.clicked.connect(self.mostrar_ruta_excel)
		self.btn_archivos.clicked.connect(self.mostrar_ruta_archivos)
		self.btn_guardar.clicked.connect(self.guardar)



	def ejecutar_escritura(self):
		"""Ejecuta el proceso principal"""
		rutas = self.comprobar_rutas()
		if rutas:
			ruta_trabajo = self.in_archivos_excel.text()
			ruta_txt_xml = self.in_xml_txt.text()
			ruta_guardado = self.in_guardado.text()				
			anno	= self.anno.value()
			periodo = self.periodo.value()

			"""self.escribir = EscribirLayout(ruta_trabajo, 
												ruta_txt_xml, 
												ruta_completa_excel
											)

			self.escribir.finished.connect(self.del_ejecucion)
			self.escribir.start()"""

			archivo_retim = ArchivoLayout(ruta_trabajo)
			datos = archivo_retim.comprobar_faltantes(ruta_txt_xml, ruta_guardado, anno, periodo)

			if datos!= 'correcto':				
				self.mostrar_mensaje_warning('AVISO', 'estos empleados no se encontraron')
				self.dibujar_en_tabla(datos)
		else:
			self.mostrar_mensaje_warning('AVISO', 'Seleccione todas las rutas necesarias')


	def del_ejecucion(self):	
		del self.escribir


	def mostrar_ruta_excel(self):
		ruta = self.abrir_directorio('SELECCIONA LA CARPETA CON LOS ARCHIVOS DE ENTRADA')

		self.in_archivos_excel.setText(ruta)
	
	def mostrar_ruta_archivos(self):
		ruta = self.abrir_directorio('SELECCIONA EL PERIODO DE XML Y TXT')

		self.in_xml_txt.setText(ruta)

	def guardar(self):
		""""Abre un explorador para guardar un archivo"""


		ruta = QFileDialog.getSaveFileName(self, 'Guardar como...')
		self.in_guardado.setText(ruta[0])
		
	def abrir_directorio(self, titulo):
		"""Abre un explorador para seleccionar una carpeta"""

		ruta_carpeta = QFileDialog.getExistingDirectory(self, titulo)

		return ruta_carpeta
	
	def mostrar_mensaje_warning(self,titulo, texto):
		QMessageBox.warning(self, titulo, texto)

	def dibujar_en_tabla(self, datos):
		for dato in datos:
			self.vista.addItem(dato)
		
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


		
