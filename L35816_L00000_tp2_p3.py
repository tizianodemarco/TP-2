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
    graphic_data_2 = frequency_generator(information)
    print(graphic_data_2)
    for dato in graphic_data_2:                                              # A lo de aca lo hice solo para ver como se estaban imprimiendo los graficos
        plt.bar([x for x in dato.keys()], [y for y in dato.values()])
        plt.show()

def info_collector(data):
    information = ''
    for line in data:
            for chr in line:
                if chr in part1.ABC:
                    information += chr
    return information

def groups_generator(information):
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
    
    dictionary = {}

    for chr in group:
        if chr not in dictionary:
            dictionary[chr] = 1
        else:
            dictionary[chr] += 1

    ioc_numerator = 0
    for num in dictionary.values():
        ioc_numerator += (num*(num-1))
        
    ioc = ioc_numerator/(len(group)*(len(group)-1))
    return ioc 

def frequency_generator(information):                               # ESTA ES LA FUNCION PARA EL DOS, LO DEMAS SON MODULOS PARA LA PARTE 1
    
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
