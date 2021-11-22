#!/usr/bin/python
import requests
import os
import time


class IPS:
   def __init__(self, ip, porta, dominio):
      self.gui = ip
      self.gu = porta
      self.gabi = dominio
      self.true = [ ]
      print()
      print()
      try:
         os.system('termux-wake-lock')
      except:
         pass
  
   def tres(self):
     ips2 = self.gui
     for test in ips2:
     
        porta = self.gu   
        domino = self.gabi
        true = self.true
        dominio = f'http://{domino}'
  
        for i in range(255):
           try:
              ip = {'http':f'http://{test}{i}:{porta}'}
              teste = requests.get(dominio, headers = {'Upgrade': 'websocket'}, proxies = ip, timeout = 0.5)
   
              if teste.status_code == 101:
                 print(f'{YELLOW}{test}{i} {NADA}|{GREEN} True - Status Code 101{NADA}')
                 true.append(f"{test}{i}")
   
              elif teste.status_code == 400:
                 print(f'{YELLOW}{test}{i} {NADA}|{GREEN} True - Status Code 400{NADA}')
                 true.append(f"{test}{i}")
   
              else:
                 print(f'{YELLOW}{test}{i} {NADA}|{RED} False {NADA}')
     
     
    
           except:
              print(f'{YELLOW}{test}{i} {NADA}|{RED} False {NADA}')
              time.sleep(0.1)
        print()
        print()
        for i in true:
           print(f"{GREEN}{i} | TRUE")
        print()
        print()
   
   
   
   
   
                     
   def dois(self):
      ips2 = self.gui
      for test in ips2:
         porta = self.gu
   
         domino = self.gabi
         true = self.true
         dominio = f'http://{domino}'  
         contagem = 0
      
         while contagem < 255:   
            for i in range(255):
               try:
                  ip = {'http':f'http://{test}{contagem}.{i}:{porta}'}
                  teste = requests.get(dominio, headers = {'Upgrade': 'websocket'}, proxies = ip, timeout = 0.5)
   
                  if teste.status_code == 101:
                       print(f'{YELLOW}{test}{contagem}.{i} {NADA}|{GREEN} True - Status Code 101 {NADA}')
                       true.append(f"{test}{contagem}.{i}")
   
                  elif teste.status_code == 400:
                     print(f'{YELLOW}{test}{contagem}.{i} {NADA}|{GREEN} True - Status Code 400 {NADA}')
                     true.append(f"{test}{contagem}.{i}")
   
                  else:
                     print(f'{YELLOW}{test}{contagem}.{i} {NADA}|{RED} False {NADA}')
      
     
               except:
                  print(f'{YELLOW}{test}{contagem}.{i} {NADA}|{RED} False {NADA}')
     
            print()
            print()
            for i in true:
               print(f"{GREEN}{i} | TRUE")
            print()
            print()
            contagem = contagem + 1







BRANCO='\033[1;29m'
NADA='\033[0m'
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'

def main():
   os.system("clear")
   print("ESSE SCRIPT SERVE PARA TESTAR IPS DA CLOUDFLARE")
   print()
   print("FUNCIONA COM 2 OU 3 CASAS, EX: 104.10. OU 104.10.10.")
   print()
   ip = []
   uru = input("Digite o ip: ")
   ip.append(uru)
   a = str((uru).replace('.','').isdigit())

   if "True" in a:
      pass
   else:
      main()
 
   print()
 
   porta = input("Digite a porta: ")
   auth = str((porta).replace('.','').isdigit())
 
   if "True" in auth:
      pass
   else:
      main()
 
   print()
   dominer = input("Digite o dominio: ")
   dominio = ((dominer).replace(' ', ''))
   
   print()
   for i in range(999):
      print("Mais algum ip? ")
      print()
      print("1 - Sim")
      print("2 - Não")     
      print()
      milho = input('Escolha uma opção: ')      
      auto = uru.count('.')
   
      if milho == '1':
         print()
         ip.append(input("Digite o IP: "))
         print()
         
      else:
         break
         
         
   if auto == 2:
      IPS(ip, porta, dominio).dois()
 
   if auto == 3:
      IPS(ip, porta, dominio).tres()
 
   else:
      main()

main()
  


   

   
   
   
  
