import unicodedata

abecedario_numeros = {}
abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
vocales_tilde = 'ÁÉÍÓÚ'
for i, letra in enumerate('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'):
    abecedario_numeros[letra] = i

def convertir_mayuscula(entrada):
    texto_mayuscula=""
    texto_mayuscula = entrada.upper()
    return texto_mayuscula

def encriptacion_vigenere(entrada, palabra_clave, modulo):
    mensaje = ""
    cont = 0
    for i in range(len(entrada)):
        if entrada[i].isalpha():
            numero = (abecedario_numeros[entrada[i]]+abecedario_numeros[palabra_clave[cont]]) % modulo
            letra_encriptada = abecedario[numero]
            mensaje += letra_encriptada
            cont +=1
        else:
            mensaje += entrada[i]
        if cont > len(palabra_clave)-1:
            cont = 0
    return mensaje

def encriptacion_vigenere_ascii(entrada,palabra_clave):
    mensaje = ""
    cont = 0
    for i in range(len(entrada)):
        if entrada[i].isalpha():
            numero = (ord(entrada[i])-33 + ord(palabra_clave[cont])-33) % 191
            letra_encriptada = chr(numero)
            mensaje += letra_encriptada
            cont += 1
        else:
            mensaje += entrada[i]
        if cont > len(palabra_clave)-1:
            cont = 0
    return mensaje

def eliminar_tildes(entrada):
    texto_sin_tildes = ''.join((c for c in unicodedata.normalize('NFD', entrada) if unicodedata.category(c) != 'Mn'))
    return texto_sin_tildes

def calcular_frecuencia(entrada):
    frecuencia = {}
    for letra in entrada:
        if letra.isalpha():
            if letra in frecuencia:
                frecuencia[letra] += 1
            else:
                frecuencia[letra] = 1
    return frecuencia

def descifrado(entrada, palabra_clave,modulo):
    mensaje = ""
    cont = 0
    for i in range(len(entrada)):
        if entrada[i].isalpha():
            numero = (abecedario_numeros[entrada[i]]-abecedario_numeros[palabra_clave[cont]]) % modulo
            letra_encriptada = abecedario[numero]
            mensaje += letra_encriptada
            cont +=1
        else:
            mensaje += entrada[i]
        if cont > len(palabra_clave)-1:
            cont = 0
    return mensaje

# Variables
modulo = 27
#Ejercicio 1
#mensaje = "Creer que es posible es el paso número uno hacia el  ́exito. Despertarse y pensar en algo positivo puede cambiar el transcurso de todo el día. No eres lo suficientemente viejo como para no iniciar un nuevo camino hacia tus sueños. Levántate cada mañana creyendo que vas a vivir el mejor día de tu vida"
#palabra_clave = "POSITIVO"
#print(mensaje,"\n")
##mensaje_cifrado = encriptacion_vigenere_ascii(mensaje,palabra_clave)
##print(mensaje_cifrado,'\n')
#mensaje = convertir_mayuscula(mensaje)
#mensaje = eliminar_tildes(mensaje)
#mensaje_cifrado = encriptacion_vigenere_ascii(mensaje,palabra_clave)
#print(mensaje_cifrado)


#Ejercicio 2
#mensaje = "Creer que es posible es el paso número uno hacia el  ́exito. Despertarse y pensar en algo positivo puede cambiar el transcurso de todo el día. No eres lo suficientemente viejo como para no iniciar un nuevo camino hacia tus sueños. Levántate cada mañana creyendo que vas a vivir el mejor día de tu vida"
#mensaje = convertir_mayuscula(mensaje)
#mensaje = eliminar_tildes(mensaje)
#palabra_clave = "POSITIVO"
#mensaje_cifrado = encriptacion_vigenere(mensaje,palabra_clave,modulo)
#print(mensaje)

#Ejercicio 5
#mensaje = "Creer que es posible es el paso número uno hacia el  ́exito. Despertarse y pensar en algo positivo puede cambiar el transcurso de todo el día. No eres lo suficientemente viejo como para no iniciar un nuevo camino hacia tus sueños. Levántate cada mañana creyendo que vas a vivir el mejor día de tu vida"
#mensaje = convertir_mayuscula(mensaje)
#mensaje = eliminar_tildes(mensaje)
#frecuencias = calcular_frecuencia(mensaje)
#for letra, frecuencia in sorted(frecuencias.items()):
#    print(f"{letra}: {frecuencia}")

#palabra_clave = "POSITIVO"
#mensaje_cifrado = encriptacion_vigenere(mensaje,palabra_clave,modulo)
#frecuencias = calcular_frecuencia(mensaje_cifrado)
#for letra, frecuencia in sorted(frecuencias.items()):
#    print(f"{letra}: {frecuencia}")

#palabra_clave = "HIELO"
#mensaje_cifrado = encriptacion_vigenere(mensaje,palabra_clave,modulo)
#frecuencias = calcular_frecuencia(mensaje_cifrado)
#for letra, frecuencia in sorted(frecuencias.items()):
#    print(f"{letra}: {frecuencia}")

#palabra_clave = "MAR"
#mensaje_cifrado = encriptacion_vigenere(mensaje,palabra_clave,modulo)
#frecuencias = calcular_frecuencia(mensaje_cifrado)
#for letra, frecuencia in sorted(frecuencias.items()):
#    print(f"{letra}: {frecuencia}")

#Ejercicio 6
mensaje = "WPIXHVYYOSRTECSZBEEGHUUFWRWTZGRWUFSRIWESSXVOHAIHOHWWHCWHUZOBOZEAOYBMCRLTEYOTI"
mensaje = convertir_mayuscula(mensaje)
mensaje = eliminar_tildes(mensaje)
palabra_clave = "HIELO"
mensaje_descifrado = descifrado(mensaje,palabra_clave,modulo)
print(mensaje_descifrado)

