#Aula de Cálculo Computacional 29/08/2023
#Equações lineares e não-lineares

#Instalar e importar biblioteca
import sympy as sp

#Declarando os simbolos da minha equação
m, b = sp.symbols('m b')

eq1 = sp.Eq(m*11 + b,120)
eq2 = sp.Eq(m*19 + b,150)
eq3 = sp.Eq(m*35 + b,180)
eq4 = sp.Eq(m*43 + b,210)
eq5 = sp.Eq(m*72 + b,240)

#Tentando resolver as equações com apenas dois simbolos
ans = sp.solve((eq1,eq2,eq3,eq4,eq5),(m,b))

print(ans)

#esses pontos não são uma reta perfeita, então temos que trabalhar com combinações de pontos para formar a reta
ans1 = sp.solve((eq1,eq5),(m,b))
ans2 = sp.solve((eq2,eq4),(m,b))
ans3 = sp.solve((eq1,eq3),(m,b))
print(ans1)
print(ans2)
print(ans3)
print(float(ans2.get(b)))

#Resolvendo combinações com listas
ans1 = list(sp.linsolve((eq1,eq5),(m,b)))
ans2 = list(sp.linsolve((eq2,eq4),(m,b)))
ans3 = list(sp.linsolve((eq1,eq3),(m,b)))
print(ans1)
print(ans2)
print(ans3)
print(round(ans3[0][1],2))

#todos possuem algum erro associado. Mais para frente utilizaremos regressão linear para trabalhar com um melhor modelo que explique essa situação. 
