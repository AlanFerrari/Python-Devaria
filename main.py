def Validar(valido, valido2):
    if valido and valido2:
        return 'Os valores são true.'
    else:
        return 'Valor incompativel'

if __name__ == "__main__":
    numero = input("Digite um número: ")
    print(f"O número digitado foi {numero}")
    
    #O código abaixo usa a função/método
    teste = True
    teste2 = True
    respostaDaFuncao = Validar(teste, teste2)
    print(respostaDaFuncao)
