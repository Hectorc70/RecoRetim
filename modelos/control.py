from rutas import Rutas, unir_cadenas


class EmpleadoRecalculo:

    def __init__(self, numero, periodo):
        self.numero = numero
        self.ruta_periodo = periodo

        self.ruta = Rutas()
        
    
    def buscar_empleado(self):        

        rutas = self.ruta.recuperar_rutas(self.ruta_periodo, True)       

        for ruta in rutas:                 
            extencion = ruta[-1].split('_')[-1].split('.')[-1]

            if extencion == 'xml' or extencion == '.txt':
                control = int(ruta[-1].split('_')[0])             
                nomina  =  ruta[4]
                
                if control == self.numero:
                    ruta_unida = unir_cadenas('\\',ruta[:-2])
                    return ruta
                    break
                


""" empleado = EmpleadoRecalculo(318212, 'Y:\\CFDI_2020\\CFDI_NOMINA_2020\\10_2020')
empleado.buscar_empleado() """
