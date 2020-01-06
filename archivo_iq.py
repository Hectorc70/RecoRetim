


from modelos.archivo_excel import Archivo_excel

class IQ(Archivo_excel):


	def __init__(self):
		Archivo_excel.__init__(self,'IQ')

		self.leer_titulos(0,2)
		self.obtener_claves_celdas(0)

		self.obtener_claves_celdas_ccn(0)
		self.hoja_lectura = self.hojas_lista[0]
		self.doc = self.documento_open

		#self.extraer_no_control()

	def extraer_no_control(self):
		"""Extrae no control del IQ"""


		self.no_control = list()


		columna_control = self.claves_columnas['No. Control']
		fila_i       	= self.columnas_i['No. Control']

		hoja = self.hoja_lectura
		titulos = hoja[columna_control]

		for titulo in range(fila_i,len(titulos)):
			#print([titulos[titulo].value])
			self.no_control.append([titulos[titulo].value])

		return self.no_control


	def extraer_ccn_1401(self):
		"""Almacena cantidades del columna
			de APORTACION SEGURIDAD """


		self.ccn_1401 = list()


		columna_ccn = self.columnas_ccn['1401']
		fila_i_ccn       	= self.columnas_i_ccn['1401']

		hoja = self.hoja_lectura
		titulos = hoja[columna_ccn]

		for titulo in range(fila_i_ccn,len(titulos)):
			self.ccn_1401.append([titulos[titulo].value])

		#print(self.ccn_1401[-1])


	def extraer_ccn_2240(self):
		"""Almacena cantidades del columna
			de IMPUESTO ORDINARIO """


		self.ccn_2240 = list()

		if '2240' in self.columnas_ccn:
			columna_ccn = self.columnas_ccn['2240']
			fila_i_ccn       	= self.columnas_i_ccn['2240']

			hoja = self.hoja_lectura
			titulos = hoja[columna_ccn]

			for titulo in range(fila_i_ccn,len(titulos)):
				self.ccn_2240.append([titulos[titulo].value])


		else:
			pass

		#print(self.ccn_2240)


	def extraer_ccn_2566(self):
		"""Almacena cantidades del columna
			de IMPUESTO EXTRAORDINARIO """


		self.ccn_2566 = list()

		if '2566' in self.columnas_ccn:

			columna_ccn = self.columnas_ccn['2566']
			fila_i_ccn       	= self.columnas_i_ccn['2566']

			hoja = self.hoja_lectura
			titulos = hoja[columna_ccn]

			for titulo in range(fila_i_ccn,len(titulos)):
				self.ccn_2566.append([titulos[titulo].value])
		else:
			pass

		#print(self.ccn_2566)





	def extraer_ccn_481(self):
		"""Almacena cantidades del columna
			de SUBSIDIO AL EMPLEO """


		self.ccn_481 = list()

		if '/481' in self.columnas_ccn:
			columna_ccn = self.columnas_ccn['/481']
			fila_i_ccn 	= self.columnas_i_ccn['/481']

			hoja    = self.hoja_lectura
			titulos = hoja[columna_ccn]

			for titulo in range(fila_i_ccn,len(titulos)):
				self.ccn_481.append([titulos[titulo].value])

		else:
			pass

		#print(self.ccn_481)




	def extraer_ccn_559(self):
		"""Almacena cantidades del columna
			de TRANSFERENCIA BANCARIA"""


		self.ccn_559 = list()


		columna_ccn = self.columnas_ccn['/559']
		fila_i_ccn       	= self.columnas_i_ccn['/559']

		hoja = self.hoja_lectura
		titulos = hoja[columna_ccn]

		for titulo in range(fila_i_ccn,len(titulos)):
			self.ccn_559.append([titulos[titulo].value])

		print(self.ccn_559)


	def ejecutar(self):
		pass
