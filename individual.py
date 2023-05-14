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



def resultado(candidado):
    global result
    for i in range(len(candidado)):
        e = candidado[i][0]
        t = candidado[i][1]
        p = candidado[i][2]
        s = candidado[i][3]

        result.append(f'{i+1}ª Candidato: e{e}_t{t}_p{p}_s{s}')
    print(result)
    

result = []
candidato = []
while True:
    lista = [int(input('Nota para Entrevista: ')),
            int(input('Nota para Teste Teorico: ')),
            int(input('Nota para Teste Prático: ')),
            int(input('Nota para Soft Skill: '))]
    candidato.append(lista[:])
    lista.clear


    resposta = input('Quer continuar? ').lower()[0]
    if resposta == 'n':
        break
    
resultado(candidato)

print(candidato)
print(result)

