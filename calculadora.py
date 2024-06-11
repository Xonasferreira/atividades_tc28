#   definindo a função

def calculadorapy1(num1, num2, operador) :

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

#   saida de dados

resultado = calculadorapy1(2, 3, 1)
print("Resultado do calculo: " + str (resultado))