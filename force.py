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


def Main():
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
  print("0 - VOLTAR")
  print()
   
  passi = input("Escolha uma Opção: ")
 
  if passi == "1":
    os.system('clear')
    print(f"{BANNER}")
    print(f"{RED}DESLIGUE O WI-FI, PARE A VPN E LIGUE OS DADOS\nMOVEIS{NADA} PARA O SCRIPT GERAR O {GREEN}PASS{NADA} E CAPTURAR OS\nTOKENS DE ADS QUE ESTÃO ATIVOS NA SUA LINHA\n\n")
    time.sleep(5)
    peo = input(f"{NADA}DIGITE {GREEN}ENTER{NADA} APÓS FAZER TUDO")
    print()
   
    try:    
     access = json.loads(requests.post('http://i.vivo.ddivulga.com/i/gp' , data = {'version' : '2'}).text)
     sctoken = access['sctoken']
    except:
     os.system('clear')
     print(f"{BANNER}\n{RED}Merda de pass{NADA}")
     time.sleep(5)
     Main()

  elif passi == "2":
     os.system('clear')
     print(f"{BANNER}")
     sctoken = input(f"COLE O PASS: {GREEN}")
  elif passi == "0":
     Main()
  else:
     Main()
   
   
  op = "VIVO"
  UrlReward="http://e.vivo.ddivulga.com/api/clickEvent"
  data = f"slotId=%5B%7B%22slotId%22%3A%22101%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22102%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22103%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22104%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22105%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22106%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22107%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22108%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22109%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=660224&insertionId=&insertionUUID=&insertionType=&referer=http%3A%2F%2Finternetgratis.vivo.com.br%2F&accessPass={sctoken}"
  url = "http://e.vivo.ddivulga.com/api/v2.1/fetch"
  headers = CaseInsensitiveDict()
  headers["Origin"] = "http://a.vivo.ddivulga.com"
  headers["Content-Type"] = "application/x-www-form-urlencoded"
  reapit=999
   
  
  
 elif( option == '2' or option == '02'):
  OPERADORA = "OI  "
  BANNER = f"============================================{NADA}\n{LETRAPRETA}                  MBS {OPERADORA}                  {NADA}\n============================================{NADA}"
  os.system('clear')
  print(f"{BANNER}")
  print("1 - PROCURAR PASS")
  print("2 - PASS PERSONALIZADO")
  print("0 - VOLTAR")
  print()
   
  passi = input("Escolha uma Opção: ")
 
  if passi == "1":
    os.system('clear')
    print(f"{BANNER}")
    print(f"{RED}DESLIGUE O WI-FI, PARE A VPN E LIGUE OS DADOS\nMOVEIS{NADA} PARA O SCRIPT GERAR O {GREEN}PASS{NADA} E CAPTURAR OS\nTOKENS DE ADS QUE ESTÃO ATIVOS NA SUA LINHA\n\n")
    time.sleep(5)
    peo = input(f"{NADA}DIGITE {GREEN}ENTER{NADA} APÓS FAZER TUDO")
    print()
    UrlReward="http://e.oi.ddivulga.com/api/clickEvent"

    try:    
     access = json.loads(requests.post('http://e.oi.ddivulga.com/api/gp' , data = {'version' : '2'}).text)
     sctoken = access['sctoken']
     
    except:
     os.system('clear')     
     print(f"{BANNER}\n{RED}MERDA DE PASS{NADA}")
     time.sleep(5)
     Main()
 
  elif passi == "2":
     os.system('clear')
     print(f"{BANNER}")
     sctoken = input(f"COLE O PASS: {GREEN}")
  elif passi == "0":
     Main()
  else:
     Main()
  op = "OI"
  UrlReward="http://e.oi.ddivulga.com/api/clickEvent"
  data = f"slotId=%5B%7B%22slotId%22%3A301%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=822068&insertionId=&insertionUUID=&insertionType=ANY&referer=&accessPass={sctoken}"
  url = "http://e.oi.ddivulga.com/api/v2.1/fetch"
  headers = CaseInsensitiveDict()
  headers["Origin"] = "http://e.oi.ddivulga.com"
  headers["Content-Type"] = "application/x-www-form-urlencoded"
  reapit=9999
   
   

 elif option == "0":
     os.system('clear')
     exit()
 else:
   os.system('clear')
   Main()
      
 advid = [ ]
 impressionid = [ ]
 tokens_on = 0
 iu = 0
 AdvName = [ ]
 
 buscar(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, tokens_on, AdvName, iu, op)

 
