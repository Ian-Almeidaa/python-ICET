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

def q4():
    num = int(input("Digite um número: "))
    if num <= 1:
        teste = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} não é primo.")
            break
        print(f"{num} é primo.")

    """if teste == True:
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")"""

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
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    num3 = float(input("Digite o terceiro valor: "))
    if num1 > num2 and num1 > num3:
        print(f'O maior valor é {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'O maior valor é {num2}')
    elif num3 > num1 and num3 > num2:
        print(f'O maior valor é {num3}')

def q7():
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    num3 = float(input("Digite o terceiro valor: "))
    maior = 0
    menor = 0
    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    elif num3 > num1 and num3 > num2:
        maior = num3

    if num1 < num2 and num1 < num3:
        menor = num1
    elif num2 < num1 and num2 < num3:
        menor = num2
    elif num3 < num1 and num3 < num2:
        menor = num3

    print(f'a diferença entre o maior número ({maior}) e o menor número ({menor}) é de {maior-menor}')    

def q8():
    base = float('-inf')
    soma = 0
    quantidade = 0

    while True:
        numNew = float(input('Digite um número: '))
        if numNew < base:
            break

        soma += numNew
        quantidade += 1
        base = numNew

    media = soma / quantidade

    print(f'Ao total foram digitados {quantidade} números, a média deles foram {media} e a soma total foi de {soma}')

def q9():
    cont = int(input('Digite quantos números serão comparados: '))
    maior = float(input('Digite o 1° número: '))
    for i in range(2,cont + 1):
        num = float(input(f'Digite o {cont}° número: '))
        if num > maior:
            maior = num
    
    print(f'O maior número entre os {cont} números foi {maior}')

def q10():
    worldA = 90000000
    worldB = 200000000
    year = 0
    while worldA < worldB:
        worldA += (worldA/100)*3
        worldB += (worldB/100)*1.5
        year += 1

    print(f'foi preciso {year} anos para o País A passar o País B')

def q11():
    numero = input("Digite um número inteiro: ")
    algarismo = input("Digite um algarismo (0 a 9): ")

    if len(algarismo) != 1 or not algarismo.isdigit():
        print("Erro: você deve digitar um único algarismo entre 0 e 9.")
    else:
        if algarismo in numero:
            print(f"O algarismo {algarismo} aparece no número {numero}.")
        else:
            print(f"O algarismo {algarismo} não aparece no número {numero}.")

def q12():
    char = input("Digite um caractere: ")

    if len(char) != 1:
        print("Erro: Você deve digitar apenas um único caractere.")
    else:
        if char.isupper():
            print(f"O caractere '{char}' é uma letra maiúscula.")
        elif char.islower():
            print(f"O caractere '{char}' é uma letra minúscula.")
        elif char.isdigit():
            print(f"O caractere '{char}' é numérico.")
        else:
            print(f"O caractere '{char}' é um símbolo especial.")
