import os
from manejadorTalleres import ManejadorTalleres
from manejadorInscripciones import ColeccionInscripciones
from manejadorPersonas import ColeccionPersonas
from classPersona import Persona
from classTallerCapacitacion import TallerCapacitacion
from classInscripcion import Inscripcion

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self,op,mt,mi,mp):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mt,mi,mp)

    def salir(self,mt,mi,mp):
        print('Salida del programa')

    def opcion1(self,mt,mi,mp):
        os.system('cls')
        mt.cargarArchivo()
        input()
        os.system('cls')

    def opcion2(self,mt,mi,mp):
        band=False
        os.system('cls')
        print('\t\t---INSCRIPCION PERSONA----\n')
        nombre=input('~INGRESE NOMBRE Y APELLIDO:')
        direccion=input('~INGRESE DIRECCION:')
        dni=input('~INGRESE DNI:')
        os.system('cls')
        print('\t\t---INSCRIPCION PERSONA----\n')
        print('NOMBRE:{:25}\nDIRECCION:{}\nDNI:{}'.format(nombre.upper(),direccion.upper(),dni.upper()))
        taller=int(input('\tINGRESE EL TALLER QUE DESEA INSCRIBIR: '))
        persona=Persona(nombre, direccion, dni)
        while not band:
            inscrip=mt.inscripcion(persona,taller)
            if inscrip!=None:
                mi.agregarInscripcion(inscrip)
                mp.agregarPersona(persona)
                band=True
                print('\n\t[---INSCRIPCION REALIZADA CON EXITO---]')
            elif inscrip==None:
                os.system('cls')
                print('++++ TALLER NO ENCONTRADO. REINTENTE ++++')
                input()
                os.system('cls')
                print('\t\t---INSCRIPCION PERSONA----\n')
                print('NOMBRE: {:25}\nDIRECCION: {:20}\nDNI: {:10}'.format(nombre.upper(),direccion.upper(),dni.upper()))
                taller=int(input('\tINGRESE EL TALLER QUE DESEA INSCRIBIR: '))
        input()
        os.system('cls')
        mi.listar()
        input()
        os.system('cls')

    def opcion3(self,mt,mi,mp):
        band=False
        os.system('cls')
        print('~~~CONSULTA INSCRIPCION~~~\n')
        dni=input('INGRESE EL DNI QUE DESEA BUSCAR: ')
        while not band:
            inscrip=mi.consulta(str(dni))
            if inscrip!=None:
                print('LA PERSONA CON DNI {} ESTA INSCRIPTA Y DEBE {} PESOS'.format(dni,inscrip.deuda()))
                band=True
            elif inscrip==None:
                print('HOLA HOLA')
                band=True
            else:
                print('EL DNI REGISTRADO NO SE ENCUENTRA INSCRIPTO.REINTENTE')
                band=True
        input()
        os.system('cls')
    def opcion4(self,mt,mi,mp):
        os.system('cls')
        print('~~~CONSULTA INSCRIPTOS~~~\n')
        taller=int(input('INGRESE EL TALLER: '))
        band=False
        while not band:
            band=mt.InscriptosTaller(taller)
            if band:
                pass
            else:
                print('NO EXISTE TALLER INGRESADO.REINTENTE')
                taller=int(input('INGRESE EL TALLER: '))
        input()
        os.system('cls')
    def opcion5(self,mt,mi,mp):
        os.system('cls')
        print('~~~REGISTRAR PAGO~~~')
        dni=input('INGRESE DNI:')
        band=False
        while not band:
            inscrip=mi.pago(dni)
            if inscrip!=None:
                print('PAGO REGISTRADO')
                band=True
                input()
                os.system('cls')
            else:
                print('INSCRIPCION NO ENCONTRADA. DNI NO REGISTRADO')
                input()
                os.system('cls')
                print('~~~REGISTRAR PAGO~~~')
                dni=input('INGRESE DNI:')
    def opcion6(self,mt,mi,mp):
        os.system('cls')
        print('CARGA DE ARCHIVO')
        mi.crearArchivo()
        print('ARCHIVO CREADO')
        input()
        os.system('cls')



        