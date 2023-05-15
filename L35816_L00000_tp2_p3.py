import L35816_L00000_tp2_p1 as part1
import matplotlib.pyplot as plt

def main():

    ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
    }

    data = part1.try_path('Ingrese el nombre del archivo encriptado: ')                     # Se importa nuevamente la función de la parte 1, usada para corroborar que el archivo a abrir exista y pueda abrirse
    information = info_collector(data)
    graphic_1_data = groups_generator(information)                                        
    plt.bar([x for x in graphic_1_data.keys()], [y for y in graphic_1_data.values()])       # Con ayuda del diccionario generado, se imprimen en el eje x el largo de la clave, y en el eje y los valores del índice de coincidencia obtenidos
    plt.axhline(y= 0.0686, color= "k", linestyle= "--")
    plt.axhline(y = 0.0385, color = "k", linestyle= "--")
    plt.xlabel("Largo de la clave")
    plt.ylabel("Índice de coincidencia")
    plt.show()
    
    plt.subplot(3, 2, 1)                                                                                                # Primer figura del gráfico de frecuencias (alfabeto inglés)
    plt.bar([x for x in ENGLISH_LETTERS_FRECUENCIES.keys()], [y for y in ENGLISH_LETTERS_FRECUENCIES.values()])
    plt.ylabel('Frecuencia')
    plt.title('Inglés')

    graphic_2_data = frequency_generator(information)
    posicion = 1 
    grupo = 0
    for key_letter in graphic_2_data:
        posicion += 1
        grupo += 1
        plt.subplot(3, 2, posicion)                                                         # La posicion de cada figura en el gráfico y el grupo que indica el titulo, iteran junto a los datos del diccionario de frecuencias obtenido
        plt.bar([x for x in key_letter.keys()], [y for y in key_letter.values()])
        plt.ylabel('Frecuencia')
        plt.title(f'Letra {grupo} de la clave')
    plt.tight_layout()
    plt.show() 
        
def info_collector(data: list) -> str:
    '''
    Recibe una lista de listas con cadenas de texto, itera en cada una de ellas y en cada caracter para
    devolver una cadena con aquellos caracteres que pertenecen al alfabeto ingles.

    Parámetros de entrada
    ---------------------
    data: list
    Producto de la función 'try_path' importada de la parte uno, es una lista de listas, donde cada
    sublista es una línea del archivo abierto
    
    Parámetros de salida
    --------------------
    information: str
    Cadena de texto que almacena los caracteres del alfabeto en inglés del archivo abierto
    '''
    information = ''
    for line in data:
        for chr in line:
            if chr in part1.ABC:                # Importamos la constante del alfabeto definida en la parte 1.
                information += chr
    return information

def groups_generator(information: str) -> dict:              
    '''
    Genera los grupos de caracteres para largos de clave de 1 a 30, calcula el IoC promedio para cada grupo,
    y agrega los key_letters obtenidos a un diccionario.

    Parámetros de entrada
    ---------------------
    information: str
    Cadena de caracteres obtenida de la funcion 'info_collector'

    Parámetros de salida
    --------------------
    dicc: dict
    Diccionario que almacena como key el largo de la clave y como value el ioc calculado para ese largo
    '''
    dicc = {}
    for key_lenght in range(1,31):
        groups = []

        for ord in range(len(information[:key_lenght])):
            groups.append(information[ord::key_lenght])

        ioc_average= 0

        for group in groups:
            ioc_average += get_ioc(group)           # Tras calcular el Ioc de cada grupo con ayuda de la función 'get_ioc', va almacenando en la variable 'ioc_average' la suma de cada uno de ellos para después dividirlo por la cantidad de grupos, obteniendo así el promedio

        ioc_average = ioc_average / len(groups)
        dicc[key_lenght] = ioc_average

    return dicc
    
def get_ioc (group: list) -> int:
    '''
    Recibe una lista, que corresponde a cada grupo generado según el largo de la clave, genera un
    diccionario para contar la cantidad de veces que se repite cada letra en el grupo, y a partir de la
    fórmula del ioc, lo calcula y lo devuelve.

    Parámetros de entrada
    ---------------------
    group: list
    Lista de caracteres, generada a partir de la división por grupos según el largo de la clave
    
    Parámetros de salida
    --------------------
    ioc: int
    Cifra del ioc calculado
    '''
    repeating_letters = {}

    for chr in group:
        if chr not in repeating_letters:
            repeating_letters[chr] = 1
        else:
            repeating_letters[chr] += 1

    ioc_numerator = 0
    for num in repeating_letters.values():
        ioc_numerator += (num*(num-1))              
        
    ioc = ioc_numerator/(len(group)*(len(group)-1))         # Formula del IoC
    return ioc 

def frequency_generator(information: str) -> list:                       # Función para la parte 2 del Ejercicio 3
    '''
    Recibe los caracteres del alfabeto inglés del archivo de texto abierto, genera los grupos de caracteres
    para un largo de clave 5, cuenta la cantidad que aparece cada caracter en el grupo para después calcular 
    su frecuencia, almacenando los key_letters en un diccionario, y devuelve una lista de diccionarios, donde cada
    uno almacena como key el caracter, y como value la frecuencia de esa leyra en el grupo. Cada diccionario 
    contiene las frecuencias de las letras de un grupo de caracteres de la cadena de entrada
    
    Parámetros de entrada
    ---------------------
    information: str
    Cadena de caracteres obtenida de la funcion 'info_collector'

    Parámetros de salida
    --------------------
    all_frequencies: list
    Lista de diccionarios, donde cada diccionario almacena como key el caracter, y como value su frecuencia en el 
    grupo de caracteres generado
    '''
    groups = []
    for ord in range(len(information[:5])):
        groups.append(information[ord::5])
    
    all_frequencies = []
    for group in groups:
        letters_frequency = {}

        for letter in part1.ABC:
            letters_frequency[letter] = 0

        for chr in group:
            letters_frequency[chr] += 1

        for chr, counter in letters_frequency.items():            
            letters_frequency[chr] = counter/len(group)     # La frecuencia es calculada como la cantidad de veces que aparece el caracter en el grupo, dividido la cantidad total de caracteres del grupo
        all_frequencies.append(letters_frequency)           # Cada iteración corresponde, en este caso, desde la primera a la quinta letra de la clave

    return all_frequencies
    
if __name__ == '__main__':
    main()
