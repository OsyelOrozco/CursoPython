import math

print('***Constantes***')

Pi = 3.14159 #Constante de pi

print('Valor de pi:', Pi) #3.14159

NOMBRE_BASE_DATOS = "mi_base_datos" #Constante para el nombre de la base de datos
print('Nombre de la base de datos:', NOMBRE_BASE_DATOS) #mi_base_datos

#Esto NO se deve hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = 'Listado_Clientes' #Constante para el nombre de la base de datos
print('No cambiar el valor de una constante:', NOMBRE_BASE_DATOS) #Listado_Clientes

#usar una constante del lenguaje Python, aunque es este caso no esta en mayusculas
print('Valor de math.pi:', math.pi) #3.14159