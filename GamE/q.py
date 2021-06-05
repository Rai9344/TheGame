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
    m2 = str(input(''' Qual das resposta abaixo a resposta esta correta:
    6+4*3-6 ÷ 3 = 16
    (a) 5² * 3 + 5² + raiz 81
    (b) Raiz 81 + 2^2 + (2 * 8 - 13)
    (c) (4^4) - (20) ÷ (2) - raiz 81
    (d) (3² + 5) x (3 -3)
    '''))
    if m2 == 'b' or 'B':
        print('Resposta Correta')
        sleep(0.3)
    elif m2 == 'a' or 'A':
        sleep(0.3)
        print('Resposta incorreta')
    elif m2 == 'c' or 'C':
        sleep(0.3)
        print('Resposta incorreta')
    elif m2 == 'd' or 'D':
        sleep(0.3)
        print('Resposta incorreta')
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
    país = str(input(''' Nas opções abaixo uma delas os  paises não falam inglês ?
    (a) Macau, EUA, Finlandia, Suiça
    (b) EUA, Canadá, Irlanda, Bahamas
    (c) Macau, EUA, Finlandia, Suiça
    (d) Austrália, Canadá, Inglaterra
'''))

print('Fim de Jogo')