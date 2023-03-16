import random
def bola_ocho():
    preguntita = (input("Cual es tu pregunta? "))
    print(preguntita)

    respuesta_uno = "Rotundo Si"
    respuesta_dos = "Si, pero puede que me equivoque"
    respuesta_tres = "Tines 50% de posivilidades que se cumpla"
    respuesta_cuatro = "Ni lo sueñes"
    respuesta_cinco = "Rotundo No"
    respuesta_seis = "Nel pastel"
    respusta_siete = "talvez si pones de tu parte"
    respuesta_ocho = "Cuando los cerdos vuelen"

    preguntas = random.randint(1,8)

    if preguntas == 1:
        print(respuesta_uno)
    if preguntas == 2:
        print(respuesta_dos)
    if preguntas == 3:
        print(respuesta_tres)
    if preguntas == 4:
        print(respuesta_cuatro)
    if preguntas == 5:
        print(respuesta_cinco)
    if preguntas == 6:
        print(respuesta_seis)
    if preguntas == 7:
        print(respusta_siete)
    if preguntas == 8:
        print(respuesta_ocho)

bola_ocho()

