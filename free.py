#!/usr/bin/python
import requests
import random
import json
import os

class SSH:
   def __init__(self):
      os.system('clear')
      print('Gerar SSH Free')
      print()
      print('1 - NetTunnel')
      print()
      option = input('Escolha uma opção: ')
      print()
      if option == '1':
         SSH.NetTunnel(self)
      
      else:
         SSH()
     
      
       
         
   def NetTunnel(self):
      cabeca ={
          'user-agent': 'Android', 
          'origin': 'https://www.nettunnel.xyz', 
          'referer': 'https://www.nettunnel.xyz/ssh/br/',
          'Host': 'www.nettunnel.xyz',
          'x-requested-with': 'XMLHttpRequest',
          'cookie': 'PHPSESSID=3f0039kr0nc1klo49suu4td9tg'
                  }
      
      requests.get('https://www.nettunnel.xyz/ssh/br/', headers = cabeca)

      NetTunnelUser = json.loads(requests.post('https://www.nettunnel.xyz/ssh/br/pages/create.php', data = '', headers = cabeca).text)


      print('Usuario: ' + NetTunnelUser["user"] + '\n' + 'Senha: ' + str(NetTunnelUser["pass"]) + '\n' + 'Dominio: ' + str(NetTunnelUser["ip"]))
      
SSH()