import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma = 0
    while i < 6:
        soma = soma + abs(as_a[i] - as_b[i])
        i += 1
    grau_similaridade = soma / 6
    return grau_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = tamanho_medio_de_palavras(texto)
    ttr = relacao_type_token(texto)
    hlr = razao_hapax_legomana(texto)
    sal = tamanho_medio_sentenca(texto)
    sac = complexidade_de_sentenca(texto)
    pal = tamanho_medio_frases(texto)
    assinatura = [wal,ttr,hlr,sal,sac,pal]

    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0
    j = 1
    while i < len(textos):
        textos[i] = calcula_assinatura(textos[i])
        i += 1
    as_b = ass_cp
    while i < len(textos):
        as_a = textos[i]
        textos[i] = compara_assinatura(as_a,as_b)
        i += 1
    i = 0
    while i < len(textos):
        while j < len(textos):
            if textos[i] < textos [j]:
                cohpiah = i
            else:
                cohpiah = j
            j += 1
        i += 1
        j = i + 1
    cohpiah = cohpiah + 1
    return cohpiah

def programa_funcionando():
    i = 0
    ass_cp = le_assinatura()
    textos = le_textos()
    
    texto_cohpiah = avalia_textos(textos,ass_cp)
    return texto_cohpiah
#_______________________FUNÇÕES QUE EU FIZ_________________________

#   MENU -----------------------------

# Tamanho médio de palavras (wal)
def tamanho_medio_de_palavras(texto):
    wal = soma_tamanhos_das_palavras(texto) / total_de_palavras(texto)
    return wal

# Relação Type-Token (ttr)
def relacao_type_token(texto):
    ttr = n_total_palavras_diferentes(texto) / total_de_palavras(texto)
    return ttr

# Razão Hapax Legomana (hlr)
def razao_hapax_legomana(texto):
    hlr = n_total_palavras_unicas(texto) / total_de_palavras(texto)
    return hlr

# Tamanho médio de sentença (sal)
def tamanho_medio_sentenca(texto):
    sal = soma_caracteres_sentencas(texto) / n_sentencas(texto)
    return sal

# Complexidade de sentença (sac)
def complexidade_de_sentenca(texto):
    sac = n_frases(texto) / n_sentencas(texto)
    return sac

# Tamanho médio de frase (pal)
def tamanho_medio_frases(texto):
    pal = n_caracteres_frases(texto) / n_frases(texto)
    return pal




#   FUNÇÕES ----------------------------
def soma_caracteres_sentencas(texto):
    soma_caracteres = 0
    sentenca = separa_sentencas(texto)
    i = 0
    while i < len(sentenca):
        soma_caracteres = soma_caracteres + len(sentenca[i])
        i += 1
    return soma_caracteres

def n_sentencas(texto):
    sentenca = separa_sentencas(texto)
    return len(sentenca)

def n_frases(texto):
    n_frase = []
    sentenca = separa_sentencas(texto)
    i = 0
    while i < len(sentenca):
        n_frase = n_frase + separa_frases(sentenca[i])
        i += 1
    return len(n_frase)

def n_caracteres_frases(texto):
    frase = []
    soma_caracteres = 0
    sentenca = separa_sentencas(texto)
    i = 0
    while i < len(sentenca):
        j = 0
        frase = separa_frases(sentenca[i])
        while j < len(frase): 
            soma_caracteres = soma_caracteres + len(frase[j])
            j += 1
        i += 1
    return soma_caracteres

def n_total_palavras_diferentes(texto):
    n_total_palavras_diferentes = 0
    frase = []
    lista_palavras = []
    sentenca = separa_sentencas(texto)
    i = 0
    while i < len(sentenca):
        j = 0
        frase = separa_frases(sentenca[i])
        while j < len(frase): 
            lista_palavras = lista_palavras + separa_palavras(frase[j])
            j += 1
        i += 1
    n_total_palavras_diferentes = n_palavras_diferentes(lista_palavras)
    return n_total_palavras_diferentes

def n_total_palavras_unicas(texto):
    frase = []
    lista_palavras = []
    sentenca = separa_sentencas(texto)
    i = 0
    while i < len(sentenca):
        j = 0
        frase = separa_frases(sentenca[i])
        while j < len(frase): 
            lista_palavras = lista_palavras + separa_palavras(frase[j])
            j += 1
        i += 1
    n_total_palavras_unicas = n_palavras_unicas(lista_palavras)
    return n_total_palavras_unicas

def total_de_palavras(texto):
    total_palavras = 0
    frase = []
    sentenca = separa_sentencas(texto)
    i = 0
    while i < len(sentenca):
        j = 0
        frase = separa_frases(sentenca[i])
        while j < len(frase): 
            lista_palavras = separa_palavras(frase[j])
            total_palavras = total_palavras + len(lista_palavras)
            j += 1
        i += 1
    return total_palavras

def soma_tamanhos_das_palavras(texto):
    soma_tamanho_palavras = 0
    frase = []
    sentenca = separa_sentencas(texto)
    i = 0
    while i < len(sentenca):
        j = 0
        frase = separa_frases(sentenca[i])
        while j < len(frase):
            k = 0
            lista_palavras = separa_palavras(frase[j])
            while k < len(lista_palavras):
                soma_tamanho_palavras = soma_tamanho_palavras + len(lista_palavras[k])
                k += 1
            j += 1
        i += 1
    return soma_tamanho_palavras

print("O autor do texto",programa_funcionando(),"está infectado com COH-PIAH")
