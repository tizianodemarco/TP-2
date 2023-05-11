import L35816_L00000_tp2_p1 as part1

def main():
    print('≡≡Encriptador de Cifrado de Vigenère≡≡')
    data = part1.try_path('Ingrese nombre del archivo encriptado: ')
    code = part1.try_code('Ingrese la clave: ')
    archive = part1.try_archive('Ingrese nombre del archivo para la encripción: ')
    part1.encrypter(data, code, archive, desencrypter=True)

if __name__ == '__main__':
    main()