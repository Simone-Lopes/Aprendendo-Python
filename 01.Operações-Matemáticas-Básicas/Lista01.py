#Simone Lopes dos Santos
#Lista de exercícios 01

# Exercício 01
a = 2
a_elevado_cubo = pow(a, 3)

r1 = a_elevado_cubo

#Exercício 02

b = -2
b_elevado_cubo = pow(b, 3)

r2 = b_elevado_cubo

#Exercício 03

c = 1
c_elevado_cubo = pow(c, 3)

r3 = c_elevado_cubo

#Exercício 04

d = -1
d_elevado_zero = pow(c, 0)

r4 = d_elevado_zero

#Exercício 05

e = 2
e_elevado_zero = pow(e, 0)

r5 = e_elevado_zero

#Exercício 06

f = 2 / 5
f_elevado_cubo = pow(f, 3)

r6 = f_elevado_cubo

#Exercício 07

g = 3
g_elevado_quadrado = pow(g, -2)

r7 = g_elevado_quadrado

#Exercício 08

h = 1 / 2
h_elevado_cubo = pow(h, -3)

r8 = h_elevado_cubo

#Exercício 09

j = -1
j_elevado_cubo = pow(j, 3)
j_elevado_quarta = pow(j_elevado_cubo, 4)

r9 = j_elevado_quarta

#Exercício 10

k = 0.5
k_elevado_cubo = pow(k, 3)

r10 = k_elevado_cubo

#Exercício 11

k = 0.25
k_elevado_quarta = pow(k, 4)

r11 = k_elevado_quarta

#Exercício 12

l = 0
l_elevado_quarta = pow(l, 4)

r12 = l_elevado_quarta

#Exercício 13

m = 1 + 0.41
m_elevado_quadrado = pow(m, 2)

r13 = m_elevado_quadrado

#Exercício 14

n = 5
n_elevado_quadrado = pow(n, 2)

o = -2
o_elevado_quarta = pow(o, -4)

p = 1 / 4

r14 = p + n_elevado_quadrado + o_elevado_quarta

#Exercício 15

q = 2
q_elevado_cubo = pow(q, -3)

r = -4
r_elevado_quinta = pow(r, -5)

r15 = q_elevado_cubo + r_elevado_quinta

#Exercício 16

s = 4 / 5
t = 1 / 2
s_com_t = s - t + 1

s_t_elevado_quadrado = pow(s_com_t, -2)

u = 3
u_elevado_quadrado = pow(u, 2)
v = 4 - 5
v_elevado_quadrado = pow(v, -2)
u_com_v = 1 + u_elevado_quadrado - v_elevado_quadrado

r16 = s_t_elevado_quadrado + (1 / u_com_v)


#Armazenando respostas em vetor e printando para o usuário
respostas =[r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16]

i = 1
exercicio = 1

for i in range (len(respostas)):
    print("Resposta", exercicio, ":", "%.2f" % respostas[i])
    i += 1
    exercicio += 1

