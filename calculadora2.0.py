import matplotlib.pyplot as plt
import numpy as np

menu1 = ''' 
---------- BEM VINDO! :D ---------- 
---------- CALCULADORA ------------ 
''' 
print(menu1) 
 
menu2 = ''' 
 __________________________________
|            Opções                |
|                                  |
|         1. Básicas               |
|         2. funções               |
|         3. sair                  |
|                                  |
|__________________________________|
''' 

menu3 = '''
 __________________________________
|        Operações básicas         |
|                                  |
|        1. Soma                   |
|        2. subtração              |
|        3. multiplicação          |
|        4. divisão                |
|        5. voltar                 |
|__________________________________|
'''

menu4 = '''
 __________________________________
|              funções             |
|                                  |
|          1. calcular raízes      |
|          2. função linear        |
|          3. raiz quadrada        |
|          4. função quadrática    |
|          5. exponencial          |
|          6. fatoração            |
|          7. voltar               |
|__________________________________|
'''

# funções básicas 

def soma(n1, n2):
    return n1 + n2

def subtração(n1, n2):
    return n1 - n2

def multiplicação(n1, n2):
    return n1 * n2

def divisão(n1, n2):
    return n1 / n2

# funções

def bhaskara(a,b,c):
   delta = (b**2) - (4*a*c)
   x1 = (((-1)*b) + (delta**0.5))/(2*a)
   x2 = (((-1)*b) - (delta**0.5))/(2*a)
   if delta == 0:
      print(f'\nequação do 2° grau: {a}.x²{b}.x{c} = 0')
      print(f'Como Delta = 0, temos um único valor de raiz (X1 = x2): {x1}')
   elif delta > 0:
      print(f'\nequação do 2° grau: {a}.x2²{b}.x{c} = 0')
      print(f'Como Delta > 0, temos dois valores distintos de raízes: {x1} e {x2}')
   else:
      print(f'\nequação do 2° grau: {a}.x²{b}.x{c} = 0')
      print('Como Delta < 0, não temos raízes reais!')

def linear(x, a, b):
  return a * x + b

def raiz_quadrada(n):
    return n ** 0.5

def plot_linear(a, b):
  x = np.linspace(-10, 10, 100)
  y = linear(x, a, b)
  plt.bar(x,y, label=f'a função linear: y={a}x+{b}')
  plt.xlabel('eixo x')
  plt.ylabel('eixo y')
  plt.title('grafico da função linear')
  plt.grid(True)
  plt.show()

def exponencial(a, x):
   return a ** x

def plot_exponencial(a, b):
   x = np.linspace(-6, 6, 100)
   y = exponencial(a, x)
   plt.plot(x, y)
   plt.title(f'grafico da função exponencial {a}^{b}')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.grid(True)
   plt.show()

def funcao_quadratica(x, a, b, c):
   return a * x ** 2 - 4 * a * a

def plot_quadratica(a, b, c):
   x = np.linspace(-10, 10, 100)
   y = funcao_quadratica(x, a, b, c)
   plt.plot(x, y, label = f'{a} x² + {b} x + {c}')
   plt.title('grafico da função quadratica')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.grid(True)
   plt.show()

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def plot_fatorial(n):
  x = list(range(n+1))
  y = [fatorial(i) for i in x]
  plt.plot(x, y, marker='o', linestyle='-')
  plt.title('grafico de fatorial')
  plt.xlabel('numero')
  plt.ylabel('fatorial')
  plt.grid(True)
  plt.show()

# loop da calculadora
   
while True:

    print(menu2)

    opcao = int(input('esolha uma opção: '))

    if opcao == 3:
        break
   
        # operações básicas
   
    if opcao == 1:
        print(menu3)

        operacao = int(input('esolha uma operação básica: '))

        if operacao == 5:
            continue
      
        elif operacao == 1:
            print('você escolheu a função soma')
            numero1 = float(input('digite o primeiro número: '))
            numero2 = float(input('digite o nsegundo número: '))
            resultado = soma(numero1, numero2)
            print(resultado)

        elif operacao == 2:
            print('você escolheu a função subtração')
            numero1 = float(input('digite o primeiro número: '))
            numero2 = float(input('digite o nsegundo número: '))
            resultado = subtração(numero1, numero2)
            print(resultado)

        elif operacao == 3:
            print('você escolheu a função multiplicação')
            numero1 = float(input('digite o primeiro número: '))
            numero2 = float(input('digite o nsegundo número: '))
            resultado = multiplicação(numero1, numero2)
            print(resultado)

        elif operacao == 4:
            print('você escolheu a funçao divisão')
            numero1 = float(input('digite o primeiro número: '))
            numero2 = float(input('digite o nsegundo número: '))
            resultado = divisão(numero1, numero2)
            print(resultado)

        print('continuar?')
        continuar = input('S/N: ')
        if continuar != 'S' and continuar != 's':
            print('encerrando aplicação...')
            break
    
        else:
            print('\ndigite uma operação válida')
            continue

    elif opcao == 2:
      
        # funções

        print(menu4)

        funcao = int(input('escolha uma função: '))

        if funcao == 7:
             continue
      
        elif funcao == 1:
            print('\nvocê escolheu a função calcular raiz')
            a = float(input('digite o valor de a: '))
            b = float(input('digite o valor de b: '))
            c = float(input('digite o valor de c: '))
            resultado = bhaskara(a, b, c)
            print(resultado)

        elif funcao == 2:
            print('\nvoce escolheu a função linear')
            a = int(input('digite o valor de a: '))
            b = int(input('digite o valor de b: '))
            plot_linear(a, b)

        elif funcao == 3:
            print('\nvocê escolheu a função raiz quadrada')
            numero = int(input('digite um numero para descobrir sua raiz quadrada: '))
            print(f'a raiz quadrada de {numero} é {raiz_quadrada(numero)}')

        elif funcao == 4:
            print('\nvoce escolheu a função quadratica')
            a = int(input('digite o valor de a'))
            b = int(input('digite o valor de b'))
            c = int(input('digite o valor de c'))
            plot_quadratica(a, b, c)

        elif funcao == 5:
            print('\nvoce escolheu a função exponencial')
            a = int(input('digite o valor de a'))
            b = int(input('digite o valor de b'))
            plot_exponencial

        elif funcao == 6:
            print('\nvoce escolheu a função fatorial')
            numero = int(input('digite o numero para calcular seu fatorial'))
            plot_fatorial(numero)
     
        else:
            print('escolha uma opção valida')
            continue
      
        print('continuar?')
        continuar = input('S/N: ')
        if continuar != 'S' and continuar != 's':
            print('encerrando aplicação...')
            break