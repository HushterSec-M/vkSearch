import json, requests
"""from bs4 import BeautifulSoup

def tanimoto(s1, s2):
    a, b, c = len(s1), len(s2), 0.0
    for sym in s1:
        if sym in s2:
            c += 1

    return c / (a + b - c)

def searchName(name, Sex):
    with open('russian_names.json', 'rt', encoding='utf-8-sig') as fh:
        data = json.load(fh)
    names = [[i['Name'], i['Sex']] for i in data]
    for i in names:
        if (tanimoto(name.lower().replace('е', 'ё'), i[0].lower().replace('е', 'ё')) > 0.7) and (i[1] == Sex):
            yield i[0]


def get_html(url):
    r = requests.get(url).text
    return r


def parse(name):
    url = 'https://ru.wikipedia.org/wiki/' + name
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_="infobox")
    key = table.find_all("th")
    value = table.find_all("td")
    dict = {}
    lkey, lval = len(key), len(value)
    # print(lkey, lval)
    for i in range(min(len(key), len(value))):
        try:
            if lkey == lval:
                dict[key[i].getText()] = value[i].getText()
            elif lkey > lval:
                dict[key[i].getText()] = value[i - (lkey - lval)].getText()
            elif lkey < lval:
                dict[key[i].getText()] = value[i + (lkey - lval)].getText()
        except:
            break
    dict = dict["Производ. формы"]
    dict = dict.replace("\n", "").replace("[", '').replace("]", '').replace("(", '').replace(")", '').replace(" ",
                                                                                                              '').replace(
        ".", '')
    for i in range(100):
        dict = dict.replace(str(i), '')
    dict = dict.split(",")
    dict.append(key[0].getText())
    return dict


def maintmp(stringSearch, SEX):
    try:
        names = []
        names.append(stringSearch.split()[0])
        names += parse(stringSearch.split()[0])
        print("Wikipedia:")
    except:
        print("Local Dict:")
        names = searchName(stringSearch.split()[0], SEX)
    return set(names)
"""
def main(fullname):
    print("Tname:")
    original_name = fullname.split()[0].lower()
    result = [original_name]
    with open('tname.json', 'rt', encoding='utf-8-sig') as fh:
        data = json.load(fh)
    for name in data:
        variable = data[name].split(", ")
        if original_name == name or original_name in variable:
            result+=[name]
            result+=variable
            break
    return set(result)