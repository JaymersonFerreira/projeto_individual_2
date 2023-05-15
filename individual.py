def mensagem(msg):
        print('-' * 30) 
        print()
        print(f'\033[34m{msg}\033[m')  
        print('-' * 30)


def resultado(criterios, candidato):
    global result, lista_aprovados
    for i in range(len(candidato)):
        e = candidato[i][0]
        t = candidato[i][1]
        p = candidato[i][2]
        s = candidato[i][3]

        result.append(f'{i+1}ª Candidato: e{e}_t{t}_p{p}_s{s}')
        
    mensagem('Candidatos:')  
    
    for c in range(len(result)):
        print(f'{result[c][:13]:.<18}', end='')
        print(f'{result[c][13:]}')
    
    for j in range(len(result)):
        cont = 0
        for i in range(0, 4):
            if 0 < criterios[i] <= candidato[j][i]:
                cont += 1
            if cont == 4:
                lista_aprovados.append(f'{j+1}ª Candidato: e{candidato[j][0]}_t{candidato[j][1]}_p{candidato[j][2]}_s{candidato[j][3]}')

    mensagem('Lista dos aprovados:')
     
    for ap in range(len(lista_aprovados)):
        print(f'{lista_aprovados[ap][:13]:.<18}', end='')
        print(f'{lista_aprovados[ap][13:]}')


lista_aprovados = []
result = []
candidato = []
pos = 1
  
mensagem('Quais são as notas:')
   
while True:
    print(f'{pos}ª Candidato:')
    notas = [int(input('Nota para Entrevista: ')),
            int(input('Nota para Teste Teorico: ')),
            int(input('Nota para Teste Prático: ')),
            int(input('Nota para Soft Skill: '))]
    candidato.append(notas[:])
    notas.clear

    resposta = input('Quer continuar? ').lower()[0]
    if resposta == 'n':
        break
    print()
    pos +=1
   
mensagem('Quais são Critério:')
   
criterios = [int(input('e_ Entrevista: ')),
             int(input('t_ Teste Teórico: ')),
             int(input('p_ Teste Prático: ')),
             int(input('s_ Soft Skill: '))]

resultado(criterios, candidato)



