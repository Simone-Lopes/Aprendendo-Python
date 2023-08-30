#Aula de Cálculo Computacional com Python 29/08 2023
#Estatística descritiva e sistemas lineares e não lineares

import statistics as st

#Mediana
set1 = [1,3,3,4,5,7]
print("A mediana da base é {:.2f}".format(st.median(set1)))

#Moda
set2 = [2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7]
set3 = [2.4, 1.3, 1.3, 1.3, 2.4, 4.6]
set4 = ["red", "blue", "black", "blue", "black", "black", "brown"]
print("A moda do data set 2 é % s" % (st.mode(set2)))
print("A moda do data set 3 é % s" % (st.mode(set3)))
print("A moda do data set 4 é % s" % (st.mode(set4)))

#Máximo e minímo
arr = [1, 2, 3, 4, 5, -2, -4, -3, -1, -5, -6, 1, 2, 5, 4, 8, 9, 12]
Maximum = max(arr)
Minimum = min(arr)
#A diferença entre o valor máximo e minímo
Range = Maximum - Minimum 
print("Maximum = {}, Minimum = {} e Range = {}".format(Maximum, Minimum, Range))
print("Variância de arr é {:.02f}".format(st.variance(arr)))
print("O desvio padrão de arr é {:.02f}".format(st.stdev(arr)))

#Quartil
print(st.quantiles(arr, n=4, method='inclusive'))
print(st.quantiles(arr, n=10, method='inclusive'))
#Alteramos a divisão de amostra para ganhar precisão



