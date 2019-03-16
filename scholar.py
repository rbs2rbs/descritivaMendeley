# PARA FAZER O PARSE HTML
from bs4 import BeautifulSoup as BS
# PARA FAZER AS REQUISIÇÕES HTTP
import requests
# UTILIZAR REGEX PARA ESTRAIR TEXTOS
import re



class Scholar(object):
  def __init__(self,busca,tipo,token):
    self.url_inicial = "https://api.mendeley.com/search/catalog?%s=%s&limit=100" %(tipo,"%22"+busca.replace(" ","%20")+"%22")
    self.headers = {
          'Authorization': 'Bearer '+token,
          'Accept' : 'application/vnd.mendeley-document.1+json'
          }
    self.req = requests.get(self.url_inicial, headers = self.headers, timeout = 5)
    self.saida = []
    self.qt_artigos = None
    self.titulos = None
    self.anos = None

  def gerar(self):
    print(self.req.status_code)
    if self.req.status_code != 200:
      print('Token Expirado')
      return('Token Expirado')
    else:
      for dados in self.req.json():
        self.saida.append(
          {
            'titulo' : dados['title'],
            'ano' : dados['year'],
            'resumo' : dados['abstract']
          }
        )

      proximo = self.req.links
      if proximo:
        while proximo:
          url = proximo['next']['url'] 
          req = requests.get(url, headers = self.headers, timeout = 5)
          print(req.status_code)
          for dados in req.json():
            self.saida.append(
              {
                'titulo' : dados['title'],
                'ano' : dados['year'],
                'resumo' : dados['abstract']
              }
            )
          proximo = req.links    

    self.qt_artigos = len(self.saida)/2
    # self.titulos = self.saida['titulo']
    # self.anos = self.saida['ano']








# url = 'https://api.mendeley.com/search/catalog?title=%22machine%20learning%22&limit=100'      
# headers = {
#   'Authorization': 'Bearer MSwxNTUyMzQ3NTA1MTUzLDU0MDU5NTI5MSwxMDI4LGFsbCwsLDFlZTIwZTMzNzkzYmY3NDkzYjdhNjg1NzYyNmRhOTg1MGYzNGd4cnFiLDQ1MGE3NzZiLWRhMjEtMzk5MC05NTZiLTY3ZTZkZWMzM2E1NyxGMWZNSWg2MXZWTnlMTHRSLU5USzFlM1hLZnc',
#   'Accept' : 'application/vnd.mendeley-document.1+json'
#   }

# req = requests.get(url, headers = headers, timeout = 5)
# saida = []
# if req.status_code != 200:
#   print('Token Expirado')
# else:
#   for dados in req.json():
#     saida.append(
#       {
#         'titulo' : dados['title'],
#         'ano' : dados['year']
#       }
#     )

#   proximo = req.links
#   if proximo:
#     while proximo:
#       url = proximo['next']['url']   
#       print(url)  
#       headers = {
#       'Authorization': 'Bearer MSwxNTUyMzQ3NTA1MTUzLDU0MDU5NTI5MSwxMDI4LGFsbCwsLDFlZTIwZTMzNzkzYmY3NDkzYjdhNjg1NzYyNmRhOTg1MGYzNGd4cnFiLDQ1MGE3NzZiLWRhMjEtMzk5MC05NTZiLTY3ZTZkZWMzM2E1NyxGMWZNSWg2MXZWTnlMTHRSLU5USzFlM1hLZnc',
#       'Accept' : 'application/vnd.mendeley-document.1+json'
#       }

#       req = requests.get(url, headers = headers, timeout = 5)
#       for dados in req.json():
#         saida.append(
#           {
#             'titulo' : dados['title'],
#             'ano' : dados['year']
#           }
#         )
#       proximo = req.links
#       print(proximo)



# print(saida)