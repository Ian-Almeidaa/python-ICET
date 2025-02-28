from datetime import date, datetime

def ex1():
    valorProduto = round(float(input("Digite o valor do produto: ")),2)
    codigoPromocional = int(input("Digite o código promocional: "))
    
    if codigoPromocional == 33:
        print(f"O valor original do produto é de R${valorProduto}, /n e o valor com desconto de 10% é de R${round((valorProduto - (valorProduto/10)),2)}")
    elif codigoPromocional == 77:
        print(f"O valor original do produto é de R${valorProduto}, /n e o valor com desconto de 20% é de R${round((valorProduto - (valorProduto/15)),2)}")
    elif codigoPromocional == 230:
        if valorProduto > 100:
            print(f"O valor original do produto é de R${valorProduto}, /n e o valor com desconto de 30% é de R${round((valorProduto - (valorProduto/30)),2)}")
        else :
            print(f"O valor original do produto é de R${valorProduto}, /n e o valor com desconto de 25% é de R${round((valorProduto - (valorProduto/20)),2)}")

def ex2():
    salarioFixo = round(float(input("Digite o salario fixo: ")),2)
    numeroVendas = int(input("Digite o número de vendas: "))
    if numeroVendas < 100 and numeroVendas >= 500:
        print(f"O seu salário ficou de R${salarioFixo + 500}, Você ganhou um prêmio de R$500,00")
    elif numeroVendas < 500 and numeroVendas >= 750:
        print(f"O seu salário ficou de R${salarioFixo + 700}, Vocé ganhou um prêmio de R$700,00")
    elif numeroVendas < 750:
        print(f"O seu salário ficou de R${salarioFixo + 1000}, Vocé ganhou um prêmio de R$1000,00")

def ex3():
    hoje = datetime.today()
    data_str = input("Data de Nascimento (dd/mm/yyyy): ")
    dataNascimento = datetime.strptime(data_str, "%d/%m/%Y")
    idade = int((hoje - dataNascimento).days/ 365)

    if idade >= 16:
        print(f"Vocé tem {idade} anos, já pode votar") 

def ex4():
    num = int(input("Digite um número: "))
    if num % 2 == 0 and num > 10:
        print("SIM")
    elif num % 2 == 1 and num < 50:
        print("SIM")
    else:
        print("NÃO")
def ex5():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    num3 = int(input("Digite outro número: "))

    if num1 > num2 and num1 > num3:
        print(f"O maior número é {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"O maior número é {num2}")
    else:
        print(f"O maior número é {num3}")

def ex6():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    num3 = int(input("Digite outro número: "))
    maior = 0
    menor = 0
    meio = 0

    if num1 > num2 and num1 > num3:
        maior = num1
        if num2 < num3:
            menor = num2
            meio = num3
        else:
            menor = num3
            meio = num2
    elif num2 > num1 and num2 > num3:
        maior = num2
        if num1 < num3:
            menor = num1
            meio = num3
        else:
            menor = num3
            meio = num1
    else:
        maior = num3
        if num1 < num2:
            menor = num1
            meio = num2
        else:
            menor = num2
            meio = num1

    print(f" A ordem correta é {menor} / {meio} / {maior}")

def ex7():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 6:
        print("APROVADO")
    elif media >= 4:  
        print("RECUPERACAO")
    else:
        print("REPROVADO")

def ex8():
    num = int(input("Digite um número: "))
    if num % 5 == 0 and num % 3 == 0:
        print(f"{num} é divisível por 5 e 3")

def ex9():
    i = 0
    soma = 0
    while i < 5:
        num = int(input("Digite um número: "))
        soma += num
        i += 1
    print(f"A média dos valores é {soma / 5}")

def ex10():
    idade = int(input("Digite a idade: "))
    soma = 0
    count = 0
    while idade != 0:
        soma += idade
        idade = int(input("Digite a idade: "))
        count += 1
    print(f"A média das idades é {soma / count}")

def ex11():
    saldo = 0
    opcao = input("\nA)Cosultar Saldo\nB)Saque\nC)Deposito\nD)Sair\nDigite uma opção: ")
    while opcao != 'D' or opcao != 'd':
        if opcao == 'A' or opcao == 'a':
            print(f"\nSeu saldo é R${saldo}")
        elif opcao == 'B' or  opcao == 'b':
            valor = float(input("\nDigite o valor do saque R$"))
            if valor > saldo:
                print("\nSeu saldo é insuficiente!")
            else:
                saldo -= valor
        elif opcao == 'C' or opcao == 'c':
            valor = float(input("\nDigite o valor do deposito R$"))    
            saldo += valor
        opcao = input("\nA)Cosultar Saldo\nB)Saque\nC)Deposito\nD)Sair\nDigite uma opção: ")

def ex12():
    num = int(input("Digite um número: "))
    if num <= 1:
        teste = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} não é primo.")
            break
        print(f"{num} é primo.")

questao = int(input('Questão a ser executada (1-12): '))
eval(f'ex{questao}()')