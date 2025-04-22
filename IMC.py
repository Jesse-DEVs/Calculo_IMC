def calcular_imc(peso, altura):
    return peso/ altura ** 2

def classificar_imc(imc):
    imc = round(imc, 1)  # Arredondar o IMC para 1 casas decimais
    
    if imc <= 18.5:
        return 'Abaixo do peso'
    elif 18.5 < imc <= 24.9:
        return 'Peso normal'
    elif 25 <= imc <= 29.9:
        return 'Sobrepeso'
    elif 30 <= imc <= 34.0:
        return 'Obesidade Grau 1'
    elif 35 <= imc <= 39.9:
        return 'Obesidade Grau 2'
    else:
        return 'Obesidade Grau 3 (obesidade mórbida)'
    
def main():
    pessoas= []
    
    while True:
        name = input('Digite seu nome completo: ')
        try:
            peso = float(input('Digite seu pesso (Kg): '))
            altura = float(input('Digite sua alturua (m): '))
        except ValueError:
            print("Por favor, insira um valor numérico válido para peso e altura.")
            continue   
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        pessoas.append({'name': name, 'imc': imc, 'classificacao': classificacao})
        
        print(f"""\n Olá {name}, tudo bem ?  
Seu peso é: {peso} Kg              
Sua altura é: {altura}m              
Seu IMC é: {imc:.1f}              
Classificação: {classificacao}              
""")
        
        continuar = input('Deseja calcular o IMC de outra pessoa? (sim/nao): ').strip().lower()
        if continuar != 'sim':
            break
    
        
    print("\nResumo dos resultados:")
    for pessoa in pessoas:
        print(f"Nome: {pessoa['name']} - IMC: {pessoa['imc']:.2f} - Classificação: {pessoa['classificacao']}")    
     
if __name__ == "__main__":
    main()        