# 6. Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
# Me chamo Thiago e sou um desenvolvedor Python . Um analista de dados Python
texto = "  Me chamo Thiago e sou um desenvolvedor Python . Um analista de dados Python"
#print(texto)
texto_novo = texto.split()
#print(texto_novo)
count = {}

for pala in texto_novo:
    if pala in count:
        count[pala] += 1
       # print(pala)
    else:
        count[pala] = 1
        #print(pala)
                
print(count)

'''
texto = " Me chamo Thiago e sou um desenvolvedor Python. Um analista de dados Python"
print(texto)
palavras = texto.split()
print(palavras)
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
        print(palavra)
    else:
        contagem_palavras[palavra] = 1
        print(palavra)

print(contagem_palavras)
''' 