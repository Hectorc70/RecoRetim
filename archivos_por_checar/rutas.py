
import os
import os.path


from tkinter import filedialog


class Rutas:
    def __init__(self, ruta):
          self.ruta = ruta

          self.recuperar_docs_trabajo()   
	



    def recuperar_docs_trabajo(self):         
          self.rutas = dict()
       

        for ruta, carpetas, documentos in os.walk(self.ruta):

            for archivo in documentos:
                rutas = ruta.replace("/","\\") + "\\" + archivo


                archivo_extencion = os.path.splitext(archivo)

                nombre_archivo            = archivo.split('_')[-1]


                if archivo_extencion == '.xlsx' or archivo_extencion == '.txt':

                    if (archivo.split('_')[0] == 'IQ' and
                        nombre_archivo.split('v')[0] == 'ORDINARIA'):

                         self.rutas['IQ'] = rutas

                    elif archivo.split('(')[0] == 'IQ_layaout':
                         self.rutas['layaout'] = rutas

                    elif (archivo.split('_')[0] == 'ReporteTXT' and
                         archivo.split('_')[1] == 'BASE' and
                         archivo_extencion == '.xlsx'):

                         self.rutas['SAP-EXCEL'] = rutas

                    elif (archivo.split('_')[0] == 'ReporteTXT' and
                         archivo.split('_')[1] == 'BASE' and
                         archivo_extencion == '.txt'):

                         self.rutas['SAP-TXT'] = rutas

                    elif (archivo.split('_')[0] == 'ReporteTimbrado' and
                         archivo.split('_')[1] == 'BASE'):
                         self.rutas['RT-BASE'] = rutas

                    elif (archivo.split('_')[0] == 'ReporteTimbrado' and
                         archivo.split('_')[1] == 'BASE4'):
                         self.rutas['RT-BASE4'] = rutas

                    elif archivo.split('_')[0] == 'Recalculo':
                         self.rutas['R-RECALCULO'] = rutas

          return self.rutas




        
