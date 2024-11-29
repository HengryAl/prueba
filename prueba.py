import random

#esta funcion permite selecionar un topico

def elegir_topico(selec):
    if selec == 1:
        print('sele1')
    elif selec == 2:
        print('sele2')
    elif selec == 3:
        print('selec3')
    else:
        print('no selec')
        
lista_animales = ['perro', 'gato' ,'mamífero', 'ave' ,'reptil', 'peces', 'insectos' ,'carnívoro', 'herbívoro' ,'hábitat']
lista_cine = ['película' 'director' 'actor' 'guion' 'escena' 'estreno' 'género' 'trama' 'reparto' 'banda sonora']
lista_tecnologia = [ 'innovación' 'software' 'hardware' 'redes' 'internet' 'computadora' 'aplicación' 'código' 'nube' 'seguridad']

paso = random.randint(0,9)

print(paso)


ver = lista_animales[paso]

print(ver)

numee = len(ver)

print(numee)
