#   defenindo função

def calculadorapy(num1, num2, operador) :

    if operador == 1 :
        return num1 + num2
    elif operador == 2 :
        return num1 - num2
    elif operador == 3 :
        return num1 * num2 
    elif operador == 4 :
        if num2 != 0 :
            return num1 / num2 
        else :
            print("ERRO: Não é possível divisão po zero")
            return 0
    else :
        return 0

#   entrada de dados

num1 = float (input("Digite o primeiro número:"))
operador = float(input("Digite a referencia do operador:"))
num2 = int(input("Digite o segundo número:"))

#   saida de dados

resultado = calculadorapy(num1, num2, operador)
print(f"Resultado do calculo: {resultado}")