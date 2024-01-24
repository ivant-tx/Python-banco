#Utilizando python aprimorar minhas habilidades com python e alguns pacotes
#cadastro
import random as rd
import pandas as pd #usarei para fazer a persistencia dos dados, utilizar dicionario e arquivo csv
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
    desejo=str(input('Voce deseja fazer um novo cadastro(1), acessar uma conta(2)'))#verificar se tem somente numeros

    if desejo==1:
        numero=rd.random()
        titular=str(input('Digite o nome do titular da nova conta')).strip().lower()
        conta=cadastro(numeroconta=numero,titular=titular)
        des2=str(input('Deseja sacar(1) ou depositar(2)?')).strip()
        try:
            if des2 == 1:
                valor=float(input('Digite o valor a ser sacado'))#fazer uma função de verificação
                conta.sacar(valor)
            elif des2==2:
                valor=float(input('Digite o valor a ser depositado'))#utilizar da função de verificação
                conta.depositar(valor)
        except:
            print('infelizmente ouve um erro!')
            break

    elif desejo == 2:
            conta=usuario