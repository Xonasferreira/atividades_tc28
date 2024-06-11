#função para calcular idade 
def calcular_idade (ano_nascimento):
    ano_atual = 2024
    return ano_atual - ano_nascimento
#função para receber e tester a data de nascimento
def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021):"))
            if  ano_nascimento < 1922 or ano_nascimento > 2021:
                raise ValueError("O ano inserido não é válido")
            return ano_nascimento
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira um ano válido.")

# funão para receber o nome e unir as outras funções
def unix ():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print (f"Nome: {nome_completo} | Idade: {idade}")

#condiçao para não ocorrer conflito modular 
if __name__ == "__main__":
    unix() 