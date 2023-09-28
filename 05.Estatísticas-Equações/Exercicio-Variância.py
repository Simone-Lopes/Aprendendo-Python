from scipy import stats
import numpy as np
import sympy as sp
import statistics as st


ram = [5.3669, 5.3850, 5.4076, 5.3835, 5.4025, 5.4561, 5.4197, 5.4306, 5.4700, 5.5270, 5.5752, 5.5445, 5.6290, 5.6267, 5.6937, 5.6422, 5.7013, 5.6983, 5.6562, 5.5151, 5.4860, 5.4454, 5.4566, 5.5377, 5.5709, 5.5448]

print("Média: {:.04f}%".format(st.mean(ram)))
print("Mediana: {:.04f}%".format(st.median(ram)))
print("Desvio de padrão da amostra:{:.4f}".format(st.stdev(ram)))
print("Variancia da amostra: {:.04f}".format(st.variance(ram)))
print("Desvio de padrão da população: {:.04f}".format(st.pstdev(ram)))
print("Variancia populacional: {:.04f}".format(st.pvariance(ram)))


