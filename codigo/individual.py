def titulo(msg):
        print('-' * 30) 
        print()
        print(f'\033[34m{msg}\033[m')  
        print('-' * 30)

#Imprime os candidato
def lista_candidato(ficha):
    global result, lista_aprovados
    for i in range(len(ficha)):
        e = ficha[i][0]
        t = ficha[i][1]
        p = ficha[i][2]
        s = ficha[i][3]

        result.append(f'{i+1}ª Candidato: e{e}_t{t}_p{p}_s{s}')
        
    titulo('Lista de Candidatos:')  
    
    for c in range(len(result)):
        print(f'{result[c][:13]:.<18}', end='')
        print(f'{result[c][13:]}')
    
#Imprime os aprovados
def aprovados(criterios, ficha):
    for j in range(len(ficha)):
        cont = 0
        for i in range(0, 4):
            if 0 < criterios[i] <= ficha[j][i]:
                cont += 1
            if cont == 4:
                lista_aprovados.append(f'{j+1}ª Candidato: e{ficha[j][0]}_t{ficha[j][1]}_p{ficha[j][2]}_s{ficha[j][3]}')

    titulo('Lista dos aprovados:')
     
    for ap in range(len(lista_aprovados)):
        print(f'{lista_aprovados[ap][:13]:.<18}', end='')
        print(f'{lista_aprovados[ap][13:]}')
    if len(lista_aprovados) == 0:
        print('\033[31mNão há aprovados!\033[m')

#variáveis
lista_aprovados = []
ficha = []
result = []
pos = 1
  
titulo('Quais são as notas:')
#Recebe as notas   
while True:
    print(f'{pos}ª Candidato:')
    notas = [int(input('Nota para Entrevista: ')),
            int(input('Nota para Teste Teorico: ')),
            int(input('Nota para Teste Prático: ')),
            int(input('Nota para Soft Skill: '))]
    ficha.append(notas[:])
    notas.clear

    resposta = input('Quer continuar? [N] para sair: ').lower()[0]
    if resposta == 'n':
        break
    print()
    pos +=1
   
titulo('Quais são os Critérios:')
#Rebece os critérios   
criterios = [int(input('e_ Entrevista: ')),
             int(input('t_ Teste Teórico: ')),
             int(input('p_ Teste Prático: ')),
             int(input('s_ Soft Skill: '))]

lista_candidato(ficha)

aprovados(criterios, ficha)
