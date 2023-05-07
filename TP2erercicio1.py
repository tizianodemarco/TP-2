import os.path

def encriptar_vigenere (texto, clave):
    clave = clave.lower()
    texto = texto.lower()
    texto_cifrado = ''
    indice_clave = 0 
    for caracter in texto:
        if caracter.isalpha():
            rotacion = ord(clave[indice_clave]) - ord('a')
            caracter_cifrado = chr ((ord(caracter) - ord('a') + rotacion) % 26 + ord('a'))
            texto_cifrado += caracter_cifrado
            indice_clave = (indice_clave + 1) % len(clave)
        else:
            texto_cifrado += caracter
    return texto_cifrado

entrada_archivo = input('Ingrese la ruta del archivo de entrada: ')

while os.path.exists(entrada_archivo) == False:
    print ('El archivo no se pudo encontar, intente nuevamente')
    entrada_archivo = input('Ingrese la ruta del archivo de entrada: ')

with open (entrada_archivo, 'r') as entrada:
    texto = entrada.read()

clave = input ('Ingrese la clave de cifrado: ')

salida_archivo = input ('Ingrese la ruta del archivo de salida: ')
with open (salida_archivo, 'w') as salida:
    salida.write(encriptar_vigenere(texto, clave))


