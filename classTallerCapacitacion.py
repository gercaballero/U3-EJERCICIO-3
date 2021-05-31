from classInscripcion import Inscripcion
from manejadorInscripciones import ColeccionInscripciones
from manejadorPersonas import ColeccionPersonas

class TallerCapacitacion:
    __idTaller=0
    __nombre=''
    __vacantes=0
    __montoInscripcion=0
    __inscripciones=[]

    def __init__(self,id,nombre,vacantes,monto):
        self.__idTaller=id
        self.__nombre=nombre
        self.__vacantes=vacantes
        self.__montoInscripcion=monto
        self.__inscripciones=[]
    
    def agregarInscripcion(self,inscripcion):
        self.__inscripciones.append(inscripcion)

    def inscripcion(self,persona):
        fecha=input('\tINGRESE LA FECHA DE INSCRIPCION formato(dd/mm/aaaa): ')
        inscripcion=Inscripcion(fecha,persona,self)
        self.agregarInscripcion(inscripcion)
        return inscripcion
    
    def retornaInscripcion(self,dni):
        inscripcion=None
        i=0
        while inscripcion==None and i<len(self.__inscripciones):
            if self.__inscripciones[i].getDniPersona().upper()==dni.upper():
                inscripcion=self.__inscripciones[i]
            else:
                i+=1
        return inscripcion
    def listarInscriptos(self):
        if len(self.__inscripciones)>0:
            for inscripcion in self.__inscripciones:
                inscripcion.mostrar()
        elif len(self.__inscripciones)==0:
            print('¬¬¬¬¬EL TALLER NO TIENE NINGUN INSCRIPTO¬¬¬¬¬')

    ## GETS

    def getId(self):
            return int(self.__idTaller)
    def getMonto(self):
        return int(self.__montoInscripcion)