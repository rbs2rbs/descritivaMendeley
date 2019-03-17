from scholar import *

dados = Scholar(
    busca = 'machine learning', 
    tipo = 'abstract', 
    token = 'MSwxNTUyNzkzOTk4Njg5LDU0MDU5NTI5MSwxMDI4LGFsbCwsLGVlYjZkMTlkODNkNzYyNGM1ODM4NjYwLTQ1YmEzYTc3YWU2Mmd4cnFiLDQ1MGE3NzZiLWRhMjEtMzk5MC05NTZiLTY3ZTZkZWMzM2E1NyxiYW03OFNNU0dvXzdaaG5lWnpoMERjeFRxZXc'
)

dados.gerar()

grafico(t = "palavras-chave", dados = dados)