def buscar(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, tokens_on, AdvName, iu, op):
 os.system('clear')
 print(f"{NADA}{BANNER}\nPROCURANDO ARQUIVOS QUE ROTIA...")
 time.sleep(4)
 try:
  X9deToken = json.loads(requests.post(url, headers=headers, data=data).text)

 except:
  os.system('clear')
  print(f"{BANNER}\n{RED}MERDA DE PASS{NADA}")
  time.sleep(5)
  Main()

 tokensnovos = 0
 while iu < 4:
  iu = iu + 1
  try:
  
   advidchecar = (X9deToken[f'10{iu}']['advId'])
   
   if advidchecar in advid:
    pass
   else:
    advid.append(X9deToken[f'10{iu}']['advId'])
   
   impressionidcheck = (X9deToken[f'10{iu}']['impressionEventId'])
   
   if impressionidcheck in impressionid:
    pass
   else:
    impressionid.append(X9deToken[f'10{iu}']['impressionEventId'])
   
   AdvNamecheck = (X9deToken[f'10{iu}']['advName'])
   
   if AdvNamecheck in AdvName:
    pass
   
   else:   
    AdvName.append(X9deToken[f'10{iu}']['advName'])
   
   tokens_on = tokens_on + 1
   tokensnovos = tokensnovos + 1
  except:
   pass
   
 Numero = X9deToken['msisdn']
 FreeFire(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, AdvName, iu, op, tokensnovos, tokens_on, Numero)

def FreeFire(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, AdvName, iu, op, tokensnovos, tokens_on, Numero):


 os.system('clear')
 print(f"{BANNER}")
 print(f"{GREEN}{tokensnovos} TOKENS NOVOS FORAM ENCONTRADOS{NADA}")
 print()
 print(f"{GREEN}TOTAL DE TOKENS: {NADA} {GREEN}{tokens_on}{NADA}")
 print(f"{GREEN}NUMERO DE TELEFONE:{NADA} {GREEN}{Numero}{NADA}")
 print()
 print(f"1 - BUSCAR MAIS TOKENS {GREEN}ESTOQUE DE MBS{NADA}")
 print(f"2 - TESTAR TOKENS ENCONTRADOS {GREEN}FF PING BAIXO ON{NADA}")
 print(f"3 - TESTAGEM INDIVIDUAL {GREEN}SOCAR NA {op} AOS POUCOS{NADA}")
 print(f"0 - VOLTAR {RED}MERDA DE CHIP{NADA}")
 print()
 resl = input("Escolha uma opção: ")
 
 if resl == '2':
  pass
   
 elif resl == '1':
  buscar(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, tokens_on, AdvName, iu, op)    
  
 elif resl == '3':
   TestagemIndividual(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data, tokensnovos, tokens_on)
 
 elif resl == '0':
  Main()
 else:
  FreeFire(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, AdvName, iu, op, tokensnovos, tokens_on, Numero)
 
 print()
 headersi = CaseInsensitiveDict()
 headersi["Content-Type"] = "application/x-www-form-urlencoded"

 testador = 0
 testestokens = 0


 Envio(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, tokens_on, testador, testestokens, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data)


def Envio(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, tokens_on, testador, testestokens, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data):
 os.system('termux-wake-lock')
 for token in range(tokens_on):
  
  testador = testador + 1
  print()
  print(f"{NADA}{LETRAPRETA}           TESTADOR {testador}           {NADA}")
  print(f"{YELLOW}Adv Name: {AdvName[token]}")
  print(f"ImpressionID: {impressionid[token]}")
  print(f"AdvID: {advid[token]}{NADA}")
   
  try:
    contagem = 0
    while contagem < reapit:
      
      time.sleep(0.7)
      contagem = contagem + 1
      
      resp = requests.post(UrlReward, headers=headers, data=f"advId={advid[token]}&eventImpressionId={impressionid[token]}&apass={sctoken}").text
      
      if 'evtClickId' in resp:
        print(f"{GREEN}PARTIDAS NO FREE FIRE - {contagem}{NADA}")
      
      else:
        print(f"{RED}MERDA DE ADS{NADA}")
        time.sleep(4)
        contagem = reapit
  except:
    pass
    
 testestokens = testestokens + 1
 Acabou(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, tokens_on, testador, testestokens, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data)

