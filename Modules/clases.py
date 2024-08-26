#Fecha: 30/05/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo
#Versión 3.12.3

import Modules.functions as functions

class Persona: #Definiendo la clase padre
    def __init__(self,document='',name=''): #Método constructor
        self.__document=document
        self.__name=name

    #Métodos getter y setter para los valores
    def get__document(self):
        return self.__document
    

    def set__document(self, value):
        self.__document = value
    
    
    def get__name(self):
        return self.__name
    

    def set__name(self, value):
        self.__name=value


    def leer_datos(self):
        self.__document(functions.leer_documento())
        self.__name(functions.leer_nombre())


    def informacion(self): #Mostrando la información con .format
        print( 'el numero de documento es {0} y mi nombre es {1}'.format(self.get__document(), self.get__name()))

