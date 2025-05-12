# Calculadora
for calculadora in range(50):
    try:
        num1 = float(input("Digite o primeiro número a ser calculado:"))
    except:
        print('Os comandos funcionam apenas com números')
    try:
        num2 = float(input("Digite o segundo número a ser calculado:"))
    except:
        print('Os comandos funcionam apenas com números')

    print('Selecione uma das opções a seguir: Soma = 1, Subtração = 2, Divisão = 3, Multiplicação = 4')
    selecao = int(input("Selecione a operação matemática:"))

    if selecao == 1:
        resultado = num1 + num2
    elif selecao == 2:
        resultado = num1 - num2
    elif selecao == 3:
        resultado = num1 / num2
    elif selecao == 4:
        resultado = num1 * num2
    else:
        print('try again'),
        continue
    print(resultado)
