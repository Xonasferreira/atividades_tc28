def calculadora_py (num1, num2, operador) :
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


print("CALCURADORA PYTHON\n")
#entrada de dados
num1 = float (input("Digite o primeiro numero:"))
operador = float(input("Digite a referencia do operador:"))
num2 = int(input("Digite o segundo numero:"))


resultado = calculadora_py(num1,num2,operador)
print("Resultado do calculo:" + str(resultado))