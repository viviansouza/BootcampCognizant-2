import requests  # faz requisição http
from bs4 import BeautifulSoup
import operator
from collections import Counter  #  ajuda na manipulação de listas e tuplas

#função para definir o webcrauller
def start(url):
    wordlist = [] #armazena o conteúdo do site
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser') #objeto que faz a requisição dos dados da url e transforma em html

    for each_text in soup.findAll('div', {'class': 'entry-content'}): #  vai percorrer pelo cod html, procurar por div e class e transoformar em string
        content = each_text.text

        words = content.lower().split() #  tranforma em letras minpusculas e faz um split, cada conteúdo vai ser uma linha

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist): #  vai remover qq símbolo indesejado
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%¨&¨&*()_+<>?/.,'

        for i in range(0, len(symbols)):  # percorre a wordlist e remove os símbolos
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list): # cria um dicionário, faz uma contagem, exibe e top 20 das palavras mais utilizadas
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key=operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
