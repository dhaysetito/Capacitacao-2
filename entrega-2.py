#Dhayse de Lima Tito

import random

'''
class Lutador:
   
   def __init__(self, nome, idade, peso, forca, faixa, arte_macial):
      self.nome = nome
      self.idade = idade
      self.peso = peso
      self.forca = forca
      self.faixa = faixa
      self.arte_macial = arte_macial

   def set.nome(self, nome):
      self.nome = nome
      
   def set.idade(self, idade):
      self.idade = idade
      
   def set.peso(self, peso):
      self.peso = peso

   def set.forca(self, forca):
      self.forca = forca

   def set.faixa(self, faixa):
      self.faixa = faixa

   def set.arte_macial(self, arte_macial):
      self.arte_macial = arte_macial
'''

def menu():
   
   print('1 - Menu de Torneio')
   print('2 - Menu de Lutador')
   print('3 - Criar Torneio Aleatório')
   print('4 - Sair')

   rodar = True
   while rodar:
      escolha = input('Digite a opcao: ')
      if escolha in ('1','2','3','4'):
         rodar = False
      else:
         print('Opcao inválida')
         
   return escolha

def lutador():
   
   nome = input('Nome: ')
   idade = input('Idade: ')
   peso = input('Peso: ')
   forca = input('Forca: ')
   faixa = input('Faixa: ')
   arte_marcial = input('Arte marcial: ')

   return nome, idade, peso, forca, faixa, arte_marcial

def torneio():
   
   nome_torneio = input('Nome do Torneio: ')
   arte_marcial = input('Arte marcial do Torneio: ')
   faixa = input('Faixa: ')
   faixas = [faixa]
   
   rodar = True
   while rodar:
      escolha = input('Adicionar outra faixa (s/n)? ').lower()
      if escolha in ['s','n']:
         if escolha == 's':
            faixa = input('Faixa: ')
            faixas.append(faixa)
         else:
            rodar = False
      else:
         print('Opcao invalida!')

   peso1, peso2 = input('Faixa de peso: ').split(',')
   pesos = [[int(peso1), int(peso2)]]
   
   rodar = True
   while rodar:
      escolha = input('Deseja adicionar outra faixa de peso (s/n)? ')
      if escolha in ['s','n']:
         if escolha == 's':
            peso1, peso2 = input('Faixa de peso: ').split(',')
            pesos.append([int(peso1), int(peso2)])
         else:
            rodar = False
      else:
         print('Opcao invalida!')

   return nome_torneio, arte_marcial, faixas, pesos


def menu_torneio():
   
   print('1 - Criar torneio')
   print('2 - Inscrever lutador')
   print('3 - Ver torneios existentes')
   print('4 - Ver ranking de torneio')
   print('5 - Realizar luta')
   
   rodar = True
   while rodar:
      escolha = input('Digite a opcao: ')
      if escolha in ['1','2','3','4','5']:
         rodar = False
      else:
         print('Opcao inválida')
         
   return escolha

def menu_lutador():
   
   print('1 - Cadastro do lutador')
   print('2 - Ver lutadores')
   print('3 - Ver detalhes de lutador')
   
   rodar = True
   while rodar:
      escolha = input('Digite a opcao: ')
      if escolha in ['1','2','3']:
         rodar = False
      else:
         print('Opcao inválida')
         
   return escolha

def torneio_aleatorio():
   
   nomes_arq = open('nomes.txt','r')
   artes_marciais_arq = open('artes_marciais.txt','r')
   nomes = []
   artes_marciais = []
   
   for i in nomes_arq:
      nome = nomes_arq.readline()
      nomes.append(nome)
      
   for i in artes_marciais_arq:
      arte_marcial = artes_marciais_arq.readline()[:-1]
      artes_marciais.append(arte_marcial)

   lutadores = open('lutadores.txt','a')
   
   for i in range(200):
      nome_ = random.choice(nomes)
      arte_marcial_ = random.choice(artes_marciais)
      idade = random.randint(4,50)
      faixa = random.choice(['branca', 'cinza', 'amarela', 'laranja',\
                             'verde','azul','roxa','marrom','preta',\
                             'vermelha','livre'])
      peso = random.randint(40,84)
      pesos = random.choice([[40,60],[61,76],[52,70],[67,84]])
      forca = random.randint(0,100)
      lutador = nome_,idade, peso, forca, faixa, arte_marcial_
      lutadores.write(f'{lutador}\n')

   lutadores.close()
   torneio = f'Torneio de {arte_marcial_}',arte_marcial_,faixa,pesos
   torneios = open('torneios.txt','a')
   torneios.write(f'{torneio}\n')
   torneios.close()

   return torneio[0]
               

def main():

   lutadores = open('lutadores.txt','a')

   rodar = True
   
   while rodar:
      escolha = menu()
      if escolha == '4':
         print('Programa encerrado')
         rodar = False
      elif escolha == '1':
         escolha1 = menu_torneio()
         if escolha1 == '1':
            torneio_ = torneio()
            torneios = open('torneios.txt','a')
            torneios.write(f'{torneio_}\n')
            torneios.close()
         elif escolha1 == '2':
            lutadores = open('lutadores.txt','r')
            lutador = lutadores.readline()
            #como inscrever jogador?
            lutadores.close()
         elif escolha1 == '3':
            torneios = open('torneios.txt','r')
            for i in torneios:
               linha = i.split(',')
               print(linha[0][1:-1])
            torneios.close()
      elif escolha == '2':
         escolha1 = menu_lutador()
         if escolha1 == '1':
            lutador_ = lutador()
            lutadores = open('lutadores.txt','a')
            lutadores.write(f'{lutador_}\n')
            lutadores.close()
         elif escolha1 == '2':
            lutadores = open('lutadores.txt','r')
            for i in lutadores:
               linha = i.split(',')
               nome = linha[0]
               print(linha[0][2:-3])
            lutadores.close()
         else:
            lutadores - open('lutadores.txt','r')
            escolha2 = input('Qual lutador deseja escolher?')
            for linha in lutadores:
               i = linha.split(',')
               if i[0][2:-3] == escolha2:
                  print(f'Idade: {i[1]}\nPeso: {i[2]}\n\
Forca: {i[3]}\nFaixa: {i[4][1:-1]}\nArte Marcial: {i[5][1:-1]}')
      else:
         escolha1 = torneio_aleatorio()
         print(f'O torneio criado foi {escolha1}')


if __name__ == '__main__':
   #print(lutador())
   #print(torneio())
   #print(torneio_aleatorio())
   main()
   


