import requests
from bs4 import BeautifulSoup
import facebook
#https://www.facebook.com/search/top/?q=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9%20%D0%A5%D0%B0%D1%80%D1%83%D0%B7%D0%B8%D0%BD&epa=SEARCH_BOX
#https://www.facebook.com/search/top/?q=Алексей%20Харузин&epa=SEARCH_BOX


def get_html(url):
    r = requests.get(url).text
    return r


def parse():
    url = 'https://www.facebook.com/search/top/?q=Алексей%20Харузин&epa=SEARCH_BOX&access_token'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    res = soup.find_all('div', id="BrowseResultsContainer")
    print(res)


parse()



token = "EAAikTQ4gz0UBALbfJh1oQW0j9pFADTurqWaijZB31LZABCOfDGsGUuq9QdkZBJLGYnIg1fy7xKbkNyvz1JZCr5agwl0G6IBW8EcYpPxKQLUMNaoR9keGmjgA3COEV863ahUoLkChTKKCQheNZAZBMER8XEPA2MJRXNNNZBmGDnF64M3iUYeN9GCfnm5GGmwwUjmAVFFgXXQYwZDZD"
url = 'https://graph.facebook.com/v2.0/432234243/feed?limit=1000&access_token=%s' % token
print(url)
'''
import facebook
token='my token'
graph= facebook.GraphAPI(token)
profile=graph.get_object("me")  #extracting your own profile
friends=graph.get_connections("me","friends")['data']
friend_list=[friend['name'] for friend in friends]
print(friend_list)
'''

from facepy import GraphAPI
import json

#Selenium, WebDriver

app_id = "2432450670153541"
app_secret = "7fc2eddd66a85784f7e8d20aed0045ee"
post_login_url = "http://0.0.0.0:8080/"

graph = GraphAPI(token)
print(graph.get('me/posts'))

url_test = 'https://www.facebook.com/search/results.php?q=WORDS&type=groups'


import robobrowser

class Facebook(robobrowser.RoboBrowser):

    url = 'https://facebook.com'

    def __init__(self, email, password):
        self.email = email
        self.password = password
        super().__init__()
        self.login()

    def login(self):
        self.open(self.url)
        login_form = self.get_form(id='login_form')
        login_form['email'] = self.email
        login_form['pass'] = self.password
        self.submit_form(login_form)
log = "89042579915"
pas = "CM753159"
#acc = Facebook(log, pas)

def login(session, email, password):
    '''
    Attempt to login to Facebook. Returns cookies given to a user
    after they successfully log in.
    '''

    # Attempt to login to Facebook
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    assert response.status_code == 302
    assert 'c_user' in response.cookies
    return response.cookies

PROTECTED_URL = 'https://m.facebook.com/groups/318395378171876?view=members'
if __name__ == "__main__":

    session = requests.session()
    cookies = login(session, log, pas)
    response = session.get(PROTECTED_URL, cookies=cookies, allow_redirects=False)
    #assert response.text.find('Home') != -1