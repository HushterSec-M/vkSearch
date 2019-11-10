import requests, time, os
import getNames

print("__VK_MODULE_IS_ACTIVE__")

def printResultInFile(resultSearch):
    if resultSearch:
        for i in range(1, 21):
            try:
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images\\' + str(i) + '.jpg')
                os.remove(path)
            except: continue
        for i, item in enumerate(resultSearch[:20], 1):
            img = requests.get(item['photo_100'])
            with open('images/' + str(i) + '.jpg', 'wb') as img_file:
                img_file.write(img.content)

        with open("result.txt", "wt", encoding="utf-8") as t:
            for item in resultSearch:
                for elem in item:
                    try:
                        t.write(str(item[elem]) + " | ")
                    except:
                        t.write(" | ")
                t.write("\n")
    else:
        print(":(")


def main(stringSearch):
    API = "https://api.vk.com/method"
    ACCESS_TOKEN = []
    V = 5.80
    i = 0

    with open("ACCESS_TOKENS.txt") as at:
        for line in at.readlines():
            token = line.replace("\n", "")
            response = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&v={V}")
            print(f"'{token}' : ")
            try:
                if response.json()["response"]:
                    ACCESS_TOKEN.append(token)
                    print(" [VALID] ")
                    print(f" -> {response.json()['response'][0]['first_name']} {response.json()['response'][0]['last_name']}<br>")
            except:
                print(" [NOT VALID] ")
                print(f" -> {response.json()['error']['error_msg']}<br>")

    print("<br>")
    ALLresult = []
    timeforsleep = 0.3
    names = getNames.main(stringSearch)
    try:
        lastname = stringSearch.split()[1]
    except:
        lastname = ""
    for name in names:
        i = i % len(ACCESS_TOKEN)
        code = '''
        var offset = 0;
        var i = 0;
        var users = [];
        var q = "''' + name + ' ' + lastname + '''";
        var result = [];
        do {
            result = API.users.search({"q":q, "count":1000, "offset": offset, "fields":"domain, photo_100"});
            users = users + result.items;
            offset = offset + 1000;
        } while (result.count != 0)
        return users;
        '''
        response = requests.post(url=f"{API}/execute",
                                 data={
                                     "code": code,
                                     "access_token": ACCESS_TOKEN[i],
                                     "v": V,
                                 })
        result = response.json()['response']
        for item in result:
            if item['id'] not in [item['id'] for item in ALLresult]:
                ALLresult.append(item)
        time.sleep(timeforsleep)
    print("<span>" + ", ".join(names) + "</span>")
    return ALLresult
    #printResultInFile(ALLresult)
