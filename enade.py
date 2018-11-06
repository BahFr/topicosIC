#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Bárbara Freitas, Mayara Assis, Francelino Giordani'''

import pandas
import matplotlib.pyplot as plt
import scipy.stats as stats
enade2017=pandas.read_csv("MICRODADOS_ENADE_2017.txt", sep=';',dtype={"DS_VT_ESC_OFG": str, 
                                                                               'DS_VT_ESC_OCE':str,
                                                                              'DS_VT_ACE_OCE':str,
                                                                              'NT_GER':str,
                                                                              'NT_FG':str,
                                                                              'NT_OBJ_FG':str,
                                                                              'NT_DIS_FG':str,
                                                                              'NT_CE':str,
                                                                              'NT_OBJ_CE':str,
                                                                              'NT_DIS_CE':str})


print(enade2017.shape)
print(enade2017.columns[0:10])

"""

   QE_I22
Excetuando-se os livros indicados na bibliografia do seu curso, quantos livros você leu neste ano?
A = Nenhum.
B = Um ou dois.
C = De três a cinco.
D = De seis a oito.
E = Mais de oito.

NT_DIS_FG
Nota bruta na parte discursiva de formação geral

NT_DIS_CE
Nota bruta na parte discursiva de formação específica
"""
tabela = pandas.DataFrame(enade2017, columns=['NT_DIS_FG', 'NT_DIS_CE','CO_GRUPO','NT_GER','QE_I22'])
print(tabela.head(10))

#LIMPEZA DE DADOS 
#substitui vírgula por ponto

tabela['NT_DIS_FG'] = tabela['NT_DIS_FG'].str.replace(',', '.')
tabela['NT_DIS_CE'] = tabela['NT_DIS_CE'].str.replace(',', '.')

"""
print (tabela['NT_DIS_FG'])
print (tabela['NT_DIS_CE'])
"""
'''
Tipo de presença na parte discursiva na formação geral
222 = Ausente
556 = Participação com resultado desconsiderado pela Aplicadora
888 = Participação com resultado desconsiderado pelo Inep

Portanto, algumas notas podem ser desconsideradas dependendo do seu objetivo, 
e aqui, será de calcular a média daqueles que fizeram a prova.
'''

tabela=tabela.loc[(tabela['NT_DIS_FG'].notnull())]
#converte de str para float
print("media FG")
tabela['NT_DIS_FG'] = pandas.to_numeric(tabela['NT_DIS_FG'])
#print(tabela['NT_DIS_FG'])
print(tabela['NT_DIS_FG'].mean())

tabela=tabela.loc[(tabela['NT_DIS_CE'].notnull())]
#converte de str para float
print("Media CE")
tabela['NT_DIS_CE'] = pandas.to_numeric(tabela['NT_DIS_CE'])
#print(tabela['NT_DIS_CE'])
print(tabela['NT_DIS_CE'].mean())
print("\n")

"""
print(tabela['NT_DIS_FG'].describe())
print(tabela['NT_DIS_CE'].describe())
print("\n")
"""
#outros comandos
print('Parte discursiva formação geral')
print('indice da primeira maior nota: ', tabela['NT_DIS_FG'].idxmax())
print('Maior nota: ', tabela['NT_DIS_FG'][13594])
#print(tabela['NT_DIS_FG'].idxmax())
print("\n")

print('Parte discursiva formação específica')
print('indice da primeira maior nota: ', tabela['NT_DIS_CE'].idxmax())
print('Maior nota: ', tabela['NT_DIS_CE'][154])
#print(tabela['NT_DIS_CE'].idxmax()) 
print("\n")

#Calcula a média de um curso especifico
#Código da área de enquadramento do curso no Enade == ciencia da computacao
print("\n COMPUTACAO")
ccomp = tabela[tabela['CO_GRUPO']==4004]
print(ccomp)

print("\n DADOS COMPUTACAO GERAL")
#somente as notas de quem respondeu a questão sobre livros Formação GERAL 
ccomp=ccomp.loc[(ccomp['QE_I22'].notnull())]
print(ccomp.NT_DIS_FG.describe())

print("\n DADOS COMPUTACAO ESPECIFICA")
#Formação ESPECÍFICA
ccomp=ccomp.loc[(ccomp['QE_I22'].notnull())]
print(ccomp.NT_DIS_CE.describe())

ccomp.QE_I22.head(10)

ccomp['QE_I22'] = ccomp['QE_I22'].map({'A': 1, 'B': 2, 'C': 3, 'D': 4,'E': 5})

print(ccomp.QE_I22.head(10))

print("grafico NT_DIS_FG\n")
plt.scatter( ccomp.NT_DIS_FG, ccomp.QE_I22)
plt.ylabel('Quantidade de Livros lidos')
plt.xlabel('Nota Discussiva Formacao Geral ')
plt.show()

print("grafico NT_DIS_CE\n")
plt.scatter( ccomp.NT_DIS_CE, ccomp.QE_I22)
plt.ylabel('Quantidade de kivros lidos')
plt.xlabel('Nota Discussiva Formacao especifica')
plt.show()
print("\n")
print("Dados para quem nao leu nenhum livro FG")
leitura = ccomp.loc[ccomp.QE_I22 ==1]
print(leitura.NT_DIS_FG.describe())
print("\n")

print("Dados para quem nao leu nenhum livro CE")
leitura = ccomp.loc[ccomp.QE_I22 ==1]
print(leitura.NT_DIS_CE.describe())
print("\n")

print("Dados para quem nao leu mais de 8 livros FG")
leitura = ccomp.loc[ccomp.QE_I22 ==5]
print(leitura.NT_DIS_FG.describe())
print("\n")

print("Dados para quem nao leu mais de 8 livros CE")
leitura = ccomp.loc[ccomp.QE_I22 ==5]
print(leitura.NT_DIS_CE.describe())
print("\n")

"""
#Como verificar se a média dos alunos do campo QE_I22 para todos os alunos são realmente diferentes
qe22 = pandas.DataFrame(tabela, columns=['NT_DIS_FG', 'QE_I22'])
qe22.boxplot(by='QE_I22')
print("\n")


qe22 = pandas.DataFrame(tabela, columns=['NT_DIS_CE', 'QE_I22'])
qe22.boxplot(by='QE_I22')
print("\n")
"""


#para computacao
print("FG\n")
qe22 = pandas.DataFrame(ccomp, columns=['NT_DIS_FG', 'QE_I22'])
qe22.boxplot(by='QE_I22')
print("\n")

print("CE\n")
qe22 = pandas.DataFrame(ccomp, columns=['NT_DIS_CE', 'QE_I22'])
qe22.boxplot(by='QE_I22')
print("\n")


#A análise de variância (ANOVA) é um teste usado para comparar as médias de dois grupos. 
#suposições: normalidade, independência e variância homegênea

#nota geral agrupada pela questão 22
print("FG\n")
print(tabela['NT_DIS_FG'].groupby(tabela['QE_I22']).describe())
print("\n")

print("CE\n")
print(tabela['NT_DIS_CE'].groupby(tabela['QE_I22']).describe())
print("\n")
