from classPersona import Persona


class ColeccionPersonas:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    
    def agregarPersona(self,persona):
        if isinstance(persona, Persona):
            self.__lista.append(persona)