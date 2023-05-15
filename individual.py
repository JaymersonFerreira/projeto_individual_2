# # eX_tX_pX_sX 

# def resultado(*candidado):
#     for i in range(len(candidado)):
#         e = candidado[i][0]
#         t = candidado[i][1]
#         p = candidado[i][2]
#         s = candidado[i][3]

#         result.append(f'{i+1}ª Candidato: e{e}_t{t}_p{p}_s{s}')

#         return result
    

# def busca():
#     global notas
#     notas = [input('e_ Entrevista: '),
#              input('t_ Teste Teórico: '),
#              input('p_ Teste Prático: '),
#              input('s_ Avaliação de Soft Skill: ')
#              ]
#     return notas


# notas = []
# result = []
# candidato = []
# while True:
#     lista = [int(input('Nota para Entrevista: ')),
#             int(input('Nota para Teste Teorico: ')),
#             int(input('Nota para Teste Prático: ')),
#             int(input('Nota para Soft Skill: '))]
#     candidato.append(lista[:])
#     lista.clear


#     resposta = input('Quer continuar? ').lower()[0]
#     if resposta == 'n':
#         break


# busca()
# print(notas)
# resultado(candidato)

# print(result)



def resultado(criterios, candidato):
    global result, lista_aprovados
    for i in range(len(candidato)):
        e = candidato[i][0]
        t = candidato[i][1]
        p = candidato[i][2]
        s = candidato[i][3]

        result.append(f'{i+1}ª Candidato: e{e}_t{t}_p{p}_s{s}')
    print(f'{result}', end='\n')

    
    for j in range(len(candidato)):
        cont = 0
        for i in range(0, 4):
            if 0 < criterios[i] <= candidato[j][i]:
                cont += 1
        if cont == 4:
            lista_aprovados.append(f'{j+1}ª Candidato: e{e}_t{t}_p{p}_s{s} APROVADO')
    return lista_aprovados
    

lista_aprovados = []
result = []
candidato = []
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



criterios = [int(input('e_ Entrevista: ')),
             int(input('t_ Teste Teórico: ')),
             int(input('p_ Teste Prático: ')),
             int(input('s_ Avaliação de Soft Skill: '))]

resultado(criterios, candidato)

print(lista_aprovados)
print(candidato)


