if __name__ == "__main__":
    listaConvidados = ['Alan', 'Adan', 'Sonia']

    nome = input("Digite seu nome: ")
    idade = int(input('Digite sua idade: '))

    estaNaLista = nome in listaConvidados
    maiorIdade = idade >= 18

    if estaNaLista:
        if maiorIdade:
            print("Pode entrar você foi convidado e é maior de idade!")
        else:
            print("Desculpe, seu nome está na lista, mas você é menor de idade!")
    else:
        print('Desculpe, mas seu nome não esta na lista!')