def Acabou(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, tokens_on, testador, testestokens, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data):

 os.system('clear')
 print(f"{BANNER}")
 print(f"{GREEN}NUMERO DE TELEFONE: {GREEN}{Numero}{NADA}")
 print(f"{GREEN}TESTE COM ESSES TOKENS: {testestokens}{NADA}")
 print()
 print(f"1 - BUSCAR NOVOS TOKENS {GREEN}ESTOQUE DE MBS{NADA}")
 print(f"2 - TESTAR TOKENS NOVAMENTE {GREEN}ASSIM A {op} VAI PRO SACO{NADA}")
 print(f"0 - VOLTAR {RED}MERDA DE CHIP{NADA}")
 print()
 option = input("Escolha uma Opção: ")
 
 if option == '2':
    testador = 0
    Envio(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, tokens_on, testador, testestokens, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data)
 
 if option == '1':
  advid = [ ]
  impressionid = [ ]
  tokens_on = 0
  iu = 0
  AdvName = [ ]
  buscar(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, tokens_on, AdvName, iu, op)
 elif option == "0":
    testador = 0
    Main()    
    
 else:
    Acabou(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, tokens_on, testador, testestokens, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data)
    

def TestagemIndividual(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data, tokensnovos, tokens_on):
 os.system('clear')
 print(f"{BANNER}")
 print(f"{GREEN}NUMERO DE TELEFONE: {GREEN}{Numero}{NADA}")
 print()
 try:
  contar = 0
  for i in range(tokens_on):
   contar = contar + 1
   print(f"ADS {contar}")
   print(f"{YELLOW}Adv Name: {AdvName[i]}")
   print(f"ImpressionID: {impressionid[i]}")
   print(f"AdvID: {advid[i]}{NADA}")
   print()
 except:
  buscar(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, tokens_on, AdvName, iu, op)
 
 print("0 - VOLTAR") 
 print()
 try:
  Escolha = int(input("Escolha um ADS: "))
  if Escolha == 0:
   FreeFire(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, AdvName, iu, op, tokensnovos, tokens_on, Numero)

  else:
   pass
 except:
  TestagemIndividual(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data, tokensnovos, tokens_on)
  
 print()
 print(f"{NADA}{LETRAPRETA}           TESTAGEM INICIADA           {NADA}")
 try:
  contagem = 0
  Escolha = Escolha - 1
  while contagem < reapit:
      
   time.sleep(0.7)
   contagem = contagem + 1
      
   resp = requests.post(UrlReward, headers=headers, data=f"advId={advid[Escolha]}&eventImpressionId={impressionid[Escolha]}&apass={sctoken}").text
      
   if 'evtClickId' in resp:
    print(f"{GREEN}PARTIDAS NO FREE FIRE - {contagem}{NADA}")
      
   else:
    print(f"{RED}MERDA DE ADS{NADA}")
    time.sleep(4)
    contagem = reapit
 except:
   pass  
  
 os.system('clear')
 print(f"{BANNER}")
 print(f"{GREEN}NUMERO DE TELEFONE: {GREEN}{Numero}{NADA}")
 print()
 print(f"1 - ESCOLHER OUTRO TOKEN {GREEN}SOCAR MAIS UM POUCO{NADA}")
 print(f"2 - BUSCAR NOVOS TOKENS {GREEN}ASSIM A {op} VAI PRO SACO{NADA}")
 print(f"0 - VOLTAR {RED}MERDA DE CHIP{NADA}")
 print()
 option = input("Escolha uma Opção: ")
 
 if option == '1':
  TestagemIndividual(BANNER, NADA, LETRAPRETA, advid, impressionid, GREEN, RED, Numero, sctoken, reapit, headers, AdvName, UrlReward, url, op, iu, data, tokensnovos, tokens_on)
 
 elif option == '2':
  buscar(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, tokens_on, AdvName, iu, op)
 
 elif option == '3':
  Main()
  
 else: 
  FreeFire(BANNER, url, headers, data, RED, GREEN, NADA, sctoken, reapit, UrlReward, impressionid, advid, AdvName, iu, op, tokensnovos, tokens_on, Numero)
  
  
    
Main()
