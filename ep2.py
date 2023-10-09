from ast import For
from re import I


print(5+2, 5-2, 5*2, 5/2, 5**2, 5//2, 5%2)
print(5**8)
print('Teu cu '*3)
print('1'*2)

#desafios

# 1) Faça um programa que leia um número
#   inteiro e mostre na tela o seu sucessor
#   e seu antecessor.

n = int(input('Informe um número inteiro: '))
print('O antecessor de {}, é {} e o sucessor dele é {}' .format(n, n-1, n+1))


# 2) Crie um algoritimo que leia um número
#   e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Informe um número: '))
print('O dobro de {} é {}, o triplo é {} e o {} é a raiz quadrada' .format(n, n*2, n*3, n**(1/2)))

# 3) Desenvolva um programa que leia as duas notas
#   de um aluno, calcule e mostra a sua média.

n1 = float(input('Informe a 1ª nota do aluno: '))
n2 = float(input('Informe a 2ª nota do aluno: '))
n = float(input('Informe a primeira nota do aluno: ')) + float(input('Informe a segunda nota do aluno: '))
print('A média desse aluno é: ', (n1+n2)/2)
print('A média é ', n/2)

# 4) Escreva um programa que leia um valor em metros
#   e o exiba convertido em centimetros e milímetros.

n = float(input('Informe o tamanho em metros: '))
print('\n Kilometros: {} \n Metros: {} \n Centimetros: {} \n Milímetros: {}' .format(n/1000, n, n*1000, n*1000*1000))

# 5) Faça um programa que leia um numero qualquer e
#  mostre na tela a sua tabuada.

n = int(input('Informe um número: '))

for i in range(11) :
    print('{} X {} = {}'.format(n, i, n*i))

# 6) Crie um programa que leia quanto dinheiro uma 
#  pessoa tem na carteira e mostre quantos dólares ela
#  pode comprar. Considerando 1U$ = R$3,27

n = float(input('Dinheiro a ser convertido: '))
print('Com R${} você consegue U${:.2f}' .format(n, n/3,27))

# 7) Faça um programa que leia a largura e a altura de
#  uma parede em metros, calcule a sua área e a quanti-
#  dade de tinta necessária para pintá-la, sabendo que
#  cada litro de tinta, pinta uma área de 2m².

n = float(input('informe a altura da parede: '))*float(input('informe a largura da parede: '))
print('Você precisará de {} Litros de tinta' .format(n/(2)**2))

# 8) Faça um altoritimo que leia o preço de um produto
#  e mostre seu novo preço, com 5% de desconto.

n = float(input('Informe o preço: '))*95 / 100
print('Com 5 por cento de desconto fica', n)

# 9) Faça um algorítimo que leia o salário de um funci-
# onário e mostre seu novo salário, com 15% de aumento.

n = float(input('Informe o salário: '))*115 / 100
print('Com 15% de aumento fica', n)