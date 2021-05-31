from classPersona import Persona
class Inscripcion:
    __fechaInscripcion=''
    __pago=None
    __persona=None
    __taller=None

    def __init__(self,fecha,persona,taller):
        self.__fechaInscripcion=fecha
        self.__pago=False
        self.__persona=persona
        self.__taller=taller
    
    def __str__(self):
        pago=''
        if self.__pago:
            pago='SI'
        elif self.__pago==False:
            pago='NO'
        return ('FECHA:{}\tNOMBRE:{}\tTALLER:{}\tPAGO:{}'.format(self.__fechaInscripcion,self.__persona.getNombre(),self.__taller.getId(),pago))

    def registrarPago(self):
        self.__pago=True

    def mostrar(self):
        pago=''
        if self.__pago:
            pago='SI'
        elif self.__pago==False:
            pago='NO'
        print('NOMBRE:{:20}\tDNI:{:10}\tPAGO:{}'.format(self.__persona.getNombre(),self.__persona.getDni(),pago))
    
    def getDniPersona(self):
        return str(self.__persona.getDni())
    
    def getNumeroTaller(self):
        return int(self.__taller.getId())
    def getPago(self):
        return bool(self.__pago)
    def deuda(self):
        retorna=0
        if self.__pago==False:
            retorna=self.__taller.getMonto()
        elif self.__pago==True:
            retorna=0
        return retorna
    def getFecha(self):
        return str(self.__fechaInscripcion)

