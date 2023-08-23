#Aula de teoria dos conjuntos

#Criando conjuntos utilizando chaves
conjunto_processador = {'CPU', 'Registrador', 'Core'}
print(conjunto_processador)

#Mesmo conjunto com comando set
conjunto_processador = set (['CPU', 'Registrador', 'Core'])
print(conjunto_processador)


#O comando set garante a criação de uma lista com elementos que não se repetem
lista_processador = {'CPU', 'Registrador', 'Core'}
conjunto_processador2 = set (lista_processador)
print(conjunto_processador)

#Conjunto vazio para ver as diferenças de type
teste = {}
print(type(teste))

teste2 = set(teste)
print(type(teste2))

#Criando conjuntos

user_Thor = {'mysql', 'CPU', 'RAM', 'SSD1', 'Google'}
user_Thanos = {'LOL', 'RAM', 'CPU', 'HD', 'Google'}
user_CA = {'mysql', 'LOL', 'RAM', 'CPU', 'Firefox'}
user_TS = {'mysql', 'CPU', 'RAM', 'SSD1', 'Google'}

#---------------------------------------
#UNIÃO de dois conjuntos

print('União')
inventario1 = user_Thor | user_CA
print(inventario1)

inventario2 = user_Thor | user_CA | user_Thanos | user_TS
print(inventario2)

#Outra forma de executar - UNION
inventario3 = user_Thor.union(user_CA)
print(inventario3)

inventario4 = user_Thor.union(user_CA, user_Thanos, user_TS)
print(inventario4)

#---------------------------------------
#INTERSECÇÃO de dois conjuntos

print('Interseção')
inventario1 = user_Thor & user_CA
print(inventario1)

#Outra forma de executar - INTERSECTION
inventario2 = user_Thor.intersection(user_Thanos)
print(inventario2)

inventario3 = user_Thor.intersection(user_CA, user_Thanos, user_TS)
print(inventario3)

#---------------------------------------
#DIFERENÇA de dois conjuntos

print('Diferença')
inventario1 = user_Thor - user_CA
print(inventario1)

inventario2 = user_Thor - user_CA - user_Thanos - user_TS
print(inventario2)

#---------------------------------------
#PERTINENCIA exibe como resultante a booleana, verdadeira ou falsa

print('Pertinência')
print('CPU' in user_TS)
print('Firefox' in user_Thanos)

print('LOL' not in user_Thor)
print('LOL' not in user_Thanos)

#Pertinência com subconjuntos e superconjuntos (subset (<=) e superset(>=))

print(user_Thor.issubset(user_Thanos))
print(user_Thor.issubset(user_TS))

#Outra forma de fazer 

print(user_Thor <= user_TS)
print(user_Thor <= user_Thanos)

#Testando superconjuntos

print(user_TS.issuperset(user_Thor))
print(user_TS >=(user_Thor))

#---------------------------------------
#IGUALDADE entre dois conjuntos

print('Igualdade')
print(user_TS == (user_Thor))
print(user_TS != (user_Thor))
print(user_TS == (user_CA))
print(user_TS != (user_CA))


#---------------------------------------
#DIFERENÇA SIMÉTRICA
#Um novo conjunto surge, contendo todos os elementos que não são comuns aos dois conjuntos.

print(user_TS ^ user_CA)








