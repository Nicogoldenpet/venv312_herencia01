#Fecha: 30/05/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo
#Versión 3.12.3

#Importando los módulos y las librerias
import msvcrt
import platform
import os
import time
import random
from colorama import Fore,init, just_fix_windows_console
import Modules.clases as clases
init()
just_fix_windows_console()


def ingreso(): #Definiendo la función de ingreso
    print(Fore.LIGHTBLUE_EX)
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                             BIENVENIDO AL PROGRAMA DE HERENCIAS                                                                                                         |")
    print("|                                                                                            PARA INGRESAR PRESIONE CUALQUIER TECLA                                                                                                       |")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                                                                                                                                                                         |")
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    msvcrt.getch()
    limpiar_pantalla()
    

def limpiar_pantalla(): #Definiendo la función para limpiar pantalla
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def leer_documento():
    while True:
        documento = (input("Ingrese su documento: "))
        if (documento.isnumeric() and (len(documento) > 5)):
            break
        else:
            print("Solo se permiten números hasta una longitud de 10 dígitos.")
    return documento

def leer_nombre():
    while True:
        nombre = (input("Ingrese su nombre: "))
        if (nombre.replace(" ", "").isalpha()):
            break
        else:
            print("Solo se permiten caracteres alfabéticos.")
    return nombre



                    
                


