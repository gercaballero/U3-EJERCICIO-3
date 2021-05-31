def opcion7(self,mt,mi,mp):
        os.system('cls')
        print('~~~CONSULTAR PAGO~~~')
        dni=input('INGRESE DNI:')
        band=False
        while not band:
            inscrip=mi.consulta(str(dni))
            if inscrip!=None:
                band=True
                os.system('cls')
                print('CONSULTAS')
                print('EN M INSCRIPCIONES----> PAGO:{}'.format(mi.pagox(dni)))
                print('EN M TALLERES----> PAGO:{}'.format(mt.pagox(dni,inscrip.getNumeroTaller())))
                input()
            else:
                print('INSCRIPCION NO ENCONTRADA. DNI NO REGISTRADO')
                input()
                os.system('cls')
                band=True


def pagox(self,dni,num):
        inscripcion=None
        i=0
        retorna=''
        while inscripcion==None and i<self.__dimension:
                if self.__arreglo[i].getId()==num:
                        inscripcion=self.__arreglo[i].retornaInscripcion(dni)
                        if inscripcion.getPago():
                            retorna='SI'
                        elif not inscripcion.getPago():
                            retorna='NO'
                else:
                    i+=1
        return retorna

    
def pagox(self,dni):
        inscripcion=None
        i=0
        retorna=''
        while inscripcion==None and i<len(self.__lista):
            if self.__lista[i].getDniPersona().upper()==dni.upper():
                inscripcion=self.__lista[i]
                if inscripcion.getPago():
                    retorna='SI'
                elif not inscripcion.getPago():
                    retorna='NO'
            else:
                i+=1
        return retorna