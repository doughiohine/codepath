# Atribuição de valores a variáveis
nome = "Douglas"
idade = 29

# entrada de dados
try:
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    
    # Verifica se altura é válida
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")

    # calculo do IMC:
    imc = peso / (altura ** 2)

    # saída de dados formatada
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura:.2f}m")
    print(f"Peso: {peso:.1f}kg")
    print(f"IMC: {imc:.2f}")

except ValueError as ve:
    print(f"Erro de valor: {ve}")
except Exception as e:
    print(f"Erro inesperado: {e}")

