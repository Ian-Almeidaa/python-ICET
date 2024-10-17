def q1():
    num = int(input('digite um número: '))
    if num % 2 == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é ímpar!')

def q2():
    num1 = float(input('insira um numero:'))
    num2 = float(input('insira outro numero:'))
    print(f'o resultado das 4 operacoes basicas sao')
    round(print(f'\nSoma ({num1} + {num2}) = {num1+num2}'),2)
    round(print(f'\nSubtracao ({num1} - {num2}) = {num1-num2}'),2)
    round(print(f'\nMultiplicacao ({num1} x {num2}) = {num1*num2}'),2)
    round(print(f'\nDivisao ({num1} ÷ {num2}) = {num1/num2}'),2)
    
def q3():
    cont = 1
    while cont < 100:
        print(f'\n{cont}°')
        cont+=1

def q4(numero):
    if numero < 2:
        return False   
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True
numero = int(input("Digite um número: "))
if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")


def q5():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    if(num1 > num2):
        print(f'O valor {num1} é maior do que {num2}')
    elif(num2 > num1):
        print(f'O valor {num2} é maior do que {num1}')
    else:
        print(f'ambos os valores ({num1},{num2}) são iguais')
    
def q6():
    


