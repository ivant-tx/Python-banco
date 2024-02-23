#Utilizando python aprimorar minhas habilidades com python e alguns pacotes
#cadastro
import random as rd
import pandas as pd #usarei para fazer a persistencia dos dados, utilizar dicionario e arquivo csv
import csv
class Cadastro:
    def __init__(self):
        self.df=pd.DataFrame(columns=['Titular','numeroconta','cpf','saldo'])

    def depositar(self,numeroconta, valor):
        self.df.loc[self.df['numeroconta'] == numeroconta, 'saldo']+=valor
        # saldo apos a loc do numero conta seleciona a coluna a ser alterada

    def sacar(self,numeroconta, valor):
        self.df.loc[self.df['numeroconta'] == numeroconta, 'saldo']-=valor
        # saldo apos a loc do numero conta seleciona a coluna a ser alterada

    def novo_cadastro(self, numeroconta, titular, cpf, saldo=0):
        registro = {'Titular': titular,'numeroconta': numeroconta,'cpf':cpf,'saldo': saldo}
        self.df = self.df.append(registro, ignore_index=True)
        #ingore_index=true deixa continuo a adição de linhas
    
    def salvar_cadastro(self, dados):
        with open(dados,mode='a',newline='') as novos_dados:
            escrever=csv.writer(novos_dados)
            if novos_dados.tell() == 0:  # Verifica se o arquivo está vazio
                escrever.writerow(self.df.columns)  # Escreve os nomes das colunas apenas se o arquivo estiver vazio
            escrever.writerow([titular,numero,cpf,0])
        print(f'Seus dados foram cadastrados e seu numero de conta é {numero}')

dados = "cadastro.csv"
cadastro=Cadastro()
while True:
    desejo = int(input('Voce deseja fazer um novo cadastro(1), acessar uma conta(2):\n'))#verificar se tem somente numeros
    if desejo == 1:
        numero=''.join([str(rd.randint(0,9))for i in range(8)])
        cpf=int(input('Digite seu CPF para cadastro:\n'))
        titular=str(input('Digite o nome do titular da nova conta:\n')).strip().lower().replace(" ", "")#replace retira o espaço de nome e sobrenome
        cadastro.novo_cadastro(numero,titular,cpf)
        cadastro.salvar_cadastro(dados)
        break
        
'''
    elif desejo == 2:   
        des2=int(input('Deseja sacar(1) ou depositar(2)?:\n'))
        #dados = pd.read_csv('cadastro.csv')
        #dados.head()
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
 '''#verificar se esta de acordo com os acessos pandas
    