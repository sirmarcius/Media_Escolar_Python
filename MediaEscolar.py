
print('##### Bem-vindo ao sistema de media escolar #####')

for a in range(1,5):
    nome = str(input('\nAluno n°{} '.format(a)))
    nota1 = float(input('Entre com a nota n°{} '.format(1)))
    nota2 = float(input('Entre com a nota n°{} '.format(2)))
    nota3 = float(input('Entre com a nota n°{} '.format(3)))
    nota4 = float(input('Entre com a nota n°{} '.format(4)))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print('A média do aluno {}'.format(a), 'é:',media)
    if media >=7:
      print('Aluno nº{}'.format(a),nome,'aprovado(a)!')
    else:
      print('Aluno nº{}'.format(a),nome,'reprovado(a)!')

print('\nObrigado por utilizar nosso sistema!')      

            

