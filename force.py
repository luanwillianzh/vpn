#!/usr/bin/python
import os
import time
import requests
import json
import requests
from requests.structures import CaseInsensitiveDict

BRANCO='\033[1;29m'
VermelhoAll='\e[01;37;41m'
NADA='\033[0m'
CINZA='\e[02;37m'
DESTACAR='\e[01;37m'
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
SCOLOR='\033[0m'
SEMCOR='\033[8m'
BrancoAll='\033[03;37;47m'
LETRAPRETA='\033[02;30;47m'



os.system('clear')
print()
print("     ===================================")
print("                    MBS FREE     ")
print("         ===================================")
print("                ESCOLHA UMA OPÇÃO\n")
print("        ===================================")
print("              [ 1 ] - Vivo")
print("              [ 2 ] - Oi")
print("              [ 0 ] - Sair")
print("         ===================================")
print()
 
print("@alpacinoo007")
print("@luanw04")
print()
option = input("ESCOLHA UMA OPÇÃO: ")

print()
print()

if( option == '1' or option == '01'):
 os.system('clear')
 OPERADORA = "VIVO"
 BANNER = f"============================================{NADA}\n{LETRAPRETA}                  MBS {OPERADORA}                  {NADA}\n============================================{NADA}"
 print(f"{BANNER}")
 print("1 - PROCURAR PASS")
 print("2 - PASS PERSONALIZADO")
 print("0 - SAIR")
 print()
   
 passi = input("Escolha uma Opção: ")
 
 if passi == "1":
   os.system('clear')
   print(f"{BANNER}")
   print(f"{RED}DESLIGUE O WI-FI, PARE A VPN E LIGUE OS DADOS\nMOVEIS{NADA} PARA O SCRIPT GERAR O {GREEN}PASS{NADA} E CAPTURAR OS\nTOKENS DE ADS QUE ESTÃO ATIVOS NA SUA LINHA\n\n")
   peo = input(f"{NADA}DIGITE ENTER APÓS FAZER TUDO")
   print()
   
   try:    
    access = json.loads(requests.post('http://i.vivo.ddivulga.com/i/gp' , data = {'version' : '2'}).text)
    sctoken = access['sctoken']
   except:
    os.system('clear')
    print(f"{BANNER}\n{RED}PASS INVALIDO{NADA}")
    time.sleep(5)
    exit()

 elif passi == "2":
    os.system('clear')
    print(f"{BANNER}")
    sctoken = input("COLE O PASS: ")
 else:
    exit()
   
 
 UrlReward="http://e.vivo.ddivulga.com/api/clickEvent"
 data = f"slotId=%5B%7B%22slotId%22%3A%22101%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22102%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22103%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22104%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=660224&insertionId=&insertionUUID=&insertionType=&referer=http%3A%2F%2Finternetgratis.vivo.com.br%2F&accessPass={sctoken}"
 url = "http://e.vivo.ddivulga.com/api/v2.1/fetch"
 headers = CaseInsensitiveDict()
 headers["Origin"] = "http://a.vivo.ddivulga.com"
 headers["Content-Type"] = "application/x-www-form-urlencoded"
 reapit=60
   
  
  
elif( option == '2' or option == '02'):
 OPERADORA = "OI  "
 BANNER = f"============================================{NADA}\n{LETRAPRETA}                  MBS {OPERADORA}                  {NADA}\n============================================{NADA}"
 os.system('clear')
 print(f"{BANNER}")
 print("1 - PROCURAR PASS")
 print("2 - PASS PERSONALIZADO")
 print("0 - SAIR")
 print()
   
 passi = input("Escolha uma Opção: ")
 
 if passi == "1":
   os.system('clear')
   print(f"{BANNER}")
   print(f"{RED}DESLIGUE O WI-FI, PARE A VPN E LIGUE OS DADOS\nMOVEIS{NADA} PARA O SCRIPT GERAR O {GREEN}PASS{NADA} E CAPTURAR OS\nTOKENS DE ADS QUE ESTÃO ATIVOS NA SUA LINHA\n\n")
   peo = input(f"{NADA}DIGITE ENTER APÓS FAZER TUDO")
   print()
   UrlReward="http://e.oi.ddivulga.com/api/clickEvent"

   try:    
    access = json.loads(requests.post('http://e.oi.ddivulga.com/api/gp' , data = {'version' : '2'}).text)
    sctoken = access['sctoken']
   except:
    os.system('clear')
    print(f"{BANNER}\n{RED}PASS INVALIDO{NADA}")
    time.sleep(5)
    exit()
 
 elif passi == "2":
    os.system('clear')
    print(f"{BANNER}")
    sctoken = input("COLE O PASS: ")
 else:
    exit()
    
 data = f"slotId=%5B%7B%22slotId%22%3A301%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=822068&insertionId=&insertionUUID=&insertionType=ANY&referer=&accessPass={sctoken}"
 url = "http://e.oi.ddivulga.com/api/v2.1/fetch"
 headers = CaseInsensitiveDict()
 headers["Origin"] = "http://e.oi.ddivulga.com"
 headers["Content-Type"] = "application/x-www-form-urlencoded"
 reapit=9999
   
   


