#!/usr/bin/python
import requests,time,os
os.system('clear')

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
  exit()

advid1 = input("Adv ID: ")
print()
impression1 = input("ImpressionID: ")
print()
accessPass = input("Access Pass: ")
Ganhei="Ganhei 10 MBs - "

print()
print()

contagem = 0
while contagem < 9999:

   carioca = requests.post(UrlReward, 
   data = {'advId' : advid1,'eventImpressionId':impression1,'apass':accessPass} ).text
   
   contagem = contagem + 1
   print(f"{Ganhei}{contagem}")
   time.sleep(1)
print("Merda de ads")
   



      
