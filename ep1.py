name = str(input('Qual o seu nome filhote? '))
idade = str(input('E a sua idade, qual é? '))
numer = float(input('Me fala um numero '))
numer2 = float(input('Agora me fala outro pra eu somar '))

print('Olá {}, pelo que tu me falou sua idade é {}, bom... O resultado daquela soma é {}.'.format(name, idade, numer + numer2))