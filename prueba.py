import random

#esta funcion permite selecionar un topico

def elegir_topico(selec):
    if selec == 1:
        salii = lista_animales
    elif selec == 2:
        salii = lista_cine
    elif selec == 3:
        salii = lista_tecnologia
    else:
        salii = 'no selec'
    return salii    
lista_animales = ['perro', 'gato' ,'mamífero', 'ave' ,'reptil', 'peces', 'insectos' ,'carnívoro', 'herbívoro' ,'hábitat']
lista_cine = ['película', 'director', 'actor', 'guion', 'escena', 'estreno', 'género' ,'trama' ,'reparto' ,'banda ,sonora']
lista_tecnologia = [ 'innovación', 'software', 'hardware', 'redes', 'internet', 'computadora', 'aplicación', 'código' ,'nube' ,'seguridad']

paso = random.randint(0,9)

print(paso)
entra = int(input('Escribe 1, 2, 3, 4'))
salida = elegir_topico(entra)
ver = lista_animales[paso]

print(ver)

numee = len(ver)
 
ssali = ver.find('a')
print(numee)
print(ssali)
print(salida)