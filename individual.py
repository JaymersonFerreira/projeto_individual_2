def resultado(criterios, candidato):
    global result, lista_aprovados
    for i in range(len(candidato)):
        e = candidato[i][0]
        t = candidato[i][1]
        p = candidato[i][2]
        s = candidato[i][3]

        result.append(f'{i+1}ª Candidato: e{e}_t{t}_p{p}_s{s}')

    print('-' * 30) 
    print('\033[34mCandidatos\033[m')  
    print('_' * 30) 

    for c in range(len(candidato)):
        print(f'{result[c][:13]:.<15}', end='')
        print(f'{result[c][13:]:.>15}')
      
    
    for j in range(len(candidato)):
        cont = 0
        for i in range(0, 4):
            if 0 < criterios[i] <= candidato[j][i]:
                cont += 1
            if cont == 4:
                lista_aprovados.append(f'{j+1}ª Candidato: e{e}_t{t}_p{p}_s{s} APROVADO')

    print('-' * 30)  
    print('\033[34mLista dos aprovados\033[m')
    print('_' * 30)  

    for ap in range(len(lista_aprovados)):
        print(f'{lista_aprovados[ap][:13]:.<18}', end='')
        print(f'{lista_aprovados[ap][13:25]}')


lista_aprovados = []
result = []
candidato = []

print('-' * 30)    
print('\033[34mQuais são as notas:\033[m')
print('_' * 30)    

while True:
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

print('-' * 30)    
print('\033[34mQuais são Critério:\033[m')
print('_' * 30)    

criterios = [int(input('e_ Entrevista: ')),
             int(input('t_ Teste Teórico: ')),
             int(input('p_ Teste Prático: ')),
             int(input('s_ Soft Skill: '))]

resultado(criterios, candidato)



