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

    data = part1.try_path('Ingrese nombre del archivo encriptado: ')
    information = info_collector(data)
    graphic_data = groups_generator(information)
    plt.bar([x for x in graphic_data.keys()], [y for y in graphic_data.values()])
    plt.axhline(y= 0.0686, color= "k", linestyle= "--")
    plt.axhline(y = 0.0385, color = "k", linestyle= "--")
    plt.xlabel("Largo de la clave")
    plt.ylabel("Índice de coincidencia")
    plt.show()
    
    graphic_data_2 = plt.subplot(3, 2, 1)
    plt.bar([x for x in ENGLISH_LETTERS_FRECUENCIES.keys()], [y for y in ENGLISH_LETTERS_FRECUENCIES.values()])
    plt.ylabel('Frecuencia')
    plt.title('Inglés')
    
    graphic_data_3 = frequency_generator(information)
    posicion = 1 
    grupo = 0
    for dato in graphic_data_3:
        posicion += 1
        grupo += 1
        plt.subplot(3, 2, posicion)                                              # La posicion del grafico en la figura y el grupo que indica el titulo iteran junto a los datos del diccionario de frecuencias obtenido. 
        plt.bar([x for x in dato.keys()], [y for y in dato.values()])
        plt.ylabel('Frecuencia')
        plt.title(f'Letra {grupo} de la clave')
    plt.tight_layout()
    plt.show()
    
        
def info_collector(data):
    '''
    Devuelve los caracteres del archivo que pertenecen al alfabeto ingles en una cadena
    Argumentos:
    Data -- variable que, dado un archivo de texto existente, lee las lineas del archivo.
    '''
    information = ''
    for line in data:
            for chr in line:
                if chr in part1.ABC:    # Usamos el alfabeto definido en el ejercicio 1.
                    information += chr
    return information

def groups_generator(information):              
    '''
    Calcula el IoC promedio para una cadena dividida en grupos de letras de distintos tamaños
    Information -- Cadena de caracteres del alfabeto ingles ibtenida de la funcion info_collector.
    '''
    dicc = {}
    for key in range(1,31):
        groups = []

        for ord in range(len(information[:key])):
            groups.append(information[ord::key])

        ioc_average= 0

        for group in groups:
            ioc_average += get_ioc(group)

        ioc_average = ioc_average / len(groups)
        dicc[key] = ioc_average

    return dicc
    
def get_ioc (group):
    '''
    Calcula el IoC para un grupo de caracteres de tamaño variable
    Argumentos:
    Group--
    '''
    dictionary = {}

    for chr in group:
        if chr not in dictionary:
            dictionary[chr] = 1
        else:
            dictionary[chr] += 1

    ioc_numerator = 0
    for num in dictionary.values():
        ioc_numerator += (num*(num-1))              
        
    ioc = ioc_numerator/(len(group)*(len(group)-1))         # Formula del IoC
    return ioc 

def frequency_generator(information):                               # Esta es la funcion para la parte 2 del ejercicio 3.
    '''
    Devuelve una lista de diccionarios. Cada diccionario contiene las frecuencias de las letras de un grupo de caracteres de la cadena de entrada
    Argumentos:
    Information -- Cadena de texto (unicamente caracteres de alfabeto ingles)
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
            letters_frequency[chr] = counter/len(group)
        all_frequencies.append(letters_frequency)

    return all_frequencies
    
if __name__ == '__main__':
    main()
