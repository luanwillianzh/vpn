import requests

file = open("hosts.txt", "r")
linha = file.readlines()

for i in linha:
    t = i.replace("\n", "")
    try:
        r = requests.get(f"http://{t}")
        print(f"{t} - {r.status_code}")
    except:
        pass
