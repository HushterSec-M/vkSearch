import requests, json
API = "https://api.vk.com/method"
V = 5.84
'''token = "80e4a003f1be360834cc6b1a2cd1e3eb322094eb204ccd7c7d52de775e797a3e0fbd927646b2435c1581d"
response = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&v={V}")
print(response.json())


token = "0c0e49a889461c104d365a40a388382243abbe4a63d497f30cd58b1aa42e597a6d9e75700ee147d2ca438"
response = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&v={V}")
print(response.json())
'''
with open("ACCESS_TOKENS.txt") as at:
    for line in at.readlines():
        token = line[:-1]
        response = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&v={V}")
        print(f"'{token}' : ", end = "")
        try:
            if response.json()["response"]:
                print(" [VALID] ", end = "")
                print(f" -> {response.json()['response'][0]['first_name']}")
        except:
            print(" [NOT VALID] ", end = "")
            print(f" -> {response.json()['error']['error_msg']}")