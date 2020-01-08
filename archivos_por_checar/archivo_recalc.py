


from archivo_excel import Archivo_excel

class Archivo_Recalculo(Archivo_excel):

    def __init__(self):
        """Trabaja con el Archivo
            de Recalculo del mes De los
            empleados de    BASE"""


        Archivo_excel.__init__(self,'R-RECALCULO')

        self.leer_titulos('BASE MUNICIPIO',1)
        self.obtener_claves_celdas('BASE MUNICIPIO')

        self.input()



    def input(self):
        self.periodo_in = int(input("Escribe el periodo: "))
        print(self.periodo_in)

    def extraer_recalculo_base(self):


        self.Recalculo_r = list()
        self.Recalculo_control = list ()

        hoja_lectura = self.hojas_nombres['BASE MUNICIPIO']


        columna = self.claves_columnas['PERIODO']
        fila_i       	= self.columnas_i['PERIODO']

        columna_recal = self.claves_columnas['IMPORTE RECALCULO CON REDONDEO']
        fila_i_recal       	= self.columnas_i['IMPORTE RECALCULO CON REDONDEO']

        columna_c = self.claves_columnas['No. CONTROL']
        fila_c     	= self.columnas_i['No. CONTROL']



        hoja = hoja_lectura
        titulos = hoja[columna]
        titulos_recalc = hoja[columna_recal]
        titulos_c = hoja[columna_c]




        for titulo, titulo_recalc, titulo_c in zip(range(fila_i, len(titulos)),
                                            range(fila_i_recal, len(titulos_recalc)),
                                            range(fila_c, len(titulos_c))):

            for celda,celda_recal in zip([titulos[titulo].value],
                             [titulos_recalc[titulo_recalc].value]):

                if self.periodo_in == celda:
                    self.Recalculo_r.append([titulos_recalc[titulo_recalc].value])
                    self.Recalculo_control.append([titulos_c[titulo_c].value])

                    print([titulos_c[titulo_c].value],"--",[titulos_recalc[titulo_recalc].value])
