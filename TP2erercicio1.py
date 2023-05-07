# %%
import os.path

def encriptar_vigenere (texto, clave):
    clave = clave.lower()
    texto = texto.lower()
    texto_cifrado = ''
    indice_clave = 0 
    for caracter in texto:
        if caracter.isalpha():
            rotacion = 
            caracter_cifrado = 
            texto_cifrado += caracter_cifrado
            indice_clave = 
        else:
            texto_cifrado += caracter
    return texto_cifrado

entrada_archivo = input('Ingrese la ruta del archivo de entrada: ')

if os.path.exists(entrada_archivo) == False:
    print ('El archivo no se pudo encontar.')
    
else:
    with open (entrada_archivo, 'r') as entrada:
        texto = entrada.read()

    clave = input ('Ingrese la clave de cifrado: ')

    salida_archivo = input ('Ingrese la ruta del archivo de salida: ')
    with open (salida_archivo, 'w') as salida:
        salida.write(encriptar_vigenere(texto, clave))



# %%
