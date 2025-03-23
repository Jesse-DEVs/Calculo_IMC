while True:
    nome = input(' Digite Seu Nome Completo: ')
    
    nota_Mat = float(input(' Digite Sua Nota de Matematica (exemplo: 10.0) '))
    
    if 0 <= nota_Mat <10.0:
        break
    else:
        print('Digite um numero valido! ')
while True:
    nota_Port = float(input(' Digite Sua Nota de Portugues (exemplo: 10.0): '))
    
    if 0 <= nota_Port <10.0:
        break
    else:
        print('Digite um numero valido! ')
while True:
    nota_Ingles = float(input(' Digite Sua Nota de Ingles (exemplo: 10.0): '))

    if 0 <= nota_Ingles <10.0:
        break
    else:
        print('Digite um numero valido! ')
        
while True:
    nota_Hist = float(input(' Digite Sua Nota de Historia (exemplo: 10.0): '))

    if 0 <= nota_Hist <10.0:
        break
    else:
        print('Digite um numero valido! (exemplo: 10.0): ')


print(f' Ola {nome}, Tudo bem ?')
print(f'Nota de Matematica: {nota_Mat}')
print(f'Nota de Portugues: {nota_Port}')
print(f'Nota de Inglês: {nota_Ingles}')
print(f'Nota de Historia: {nota_Hist}')

Soma = nota_Mat + nota_Port + nota_Ingles + nota_Hist

resultado = Soma/4 
print(f'{nome} Sua media de nota foi: {resultado:.1f}')

if (resultado <= 5 ):
    print(f'{nome} Infelizmente voce foi reporvado')

elif (resultado > 5 ):
    print(f'{nome} Parabéns Você foi Aprovado!!')
    
    
