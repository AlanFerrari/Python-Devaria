def SecondOperand():
    print("Avaliando segundo operador")
    return True

if __name__ == "__main__":
    a = False and SecondOperand()
    print("O valor de A é", a)
    b = True and SecondOperand()
    print("O valor de B é", b)

    print('\n')

    c = False or SecondOperand()
    print("O valor de C é", c)
    d = True or SecondOperand()
    print("O valor de D é", d)

    print('\n')

    nome = "Agata"
    if nome == "Alan":
        print("O nome é Alan")
    elif nome == "Agata":
        print("O nome é Agata")
    else:
        print("Não é nenhum dos nomes!")