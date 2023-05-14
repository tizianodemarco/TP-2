ABC = 'abcdefghijklmnopqrstuvwxyz'

def main():
    print('≡≡Encriptador de Cifrado de Vigenère≡≡')
    data = try_path('Ingrese nombre del archivo en texto plano: ')
    code = try_code('Ingrese la clave: ')
    archive = try_archive('Ingrese nombre del archivo para la encripción: ')
    encrypter(data, code, archive)

def encrypter(data, code, archive:str, desencrypter=False):
'''
Cifra un archivo de entrada utilizando el Cifrado de Vigenère y escribe el texto cifrado en un archivo de salida
Argumentos:
Data -- Contenido del archivo de entrada
Code -- Clave de cifrado (str)
Archive -- Archivo de salida
Desencrypter -- Indica si los datos se cifran (false) o descifran (true)
'''
    dictionary = {}
    inverted_dictionary = {}
    for number, letter in enumerate(ABC):
        dictionary[letter] = number
        inverted_dictionary[number] = letter

    with open (archive, 'w') as f:     
        counter = 0
        for line in data:
            line = str(line).lower()
            new_line = ''
            for chr in line:
                if chr in ABC:
                    if not desencrypter:
                        new_ord = (dictionary[chr]+dictionary[code[counter]])%26
                        new_chr = inverted_dictionary[new_ord]
                    else: 
                        new_ord = (dictionary[chr]-dictionary[code[counter]])%26
                        new_chr = inverted_dictionary[new_ord]
                    if counter >= len(code)-1:
                        counter = 0
                    else:
                        counter +=1
                else:
                    new_chr = chr
                new_line += new_chr
            f.write(new_line)

def try_path(prompt:str):
    '''
    Verifica que el archivo exista y, en caso de existir, devuelve las lineas del archivo.
    Argumentos:
    Prompt -- Mensaje de input
    '''
    path = input(prompt)
    try:
        with open (path, 'r') as arch:        
            data = arch.readlines()              
        return data
    except FileNotFoundError:
        print ('...\nNo se pudo abrir el archivo')
        try_path(prompt)

def try_code (prompt: str):
    ''' 
    Corrobora que la clave ingresada sea válida (unicamente letras del alfabeto inglés)
    Prompt -- Mensaje de input
    '''
    code = input(prompt)
    code = code.lower()
    for chr in code:
        if chr not in ABC:
            print('...\nLa clave solo puede contener letras del alfabeto inglés') 
            try_code(prompt)
    return code

def try_archive (prompt:str):
    '''
    Impone las condiciones del nombre del archivo de salida.
    Prompt -- Mensaje de input
    '''
    archive = input(prompt)
    invalid_chr = '\/:*?"<>|'                
    for chr in archive:
        if chr not in invalid_chr:
                return archive
        else:
            print('...\nEl nombre para el archivo es inválido')  
            try_archive(prompt)

if __name__ == "__main__":
    main()
