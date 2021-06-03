# jOGO DE Perguntas >
from time import sleep
import os

print(''' Olá, Bem vindo ao Welcomoe The Game, 
este jogo foi desenvolvido pelo Raí_p
''')
nome = str(input('Primeiro qual o seu nome: '))
idade = str(input('Qual a sua idade: '))
print( 'Ola {}, você tem {} anos, bem vindo ao TheGame '.format(nome, idade))
#Estrutura do Escolha 
itemA = (''' Matemática
+ - = √ % ''')
itemB = ('Programção')
itemC = ('Geografia')

print('-='*16)
opção = input('''
[1] Matemática.
[2] Programção. 
[3] Geografia.
''' )
print('-='*12)
print('carregando...//////////////')
sleep(0.8)
# Estrutura do jogo

# matematica
if opção == '1':
    print('Você escolhe {}.'.format(itemA))
    m1 = str(input('''Calcule o valor da expressão (22 * 4)² - (2² + 5)² =
    (a) 2156
    (b) 7663
    (c) 7664
    : 
     '''))
    if m1 =='a':
        sleep(0.6)
        print('Resposta Errada')
    elif m1 == 'b':
        sleep(0.6)
        print('Resposta Errada')
    elif m1 == 'c':
        sleep(0.6)
        print('Resposta Certa')
    else:
        sleep(0.6)
        print('Erro ao Carregar')
#Programação
if opção == '2':
    print('Você escolhe {}'.format(itemB))

    p1 = input(''' Qual a estrutura de um código HTML:

    (a)<!doctype html>, <html>, <head>, </head> <body>, </body>, </html>
    (b)<!doctype html>, <html>, <head>, </head> <body>, <body>, </html>
    (c)<!doctype html>, <html>, <head>, <body>, </body>, </html>,</head>
    ''')#a
    if p1 == 'a':
        print('Resposta Correta')
    elif p1 == 'b':
        print('Resposta errada')
    elif p1 == 'c':
        print('Resposta errada')
    else:
        print('Erro ao Carregar')
#Geografia
if opção == '3':
    print('Você escolhe {}'.format(itemC))
    g1 = str(input(''' De todas as opções abaixo apenas uma todos falam Portugues:
    (a) Brasil, Moçambique, Finlandia
    (b) Portugal, Italia, EUA, Peru
    (c)Cabo Verde, Italia, Pôlonia, Peru, Angola.
    (d)Moçambique, Portugal, Angola, Cabo Verde.
    '''))
    if g1 == 'a':
        print('Infelismente você errou.')
    elif g1 == 'b':
        print('Infelismente você errou.')
    elif g1 == 'c':
        print('Infelismente você errou.')
    elif g1 == 'd':
        print('Parabéns, você acertou')
    else:
        print('erro ao carregar')

print('Fim de Jogo')