lista_de_numeros = [20,8,23,25,7,50,10,28,17,28,15,54,37]
lista_de_numeros_2 = [20,8,23,25,7,50,10]
lista_de_numeros_3 = [4,5,6]

print(len(lista_de_numeros))

def calcular_media(lista_para_somar: list) -> float:
    soma = 0
    for item in lista_para_somar:
        soma = soma + item
    media_da_lista = soma / len(lista_para_somar)
    return media_da_lista

def calcular_variancia(lista):
    media = calcular_media(lista)
    soma_diferencas = 0
    for valor in lista:
        diferenca = valor - media
        soma_diferencas += diferenca ** 2
    variancia = soma_diferencas / len(lista)
    return variancia

def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

media_1 = calcular_media(lista_de_numeros)
media_2 = calcular_media(lista_de_numeros_2)
media_3 = calcular_media(lista_de_numeros_3)

print(media_1)
print(media_2)
print(media_3)

