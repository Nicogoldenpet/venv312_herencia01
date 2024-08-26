#Fecha: 30/05/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo
#Versión 3.12.3

#Importando los módulos y colorama
import Modules.clases as clases
import Modules.functions as functions
from colorama import Fore,init, just_fix_windows_console

init()
just_fix_windows_console()

def main(apren1): #Definiendo la función main()
    functions.ingreso()

if __name__ == "__main__": #Ejecutando el código con las instancias de las clases
    apren1 = clases.Persona.leer_datos()
    main(apren1)

    
    