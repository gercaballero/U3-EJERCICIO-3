from classInscripcion import Inscripcion
from classPersona import Persona
import csv
class ColeccionInscripciones:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    
    def agregarInscripcion(self,inscripcion):
        if isinstance(inscripcion, Inscripcion):
            self.__lista.append(inscripcion)

    def consulta(self,dni):
        inscripcion=None
        i=0
        while inscripcion==None and i<len(self.__lista):
            if self.__lista[i].getDniPersona().upper()==dni.upper():
                inscripcion=self.__lista[i]
            else:
                i+=1
        return inscripcion
    def pago(self,dni):
        inscripcion=None
        i=0
        while inscripcion==None and i<len(self.__lista):
            if self.__lista[i].getDniPersona().upper()==dni.upper():
                inscripcion=self.__lista[i]
                inscripcion.registrarPago()
            else:
                i+=1
        return inscripcion

    def listar(self):
        for inscripcion in self.__lista:
            print('\n{}'.format(inscripcion))
    def crearArchivo(self):
        archivo=open('inscripciones.csv','w',newline='')
        writer=csv.writer(archivo,delimiter=',')
        for inscripcion in self.__lista:
            dato=[str(inscripcion.getDniPersona()),str(inscripcion.getNumeroTaller()),inscripcion.getFecha(),str(inscripcion.getPago())]
            writer.writerow(dato)
        archivo.close()