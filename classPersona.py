
class Persona:
    __nombre=''
    __direccion=''
    __dni=''
    
    def __init__(self,nombre,direccion,dni):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__dni=dni

    def __str__(self):
        return ('NOMBRE:{}\tDIRECCION:{}\tDNI:{}'.format(self.__nombre,self.__direccion,self.__dni))
    
    def getDni(self):
        return str(self.__dni)
    def getNombre(self):
        return self.__nombre