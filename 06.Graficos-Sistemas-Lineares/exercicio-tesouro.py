#Aula de Cálculo Computacional 31/08/2023

#Exercício 01

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import statistics as st

#Criando array
vencimento = np.array([18, 5, 11, 9, 14, 6, 13, 8, 22, 15, 7, 20, 19, 16, 21, 10, 17, 12])
yield_porcentagem = np.array([2.9, 4.2, 3.2, 3.8, 4.0, 4.5, 3.4, 3.7, 2.1, 4.7, 4.3, 2.7, 2.5, 4.1, 2.3, 3.5, 3.2, 3.6])

#Utilizando a biblioteca statistics para fazer média, mediana e desvio de padrão
print("Média de rendimentos do título: {:.02f}%".format(st.mean(yield_porcentagem)))
print("Mediana de rendimentos do título: {:.02f}%".format(st.median(yield_porcentagem)))
print("Desvio de padrão dos rendimentos do título: {:.02f}%".format(st.stdev(yield_porcentagem)))

#Definindo coeficiente angular e linear para criar equação
solucao = stats.linregress(vencimento, yield_porcentagem)
a_coef_angular, b_coef_linear = solucao.slope, solucao.intercept

#Imprimindo equação
print('A equação da reta é: y = {:.04f}x + {:.04f}'.format(a_coef_angular, b_coef_linear))

#Criando gráfico
def formula(a,b,x):
    return a*x + b

def graph(a,b , x_range):
    x = vencimento
    y = formula(a,b,x)
    plt.scatter(vencimento, yield_porcentagem) #Valores de x e y
    plt.plot(x,y)
    plt.xticks(np.arange(5, 40, step = 5))#Configurações do gráfico
    plt.xlabel('Vencimento')#eixo x
    plt.ylabel('Yield') #eixo y
    plt.title('A relação entre os rendimentos do título e os períodos de vencimento.') #título
    plt.grid()
    plt.show()
    
graph(a_coef_angular, b_coef_linear, range(5,35))


print("Quanto menor o tempo de vencimento, maior a porcentagem do yield.")
print("Com base na nossa análise, recomendamos reduzir o tempo de vencimento.")
