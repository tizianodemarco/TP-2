import L35816_L00000_tp2_p1 as part1                # Al ser un ejercicio muy similiar al 1, utilizamos las funciones definidas en ese ejercicio para optimizar lineas de código.

def main():
    print('≡≡Encriptador de Cifrado de Vigenère≡≡')
    data = part1.try_path('Ingrese nombre del archivo encriptado: ')
    code = part1.try_code('Ingrese la clave: ')
    archive = part1.try_archive('Ingrese nombre del archivo para la encripción: ')
    part1.encrypter(data, code, archive, desencrypter=True)                         # El argumento desencrypter decifra el codigo cuando toma el valor true.

if __name__ == '__main__':
    main()
