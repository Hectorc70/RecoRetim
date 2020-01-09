import os.path as path


def crear_archivo_txt( datos):
    ruta_guardado = "C:\\Users\\USUARIO\\Desktop\\Pruebas_reco.txt"

    archivo =open(ruta_guardado, 'w')
    archivo.write(datos)
    archivo.close()
    
    #if path.exists(ruta_guardado):



