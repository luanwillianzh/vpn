#!/bin/bash

RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
SCOLOR='\033[0m'

clear
echo "----------------------------"
echo "   VPN TERMUX   "
echo "----------------------------"
echo "Escolha o Metodo de Conexão"
echo "----------------------------"
echo "0 - SSH Direct "
echo "1 - PAYLOAD "
echo "2 - SSL "
echo "3 - SSL+PAYLOAD "
echo "----------------------------"
echo
echo "Vivo e Claro: Opção 1"
echo "Tim: Opção 3"
echo

read -p  "Escolha uma Opção : " mode
find=`cat settings.ini | grep "connection_mode = " |awk '{print $3}'`

sed -i "s/connection_mode = $find/connection_mode = $mode/g" settings.ini

sleep 1

killprocess() {
echo -e "${RED} vpn service stopped" 
python pidkill.py >> /dev/null &
rm logs.txt
echo -e " ${SCOLOR}"
}

function connect() {
	screen -AmdS nohub python3 tunnel.py
	sleep 1
	if [ "$mode" = '0' ] || [ "$mode" = '1' ]
	then

		screen -AmdS nohub python3 ssh.py 1
	elif [ "$mode" = '2' ] || [ "$mode" = '3' ]
		then 
			
			screen -AmdS nohub python3 ssh.py 2
	else
		echo -e "${RED}wrong choice\ntry again${SCOLOR}"
		python3 pidkill.py
		exit
	fi

	echo -e "${YELLOW}---logs----${SCOLOR}"

	sleep 10
	cat logs.txt

	var=`cat logs.txt | grep "CONNECTED SUCCESSFULLY"|awk '{print $4}'`
	if [ "$var" = "SUCCESSFULLY" ];then 
		echo -e "${GREEN}---Tunneling  starts-----"
		chmod +x proxification
		./proxification > /dev/null
		echo -e "${SCOLOR}"
		iptables --flush
		
	else
		echo -e "${RED}failed! ${SCOLOR}"
	fi
}
connect 
for i in {1..3}
do 
	
	killprocess
	echo -e "${GREEN}"
	read -p "reconnect ? [y\n] " reconnect
	if [ "$reconnect" = 'y' ]  || [ "$reconnect" = 'Y' ]
	then 
		echo -e "reconnecting ${SCOLOR}"

		connect
	else 
		exit
	fi 

done




