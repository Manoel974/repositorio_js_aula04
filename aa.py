import os 

os.system('cls')





# print('É um espaço na memória do computador que armazena valores ou expressões')
# print('Quantitativa, nominais, contínuas, etc....')
# print('O valor de uma variável pode ser alterado durante a execução de um programa, enquanto o valor de uma constante é fixo..')



# n = int(input('Digite um numero: '))

print('\n[1] Restaurane Chinês \n[2] Restaurante Tailandes \n[3] Restaurante Português \n[4] Churrascaria Brasileira')
print(30*'==')

nome = int(input('Escolh a uma opção: '))

match nome:
    case 1:
        print('Vc escoheu: Restaurante chinês')
    case 2:
        print('Vc escolheu: Restaurante tailandes')
    case 3:
        print('Vc escolheu: Restaurante português')
    case 4: 
        print('Vc escolheu: Churrascaria Brasileira')
