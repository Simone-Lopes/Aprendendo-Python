#Aula de Cálculo Computacional 31/08/2023

#Exercício 02

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import statistics as st

#Criando arrays
velocidade = np.array([1/2, 1/4, 1/8, 1/15, 1/30, 1/60, 1/125, 1/250, 1/500, 1/1000])
brilho = [200, 190, 175, 171, 168, 150, 148, 140, 131, 127]

#Utilizando a biblioteca statistics para fazer moda, mediana, decils, variância e desvio
print("Moda dos valores de brilho: {:.02f}%".format(st.mode(brilho)))
print("Mediana dos valores de brilho: {:.02f}%".format(st.median(brilho)))
print("Decils dos valores de briho: ", st.quantiles(brilho, n=10, method='inclusive'))
print("Variância dos valores de brilho: {:.02f}".format(st.variance(brilho)))
print("Desvio de padrão dos valores de brilho: {:.02f}".format(st.stdev(brilho)))

#Criando equação e imprimindo
solucao = stats.linregress(velocidade, brilho)
a_coef_angular, b_coef_linear = solucao.slope, solucao.intercept
print('A equação da reta é: y = {:.04f}x + {:.04f}'.format(a_coef_angular, b_coef_linear))

#Criando gráfico
def formula(a,b,x):
    return a*x + b

def graph(a,b , x_range):
    x = velocidade
    y = formula(a,b,x)
    plt.scatter(velocidade, brilho)
    plt.plot(x,y)
    plt.xticks(np.arange(0, 1, step = 0.1))
    plt.xlabel('Velocidade')
    plt.ylabel('Brilho')
    plt.title('Relação entre velocidade e brilho em fotografias')
    plt.grid()
    plt.show()
    
graph(a_coef_angular, b_coef_linear, range(0,1))


print("Quanto maior a velocidade, menor será o brilho da imagem.")
print("Com base na nossa análise, para obter uma foto com maior índice de brilho, a velocidade do obturador tem que ser menor.")

