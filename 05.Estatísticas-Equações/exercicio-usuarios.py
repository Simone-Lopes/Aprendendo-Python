#Atividade Sistemas Lineares e Não Lineares
#Simone Lopes e Rita de Cássia

import sympy as sp
import statistics as st

hora = ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
usuarios = [10, 12, 15, 25, 22, 18, 15, 20, 28, 30]
cpu = [20.0, 25.2, 30.0, 45.1, 42.7, 33.6, 31.5, 45.0, 53.1, 60.2]

print("Média de usuários: {:.02f}".format(st.mean(usuarios)))
print("Mediana de usuários: {:.02f}".format(st.median(usuarios)))
print("Desvio de padrão de usuários ativos: {:.02f}".format(st.stdev(usuarios)))


