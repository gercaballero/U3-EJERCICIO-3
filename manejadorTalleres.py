import numpy as np
import csv
from classTallerCapacitacion import TallerCapacitacion
class ManejadorTalleres:
    __arreglo=None
    __dimension=0
    __indice=0
    __carga=False

    def __init__(self):
        self.__arreglo=None
        self.__dimension=0
        self.__indice=0
        self.__carga=False

    def agregarTaller(self,taller):
        if isinstance(taller, TallerCapacitacion):
         if self.__indice==self.__dimension:
             print('ARREGLO NO PERMITE MAS TALLERES')
         else:
             self.__arreglo[self.__indice]=taller
             self.__indice+=1
    def cargarArchivo(self):
        if not self.__carga:
            self.test()
            self.__carga=True
            print('~~~~CARGA TALLERES REALIZADA~~~')
        else:
            print('LOS TALLERES YA ESTAN CARGADOS')
    def test(self):
        archivo=open('Talleres.csv')
        reader=csv.reader(archivo,delimiter=';')
        band=True
        for fila in reader:
            if band:
                self.__dimension=int(fila[0])
                self.__arreglo=np.empty(self.__dimension,dtype=TallerCapacitacion)
                band=False
            else:
                id=fila[0]
                nombre=fila[1]
                vacantes=fila[2]
                monto=fila[3]
                taller=TallerCapacitacion(id, nombre, vacantes, monto)
                self.agregarTaller(taller)
        archivo.close()
    
    def inscripcion(self,persona,numTaller):
        inscripcion=None
        i=0
        while inscripcion==None and i<self.__dimension:
            if self.__arreglo[i].getId()==numTaller:
                inscripcion=self.__arreglo[i].inscripcion(persona)
            else:
                i+=1
        return inscripcion
    
    def InscriptosTaller(self,taller):
        band=False
        i=0
        while not band and i<self.__dimension:
            if self.__arreglo[i].getId()==taller:
                self.__arreglo[i].listarInscriptos()
                band=True
            else:
                i+=1
        return band

