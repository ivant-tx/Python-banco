#Utilizando python aprimorar minhas habilidades com python e alguns pacotes
#cadastro
import random as rd
#import pandas as pd #usarei para fazer a persistencia dos dados, utilizar dicionario e arquivo csv
class cadastro:
    def __init__(self, numeroconta, titular, saldo=0):
        self.numeroconta=numeroconta
        self.titular=titular
        self.saldo=saldo

    def depositar(self, valor):
        self.saldo+=valor
    
    def sacar(self,valor):
        self.saldo-=valor
while True:
    desejo = int(input('Voce deseja fazer um novo cadastro(1), acessar uma conta(2):\n'))#verificar se tem somente numeros
    if desejo == 1:
        numero=rd.random()
        titular=str(input('Digite o nome do titular da nova conta:\n')).strip().lower()
        conta=cadastro(numeroconta=numero,titular=titular)
        des2=int(input('Deseja sacar(1) ou depositar(2)?:\n'))

        if des2 == 1:
            valor=float(input('Digite o valor a ser sacado:\n'))#fazer uma função de verificação
            conta.sacar(valor)
            print(conta.saldo)
            encerrar=int(input('Você deseja encerrar (1) ou fazer uma nova operação(2):\n'))
            if encerrar==1:
                print('Fim')
                break

        elif des2==2:
            valor=float(input('Digite o valor a ser depositado:\n'))#utilizar da função de verificação
            conta.depositar(valor)
            print(conta.saldo)
            encerrar=int(input('Você deseja encerrar (1) ou fazer uma nova operação(2):\n'))
            if encerrar==1:
                print('Fim')
                break
            
    #elif desejo == 2:
            #conta=usuario