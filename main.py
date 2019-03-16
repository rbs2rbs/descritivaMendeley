from scholar import *
import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# Create random data with numpy
import numpy as np
import pandas as pd

import collections

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


dados = Scholar(
    busca = 'machine learning', 
    tipo = 'abstract', 
    token = 'MSwxNTUyNzY4MzcxODI1LDU0MDU5NTI5MSwxMDI4LGFsbCwsLDIxM2YzYWNhNDIwNjkzNGNhYzU4ZDdlLTFkZWZmN2I4MmY3Zmd4cnFiLDQ1MGE3NzZiLWRhMjEtMzk5MC05NTZiLTY3ZTZkZWMzM2E1NyxOZVVGVkl3MnRHMjFZMzFuX3R2M1VhcmhKajg'
)

dados.gerar()
# ANALISE ANAO
# anos = []
# for ano in dados.saida:
#     anos.append(ano['ano'])

# anos_np = np.unique(anos, return_counts=True)
# print(anos_np)
# for index, i in enumerate(range(min(anos_np[0]),max(anos_np[0])+1)):
#     if i not in anos:
#         anos_np = np.insert(anos_np,[index],[[i],[0]], axis=1)

# plt.plot(anos_np[0], anos_np[1], 'r--')
# plt.show()

# ANALISE TITULO
# stop_words_in = set(stopwords.words('english')) 
# stop_words_pt = set(stopwords.words('portuguese')) 

# titulo_filtrado = [] 
# for titulo in dados.saida:
#     word_tokens = word_tokenize(titulo['titulo']) 
#     for w in word_tokens:
#         if not (w.lower() in stop_words_in or w.lower() in stop_words_pt):
#             if w.isalnum():
#                 titulo_filtrado.append(w.lower())

# titulo_filtrado = collections.Counter(titulo_filtrado).most_common()

# df = pd.DataFrame(titulo_filtrado[:10])

# p = df.plot(kind='barh', title ="Palavras Frequentes", figsize=(15, 10), legend=False, fontsize=12)
# p.set_yticklabels(df[0])
# p.invert_yaxis()
# plt.show()


# ANALISE RESUMO

stop_words_in = set(stopwords.words('english')) 
stop_words_pt = set(stopwords.words('portuguese')) 

titulo_filtrado = [] 
for titulo in dados.saida:
    word_tokens = word_tokenize(titulo['resumo']) 
    for w in word_tokens:
        if not (w.lower() in stop_words_in or w.lower() in stop_words_pt):
            if w.isalnum():
                titulo_filtrado.append(w.lower())

titulo_filtrado = collections.Counter(titulo_filtrado).most_common()

df = pd.DataFrame(titulo_filtrado[:10])

p = df.plot(kind='barh', title ="Palavras Frequentes", figsize=(15, 10), legend=False, fontsize=12)
p.set_yticklabels(df[0])
p.invert_yaxis()
plt.show()
