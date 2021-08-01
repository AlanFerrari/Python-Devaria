from os import error


def soma(n1, n2):
    print(f'\nSomando {n1} + {n2}')
    resultado = n1 + n2
    return resultado
def subtracao(n1, n2):
    print(f'\nSubtraindo {n1} - {n2}')
    resultado = n1 - n2
    return resultado
def multiplicacao(n1, n2):
    print(f'\nMultiplicando {n1} * {n2}')
    return n1 * n2
def divisao(n1, n2):
    if n2 != 0:
        print(f'\nDividindo {n1} / {n2}')
        return n1 / n2
    else:
        print('\nNão é possível dividir por zero')
        return
def modulo(n1, n2):
        print(f'\nModulando {n1} % {n2}')
        return n1 % n2
def elevacao(n1, n2):
    print(f'\nElevando {n1} ** {n2}')
    return n1 ** n2
if __name__ == '__main__':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    operador = input('\nDigite o operador aritmético: ')
    resultado = None

    if operador == '+':
        resultado = soma(n1, n2)
    elif operador == '-':
        resultado = subtracao(n1, n2)
    elif operador == '*':
        resultado = multiplicacao(n1, n2)
    elif operador == '/':
        resultado = divisao(n1, n2)
    elif operador == '%':
        resultado = modulo(n1, n2)
    elif operador == '**':
        resultado = elevacao(n1, n2)
    else:
        print('\nOperador inválido!')
    
    if resultado != None:
        print(f'\nO resultado da operação é: {resultado}')
    print('')