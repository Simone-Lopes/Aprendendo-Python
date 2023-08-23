# Desafio Teoria dos Conjuntos

# Inserindo tickets de corretoras

Agora = set(['ITSA4', 'ECOR3','TAEE11', 'B3SA3', 'VALE3'])

Ativa = set(['B3SA3', 'BBDC4', 'BBSE3', 'BRDT3', 'TAEE11', 'TRPL4', 'VALE3', 'VIVT3'])

Genial = set(['CPFE3', 'BEEF3', 'CYRE3', 'SAPT4', 'TRPL4'])

Easynvest = set(['B3SA3', 'AGRO3', 'COCA34', 'TAEE11', 'VALE3', 'CPLE11', 'ITSA4', 'ABEV3'])

Elite = set(['BBDC4', 'BBSE3', 'BRSR6', 'EGIE3', 'ITSA4', 'SAPR11', 'TAEE11', 'TRPL4', 'VIVT3', 'VALE3'])

Guide = set(['ALUP11', 'BBAS3', 'CYRE3', 'CPFE3', 'KLBN11', 'PSSA3', 'TIMS3', 'VALE3'])

Nova_Futura = set(['B3SA3', 'CYRE3', 'GGBR4', 'VIVT3', 'TRPL4'])

Orama = set(['ABCB4', 'BBDC4', 'BEEF3', 'CESP6', 'EGIE3'])


#Intersecção entre todas as corretoras

acao_comum = Agora.intersection(Ativa, Genial, Easynvest, Elite, Guide, Nova_Futura, Orama)
print('Ação comum entre todas as corretoras:', acao_comum)

#Escolhendo 4 corretoras
# Agora, Easynvest, Elite, Orama

#Ação comum entre as 4 corretoras - Intersecção

acao_comum_4 = Agora.intersection(Easynvest, Elite, Orama)
print('Ação comum entre as 4 as corretoras:', acao_comum_4)

#Diferença entre as 4 corretoras - Diferença
dif_Agora = Agora - Easynvest - Elite - Orama
print('Ações unicas da Agora: ', dif_Agora)

dif_Easynvest = Easynvest - Agora - Elite - Orama
print('Ações unicas da Easynvest: ', dif_Easynvest)

dif_Elite = Elite - Easynvest - Agora - Orama
print('Ações unicas da Elite: ', dif_Elite)

dif_Orama = Orama - Easynvest - Agora - Elite
print('Ações unicas da Orama: ', dif_Orama)

#Relações entre portifólios das corretoras - Pertinência

print('Há relações entre Agora e Easynvest?', Agora.issubset(Easynvest))
print('Há relações entre Agora e Elite?', Agora.issubset(Elite))
print('Há relações entre Agora e Orama?', Agora.issubset(Orama))

print('Há relações entre Easynvest e Elite?', Easynvest.issubset(Elite))
print('Há relações entre Easynvest e Orama?', Easynvest.issubset(Orama))

print('Há relações entre Elite e Orama?', Elite.issubset(Genial))

#Ações únicas de cada corretora - Diferença simétrica

acoes_unicas = Agora ^ Easynvest ^ Elite ^ Orama
print('Ações únicas de cada corretora:', acoes_unicas)




