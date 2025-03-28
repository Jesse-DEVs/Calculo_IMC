

nome = input(' Digite seu nome completo: ')
peso = int(input(' Digite sue peso: '))
altura = float(input(' Digite sua altura: '))

imc = peso / (altura ** 2)

    
print(f""" Ola {nome} Tudo bem ? 
{nome} Seu peso é: {peso}
{nome} Sua altura é: {altura}
{nome} Então seu IMC é: {imc}
""")
if imc <= 18.5:
    print(' "voce esta abaixo do peso normal" ')
elif imc > 18.5  < 24.9:
    print(' "Voce esta com o IMC ideal para um adulto" ')
else:
    print(' "Voce esta acima do peso" ')   
    