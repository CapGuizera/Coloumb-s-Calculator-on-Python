import math

wish = input('O que você deseja calcular: Carga Elétrica, Força Elétrica ou Distância? ')

K = (9*(10**9))


if wish == 'Força Elétrica':
    
    Q1 = int(input('Digite o valor da Carga Elétrica 1: '))
    Q2 = int(input('Digite o Valor da Carga Elétrica 2: '))
    D = int(input('digite o valor da distância em Metros: '))

    
    Fe1 = int((K*Q1*Q2)/(D**2))
    

    print(f'A força elétrica é: {Fe1} Coloumbs')
          
elif wish == 'Carga Elétrica':
    Q2 = int(input('Digite o Valor da Carga Elétrica 2: '))
    D = int(input('digite o valor da distância em Metros: '))
    Fe1 = int(input('digite o valor da Força Elétrica em Newtons: '))

    Q1 = int((Q2*K)/((D**2)*Fe1))

    print(
        f'A carga elétrica Q1 é de: {Q1} coloumbs')
else:
    Q1 = int(input('Digite o valor da Carga Elétrica 1: '))
    Q2 = int(input('Digite o Valor da Carga Elétrica 2: '))
    Fe1 = int(input('digite o valor da Força Elétrica em Newtons: '))

    D = int(math.sqrt(int(((K*Q1*Q2)/Fe1))))

    print(f'A distância entre Q1 e Q2 é de: {D} metros')