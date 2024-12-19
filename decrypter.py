import sys
import os
import pyaes

def main():
    if len(sys.argv) <= 1:
        print("you need to pass a file as an argument")
        return

    file_name = sys.argv[1]
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    ## chave para descriptografia
    key = str.encode("testeransomwares")
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    ## remover o arquivo criptografado
    os.remove(file_name)

    ## criar o arquivo descriptografado
    new_file = f"{file_name.split(".")[0]}.txt"
    new_file = open(f'{new_file}', "wb")
    new_file.write(decrypt_data)
    new_file.close()

if __name__ == "__main__":
    main()
