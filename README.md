# Cálculo de IMC

Este programa calcula o Índice de Massa Corporal (IMC) do usuário com base no peso e altura fornecidos.

## Como usar

1. Execute o script em Python.
2. Insira seu nome completo.
3. Digite seu peso (em kg).
4. Digite sua altura (em metros).
5. O programa calculará e exibirá seu IMC junto com uma classificação.

## Código

```python
# Solicita os dados do usuário
nome = input('Digite seu nome completo: ')
peso = float(input('Digite seu peso (kg): '))  # Melhor usar float para pesos decimais
altura = float(input('Digite sua altura (m): '))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe os resultados
print(f"""
Olá, {nome}! Tudo bem?
Seu peso é: {peso} kg
Sua altura é: {altura} m
Seu IMC é: {imc:.2f}""")  # Formata o IMC com duas casas decimais

# Classificação do IMC
if imc < 18.5:
    print('"Você está abaixo do peso normal."')
elif 18.5 <= imc <= 24.9:  # Correção da condição
    print('"Você está com o IMC ideal para um adulto."')
else:
    print('"Você está acima do peso."')
```

## Classificação do IMC

| IMC       | Classificação                |
|-----------|------------------------------|
| Menor que 18.5 | Abaixo do peso normal   |
| 18.5 - 24.9 | Peso ideal                 |
| Maior que 24.9 | Acima do peso           |

## Requisitos

- Python 3.x instalado

## Executando o programa

Salve o código como `imc.py` e execute no terminal ou prompt de comando com:

```bash
python imc.py
