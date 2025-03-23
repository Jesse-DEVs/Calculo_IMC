def big_mac():
    print('bih mac')


big_mac()


print('fim')
def fazer_big_mac(nome):
    print(f'sanduiche big mac: {nome}')

fazer_big_mac('jesse')
fazer_big_mac('abrewu')
fazer_big_mac('julia')

def fazer_batata(tamanho):
   print(f'batata {tamanho}')

def refrigerante(tipo,tamanho):
    print(f'{tipo},{tamanho}')

fazer_big_mac('jesse')         
fazer_batata('grande')
#efrigerante('coca',' medio')

def fazer_combo_bigmac(nome,tamanho_da_batata,tipo_refrigerante,tamanho_refrigerante):
   fazer_big_mac(nome)
   fazer_batata(tamanho_da_batata)
   refrigerante(tipo_refrigerante,tamanho_refrigerante)
fazer_combo_bigmac('jesse','grande','Coca','pequena')   



def soma_numeros(numero1,numero2):
    return numero1 + numero2

resultado = soma_numeros(20,10)
print(resultado)

def maior_numero(lista_numeros):
    lista_numeros.sort()
    lista_numeros.reverse()
    maior_numero = lista_numeros[0]
    return maior_numero

resultado = maior_numero([-11,-35,-73,-36,-24,])
print(resultado)

