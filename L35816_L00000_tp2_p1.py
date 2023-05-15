ABC = 'abcdefghijklmnopqrstuvwxyz'

def main():
    print('≡≡Encriptador de Cifrado de Vigenère≡≡')
    data = try_path('Ingrese nombre del archivo en texto plano: ')
    code = try_code('Ingrese la clave: ')
    archive = try_archive('Ingrese nombre del archivo para la encripción: ')
    encrypter(data, code, archive)

def encrypter(data:list, code:str, archive:str, desencrypter=False):      
    '''
    Por default, recibe una clave y encripta un archivo de entrada utilizando el Cifrado de Vigenère. Escribe el texto cifrado en 
    un archivo nuevo cuyo nombre fue elegido por el usuario. La función también desencripta en caso de que 'desencrypter' sea 
    verdadero. Esto se utilizará para la parte 2.
    
    Parámetros de entrada
    ---------------------
    data: list
    Archivo de entrada a encriptar o desencriptar
    code: str
    Clave para el cifrado
    archive: str
    Nombre para el archivo de salida
    desencrypter: bool
    Indica si los datos se cifran (false) o descifran (true). Por default es false.
    '''
    dictionary = {}                                     
    inverted_dictionary = {}
    for number, letter in enumerate(ABC):
        dictionary[letter] = number                     # Se generan un diccionario cuya key es el caracter y cuyo value el número que le corresponde, y otro a la inversa. Estos datos serán utiles para el cifrado o descifrado
        inverted_dictionary[number] = letter

    with open (archive, 'w') as f:

        code_counter = 0
        for line in data:
            line = str(line).lower()
            new_line = ''

            for chr in line:
                if chr in ABC:
                    if not desencrypter:
                        new_ord = (dictionary[chr]+dictionary[code[code_counter]])%26
                        new_chr = inverted_dictionary[new_ord]
                    else: 
                        new_ord = (dictionary[chr]-dictionary[code[code_counter]])%26
                        new_chr = inverted_dictionary[new_ord]
                    if code_counter >= len(code)-1:                                              # 'code_counter' es una variable que permite iterar sobre cada caracter de la clave elegida, una vez que es agotada, vuelve a repetirse
                        code_counter = 0
                    else:
                        code_counter +=1
                else:
                    new_chr = chr
                new_line += new_chr
                
            f.write(new_line)

def try_path(prompt:str) -> list:
    '''
    Verifica que el archivo exista y, en caso de existir, lo lee y devuelve una lista de listas que corresponden a
    las lineas del archivo 
    
    Parámetros de entrada
    ---------------------
    prompt: str
    Mensaje mostrado al usuario para que realice la entrada

    Parámetros de salida
    --------------------
    data: list
    Lista de listas, con cadenas de texto correspondientes a las líneas del archivo abierto
    '''
    path = input(prompt)
    try:
        with open (path, 'r') as arch:        
            data = arch.readlines()              
        return data
    except FileNotFoundError:
        print ('...\nNo se pudo abrir el archivo')
        try_path(prompt)                                    # En caso de no poder abrir el archivo, se volverá a pedir un ingreso hasta que este se haga efectivo

def try_code (prompt: str) -> str:
    ''' 
    Corrobora que la clave ingresada, convertida a letras minúsculas, sea válida (deben ser unicamente letras del alfabeto inglés)

    Parámetros de entrada
    ---------------------
    prompt: str
    Mensaje mostrado al usuario para que realice la entrada

    Parámetros de salida
    --------------------
    code: str
    Clave ingresada
    '''
    code = input(prompt)
    code = code.lower()
    for chr in code:
        if chr not in ABC:
            print('...\nLa clave solo puede contener letras del alfabeto inglés') 
            try_code(prompt)                                                            # En caso de una entrada inesperada, se pedirá otra clave hasta que se cumplan las condiciones
    return code

def try_archive (prompt:str) -> str:
    '''
    Impone las condiciones para el nombre del archivo a generar.

    Parámetros de entrada
    ---------------------
    prompt: str
    Mensaje mostrado al usuario para que realice la entrada

    Parámetros de salida
    --------------------
    archive: str
    Nombre para el archivo a generar
    '''
    archive = input(prompt)
    invalid_chr = '\/:*?"<>|'                
    for chr in archive:
        if chr not in invalid_chr:
                return archive
        else:
            print('...\nEl nombre para el archivo es inválido')  
            try_archive(prompt)                                             # En caso de que no sea un nombre válido para un archivo, se pedirá uno nuevo hasta que se cumplan las condiciones

if __name__ == "__main__":
    main()
