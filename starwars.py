#!/usr/bin/python
import requests,time,os

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
print("              [ 0 ] - Voltar")
print("         ===================================")
print()
 
print("@alpacinoo007")
print("@luanw04")
print()
option = input("ESCOLHA UMA OPÇÃO: ")

print()
print()

if( option == '1' or option == '01'):
   UrlReward="http://e.vivo.ddivulga.com/api/clickEvent"
  
elif( option == '2' or option == '02'):
   UrlReward="http://e.oi.ddivulga.com/api/clickEvent"
   
else:
  os.system('clear')
  exit()

advid1 = input("Adv ID: ")
print()
impression1 = input("ImpressionID: ")
print()
accessPass = input("Access Pass: ")
Ganhei="Ganhei 10 MBs - "

print()
print(f"{NADA}{LETRAPRETA}           TESTAGEM INICIADA           {NADA}")

contagem = 0
while contagem < 9999:

   carioca = requests.post(UrlReward, 
   data = {'advId' : advid1,'eventImpressionId':impression1,'apass':accessPass} ).text
   
   contagem = contagem + 1
   time.sleep(1)
   if '"evtClickId"' in carioca:
      print(f"{GREEN}{Ganhei}{contagem}{NADA}")
   else:
      print(f"{RED}Merda de ads{NADA}")
      contagem = "9999"
   



      
