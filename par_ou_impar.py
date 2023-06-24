"""
Programa: par_ou_impar
Descrição: Este programa verifica se um número digitado é par ou ímpar, caso seja negativou ou não inteiro, retornará inválido.
Autor: F
Data : 23/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis





#Entrada de dados

x = float(input("Qual o número desejado? "))


#Processamento de dados

if (x % 2) == 0 and x > 0 and int(x) == x:
    print("Seu número é par.")

elif (x % 2) != 0 and x > 0 and int(x) == x:
    print("Seu número é ímpar")
    
else:
    print("Seu número é inválido.")



#Saida de dadaos