#   função 
def calculadorapy3():
    while True:
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        #   Entrada do tipo da operção 
        operacao = input("Digite o número da operação: ")

        #   se a operação for igual a zero,parar laço de rpetição
        if operacao == '0':
            print("Encerrando a calculadora.")
            break
        
        #   se a opção de operação não estiver na lista,continue o laço
        if operacao not in ['1', '2', '3', '4']:
            print("Essa opção não existe. Tente novamente.")
            continue
        
        #   entrada de numerica e verificação de tipo 
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

        #   tipo não permitido e impressão de erro
        except ValueError:
            print("Entrada inválida! Por favor, insira números válidos.")
            continue
        #   processamento dos dados inseridos 
        if operacao == '1':
            resultado = num1 + num2
            print("Resultado: " + str(num1) + " + " + str(num2) + " = " + str(resultado))
        elif operacao == '2':
            resultado = num1 - num2
            print("Resultado: " + str(num1) + " - " + str(num2) + " = " + str(resultado))
        elif operacao == '3':
            resultado = num1 * num2
            print("Resultado: " + str(num1) + " * " + str(num2) + " = " + str(resultado))
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado: " + str(num1) + " / " + str(num2) + " = " + str(resultado))
            else:
                print("Erro: Divisão por zero não é permitida.")


# saida dos dados processados
calculadorapy3()
