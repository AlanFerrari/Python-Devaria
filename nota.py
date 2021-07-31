if __name__ == '__main__':
    nota = int(input("Digite sua nota: "))

    if nota > 60:
        print("Você está aprovado")
    elif nota > 30:
        print("Você ficou de recuperação")
    else:
        print("Você está reprovado")
