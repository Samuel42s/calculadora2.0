import time

def binary2dec(binario):
    decimal = 0
    for i in range(len(binario)):
        bit = int(binario[i])
        potencia = len(binario) - 1 - i
        decimal += bit * (2 ** potencia)
    return decimal

def dec2binary(decimal):
    binario = '0'
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2
    return binario

while True:

    print('converter binario para decimal / decimal para binario\n')
    print('escolha uma opção: ')

    opcao = int(input('binario para decimal (1) / decimal para binario (2): '))

    if opcao == 1:
        print('insira o numero bniario para converter: ')
        binario = input()
        decimal = binary2dec(binario)
        print('convertendo para decimal')
        time.sleep(2)
        print(f'O numero {binario} em decimal é: {decimal}')
    
    elif opcao == 2:
        print('insira o numero decimal para converter: ')
        decimal = int(input())
        binario = dec2binary(decimal)
        print('convertendo para binario')
        time.sleep(2)
        print(f'O numero {decimal} em binario é: {binario}')
    
    else:
        print('digite uma opção valida')
        continue
    
    continuar = input('Deseja continuar? (s/n): ')
    if continuar != 's' and continuar != 'S':
        print('encerrando programa...')
        time.sleep(2)
        break