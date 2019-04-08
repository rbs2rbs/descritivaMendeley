from scholar import *

dados = Scholar(
    busca = 'Pau da Lima', 
    tipo = 'abstract', 
    token = 'MSwxNTU0Njg1NzExMzQ2LDU0MDU5NTI5MSwxMDI4LGFsbCwsLGI5NGM3MmRjNDM5M2Q2NDYwZDZiM2U0NDVlYWRkY2IyM2Q1OWd4cnFiLDQ1MGE3NzZiLWRhMjEtMzk5MC05NTZiLTY3ZTZkZWMzM2E1NyxsSkdHbFJxTTc5UlpRTVQyTjJsZ0syMmY0WEU'
)

dados.gerar()

grafico(t = "palavras-chave", dados = dados)