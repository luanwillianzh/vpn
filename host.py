import requests

file = open("hosts.txt", "r")
linha = file.readlines()

for i in linha:
    t = i.replace("\n", "")
    try:
        r = requests.get(f"https://{t}", timeout=5)
        print(f"{t} - OK")
    except:
        pass
