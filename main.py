from manejadorTalleres import ManejadorTalleres
from manejadorInscripciones import ColeccionInscripciones
from manejadorPersonas import ColeccionPersonas
import os
from classMenu import Menu
if __name__=='__main__':
    mt=ManejadorTalleres()
    mt.cargarArchivo()
    mi=ColeccionInscripciones()
    mp=ColeccionPersonas()
    menu= Menu()
    salir= False     
    os.system('cls')      
    while not salir:
            print("-------------------Menu-------------------")
            print(' 1- CARGAR TALLERES')
            print(' 2- INSCRIPCION')
            print(' 3- CONSULTAR INSCRIPCION')
            print(' 4- INSCRIPTOS TALLER')
            print(' 5- REGISTRAR PAGO')
            print(' 6- CREAR ARCHIVO')
            print(' 7- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5','6','7','8'):
                menu.opcion(int(op),mt,mi,mp)
                if op=='8':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")
            os.system('cls')