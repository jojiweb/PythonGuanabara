a = input("Digite algo para receber as informações: ")
tipo = type(a)
alfanumerico = a.isalnum()
maiusculas = a.isupper()
numero = a.isnumeric()

print("O tipo dele é {} \n ele é alfanumérico? {} \n está em maiúsculo? {} \n é um número? {}".format(tipo, alfanumerico, maiusculas, numero))