'''
Created on 16/08/2013

@author: Lennin
'''
import psycopg2 # @UnresolvedImport
import sys
import random
import string
import os

from ConectorBD import ConexionBD

from Constantes import DIRECTORIO_TEMPORAL

def convertirImagen(img):
    return psycopg2.Binary(img)

def nombreAleatorio(N = 5):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(N))  # @UnusedVariable

def readImage(path):
    try:
        fin = open(path, "rb")
        img = fin.read()
        return img
    except IOError, e:
        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)
    finally:
        if fin:
            fin.close()

def writeImage(data,path=None):
    if path is None:
        # guardar la imagen en un directorio temporal
        path = os.path.realpath(os.path.join(DIRECTORIO_TEMPORAL ,nombreAleatorio() + ".jpg"))
        print(path)
    # guardar imagen en HDD y retornar nada
    try:
        fout = open(path,'wb')
        fout.write(data)
    except IOError, e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        if fout:
            fout.close()
    return path


def pruebaImagenes():
    path_prueba_lectura = os.path.realpath(os.path.join(DIRECTORIO_TEMPORAL ,"prueba.jpg"))

    SQL_prueba_insert = 'INSERT INTO imagenes("IMAGE") VALUES(%s);'
    SQL_prueba_select = 'SELECT "IMAGE" FROM imagenes ORDER BY "ID" DESC;'

    # PARTE INSERCION BD:
    Cnn = ConexionBD(SQL_prueba_insert,(convertirImagen(readImage(path_prueba_lectura)),))
    Cnn.ejecutar()

    # PARTE GUARDADO EN HDD DESDE BD
    Cnn = ConexionBD(SQL_prueba_select)
    img = Cnn.obtenerUno()[0]
    pth = writeImage(img)
    
    print("PATH LECTURA: " + path_prueba_lectura )
    
    print("PATH ESCRITURA: " + pth)
    # PRUEBA FINAL
    assert readImage(pth) == readImage(path_prueba_lectura)
    print("****** PRUEBA IMAGEN FINALIZADA SATISFACTORIAMENTE ******")


if __name__ == '__main__':
    pruebaImagenes()