#autor: Alejandro Aguirre
#v:0.0.1                                      date:25/04/2022
#----------------------------------------------------------------
import random
Aprobado=20
print(
"""
:) Bienvenidos al programa de Prueba de las Tablas de Multiplicar!!
Tenés que llegar a los,
""",Aprobado," puntos para aprobar.\n")
Puntos=0

while True:
    factor1=random.randint(3, 9)
    factor2=random.randint(3, 9)

    respuesta=input('Cuanto es '+str(factor1)+' x '+str(factor2)+' = ')
    resultado=factor1*factor2

    if int(respuesta) ==resultado:
        print('Correcto!')
        Puntos+=1
    else:
        print('Incorrecto :(','\nEs ',str(resultado))
        Puntos-=1
    print('Puntos=',Puntos)

    if Puntos==Aprobado:
        print('Prueba Superada!!')
        break