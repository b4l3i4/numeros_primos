#pedir para o usuario digitar um numero, falar se e primo se nao quantas vezes e divisivel

numero = int(input('Digite um numero:'))
#da o resultado direto de  numeros menores que 1
if numero <= 1:
    print(22*'-')
    print('|O numero nao e primo|')
    print(22*'-')
else:
    primo = True
#verifica se e divisivel
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f'O numero {numero} e primo.')
#verifica quantas vezes e dividido
    else:
        divisores = 0 
        for i in range(1, numero):
            if numero % i == 0:
                divisores += 1
        print(f'O numero {numero} nao e primo, ele e divisivel {divisores} vezes por numeros menores.')