else:
  os.system('clear')
  exit()

os.system('clear')
print(f"{BANNER}\nPROCURANDO TOKENS...")
time.sleep(3)
try:
 fetch = requests.post(url, headers=headers, data=data).text
 X9deToken = json.loads(fetch)

except:
 os.system('clear')
 print(f"{BANNER}\n{RED}PASS INVALIDO{NADA}")
 time.sleep(5)
 exit()

advid = [ ]
impressionid = [ ]
tokens_on = 0
iu = 0

while iu < 18:
 iu = iu + 1
 
 try:
  advid.append(X9deToken[f'10{iu}']['advId'])
  
  impressionid.append(X9deToken[f'10{iu}']['impressionEventId'])
  
  tokens_on = tokens_on + 1
  
 except:
  pass
Numero = X9deToken['msisdn']
if tokens_on == '0':
   os.system('clear')
   print(f"{BANNER}")
   print(f"NUMERO DE TELEFONE: {GREEN}{Numero}{NADA}")
   print(f"TOKENS ENCONTRADOS: {GREEN}{tokens_on}{NADA}")
   print()
   print(f"0 - SAIR {RED}NENHUM TOKEN ENCONTRADO{NADA}")
   print()
   resl = input("Escolha uma opção: ")
   exit()
else:
   os.system('clear')
   print(f"{BANNER}")
   print(f"NUMERO DE TELEFONE: {GREEN}{Numero}{NADA}")
   print(f"TOKENS ENCONTRADOS: {GREEN}{tokens_on}{NADA}")
   print()
   print(f"1 - TESTAR TOKENS ENCONTRADOS {GREEN}INICIAR O ENVIO DOS MBS{NADA}")
   print(f"0 - SAIR {RED}NENHUM TOKEN ENCONTRADO{NADA}")
   print()
   resl = input("Escolha uma opção: ")
   
   if resl == '1':
     print()
     
   else:
     exit()

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

for ih in range(999):
 for token in range(tokens_on):
  testador = 0
  testador = testador + 1
  print()
  print(f"{NADA}{LETRAPRETA}           TESTADOR {testador}           {NADA}")
  
  try:
    contagem = 0
    while contagem < reapit:
      
      time.sleep(0.9)
      contagem = contagem + 1
      
      resp = requests.post("http://e.vivo.ddivulga.com/api/clickEvent", headers=headers, data=f"advId={advid[token]}&eventImpressionId={impressionid[token]}&apass={sctoken}").text
      
      if 'evtClickId' in resp:
        print(f"{GREEN}Ganhei 10MBs - {contagem}{NADA}")
      
      else:
        print(f"{RED}Merda de ads{NADA}")
        time.sleep(4)
        contagem = reapit
  except:
    pass

 os.system('clear')
 testestokens = 0
 testestokens = testestokens + 1
 print(f"{BANNER}")
 print(f"NUMERO DE TELEFONE: {GREEN}{Numero}{NADA}")
 print(f"TESTE COM ESSES TOKENS: {GREEN}{testestokens}{NADA}")
 print()
 print(f"1 - TESTAR TOKENS NOVAMENTE {GREEN}REINICIAR INICIAR O ENVIO DOS MBS{NADA}")
 print()
 optio = input("Escolha uma Opção: ")
 
 if option == '1':
    print()
 else:
    print()
   
