from scholar import *
import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# Create random data with numpy
import numpy as np
import pandas as pd

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


dados = Scholar(
    busca = 'Pau da Lima', 
    tipo = 'abstract', 
    token = 'MSwxNTUyMzU1NzEwNzM1LDU0MDU5NTI5MSwxMDI4LGFsbCwsLDQyZmQ3MTlmMjRkZWE2NDM3NDRhMTVkNDYyMjhlZGU2ZjZjM2d4cnFiLDQ1MGE3NzZiLWRhMjEtMzk5MC05NTZiLTY3ZTZkZWMzM2E1NyxlaS14VXczbDd2NFdCZkVuNHcxZkVHZnlGZ0k'
)

dados.gerar()
# df = pd.DataFrame.from_dict(dados.saida, orient='columns')
anos = []
for ano in dados.saida:
    anos.append(ano['ano'])

anos_np = np.unique(anos, return_counts=True)
print(anos_np)
for index, i in enumerate(range(min(anos_np[0]),max(anos_np[0])+1)):
    if i not in anos:
        anos_np = np.insert(anos_np,[index],[[i],[0]], axis=1)

plt.plot(anos_np[0], anos_np[1], 'r--')
plt.show()