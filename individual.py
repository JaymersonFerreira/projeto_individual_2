# eX_tX_pX_sX 

def resultado(candidado):
    global result
    for i in range(len(candidado)):
        e = candidado[i][0]
        t = candidado[i][1]
        p = candidado[i][2]
        s = candidado[i][3]

        result.append(f'e{e}_t{t}_p{p}_s{s}')
        print(result)
        return result



#///////////////////PRINCIPAL///////////////////////////
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

# print('\n Quais notas gostaria de pesquisar?'
#           '\n e_ Entrevista'
#           '\n t_ Teste Teórico'
#           '\n p_ Teste Prático'
#           '\n s_ Avaliação de Soft Skill')


resultado(candidato)

print(result)
