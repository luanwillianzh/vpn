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
      print('2 - Speed Net')
      print()
      option = input('Escolha uma opção: ')
      print()
      
      if option == '1':     
         print('Servidores: ')
         print()
         print('1 - Brasil')
         print('2 - Canada')
         print('3 - Canada 2')
         print('4 - EUA')
         print('0 - Voltar')
         print()
         opit = input('Escolha um servidor: ')
         
         if opit == '1':
            self.UrlGet = 'https://www.nettunnel.xyz/ssh/br/'
            self.UrlPost = 'https://www.nettunnel.xyz/ssh/br/pages/create.php'
            SSH.NetTunnel(self)
            
         elif opit == '2':
            self.UrlGet = 'https://www.nettunnel.xyz/ssh/ca/'
            self.UrlPost = 'https://www.nettunnel.xyz/ssh/ca/pages/create.php'
            SSH.NetTunnel(self)
          
         elif opit == '4':
            self.UrlGet = 'https://www.nettunnel.xyz/ssh/us/'
            self.UrlPost = 'https://www.nettunnel.xyz/ssh/us/pages/create.php'
            SSH.NetTunnel(self)
            
            
         elif opit == '3':
            self.UrlGet = 'https://www.nettunnel.xyz/ssh/fr/'
            self.UrlPost = 'https://www.nettunnel.xyz/ssh/fr/pages/create.php'
            SSH.NetTunnel(self)
            
         else:
            SSH()


      elif option == '2':
         print('Servidores: ')
         print()
         print('1 - Brasil')
         print('2 - Canada')
         print('3 - EUA')
         print('0 - Voltar')
         print()
         opit = input('Escolha um servidor: ')
         
         if opit == '1':
            self.UrlGet = 'https://speednetssh.com.br/free/gerar/brfree/'
            self.UrlPost = 'https://speednetssh.com.br/free/gerar/brfree/pages/create.php'
            SSH.SpeedNet(self)
            
            
         elif opit == '2':
            self.UrlGet = 'https://speednetssh.com.br/free/gerar/cafree/'
            self.UrlPost = 'https://speednetssh.com.br/free/gerar/cafree/pages/create.php'
            SSH.SpeedNet(self)

         elif opit == '3':
            self.UrlGet = 'https://speednetssh.com.br/free/gerar/euafree/'
            self.UrlPost = 'https://speednetssh.com.br/free/gerar/euafree/pages/create.php'
            SSH.SpeedNet(self)
            
         elif opit == '0':
            SSH()
         
      else:
         SSH()
     
      
         
         
         
   def SpeedNet(self):
      print()
      
      try:
         userags = random.choice((requests.get('https://raw.githubusercontent.com/luanwillianzh/vpn/main/ua.txt').text).split('\n'))
         
         phpssid = requests.get(self.UrlGet, headers = {'user-agent': userags}).headers["set-cookie"]
        
         cabeca = {
          'user-agent': userags,
          
          'origin': 'https://speednetssh.com.br', 
          'referer': self.UrlGet,
          'x-requested-with': 'XMLHttpRequest',
          'cookie': phpssid
                  }
                  
         SpeedNetUser = json.loads(requests.post(self.UrlPost, data = '', headers = cabeca).text)

         print('Usuario: ' + SpeedNetUser["user"] + '\n' + 'Senha: ' + str(SpeedNetUser["pass"]) + '\n' + 'Dominio: ' + str(SpeedNetUser["ip"]) + '\n' +'Porta Websocket: 80' + '\n' + 'Porta SSL: 443' '\n\n' + 'Payload: ' + '\n\n' + 'GET / HTTP/1.1[crlf]Host: ' + str(SpeedNetUser["ip"]) + '[crlf]Upgrade: websocket[crlf][crlf]' )
      
      except: 
         print('Erro de conexão, faça o processo sem VPN')
         









   def NetTunnel(self):
      print()
      
      try:
         userags = random.choice((requests.get('https://raw.githubusercontent.com/luanwillianzh/vpn/main/ua.txt').text).split('\n'))
         phpssid = requests.get(self.UrlGet, headers = {'user-agent': userags}).headers["set-cookie"].split(';')[0]
         
         
         cabeca = {
          'user-agent': userags,
          'origin': 'https://www.nettunnel.xyz',
          'Host': 'www.nettunnel.xyz',
          'referer': self.UrlGet,
          'x-requested-with': 'XMLHttpRequest',
          'cookie': phpssid
                  }
                  
         NetTunnelUser = json.loads(requests.post(self.UrlPost, data = '', headers = cabeca).text)
         print(NetTunnelUser)
 

         print('Usuario: ' + NetTunnelUser["user"] + '\n' + 'Senha: ' + str(NetTunnelUser["pass"]) + '\n' + 'Dominio: ' + str(NetTunnelUser["ip"]) + '\n' +'Porta Websocket: 80' + '\n' + 'Porta SSL: 443' '\n\n' + 'Payload: ' + '\n\n' + 'GET / HTTP/1.1[crlf]Host: ' + str(NetTunnelUser["ip"]) + '[crlf]Upgrade: websocket[crlf][crlf]' )
      
      except: 
         print('Erro de conexão, faça o processo sem VPN')
SSH()
print()
input('Pressione enter para sair ')
exit()





