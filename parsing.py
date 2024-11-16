import requests
from bs4 import BeautifulSoup

st_accept = "text/html"
st_useragent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 "
                "Safari/537.36 OPR/114.0.0.0")
headers = {
    'Accept': st_accept,
    'User_agent': st_useragent
}

req = requests.get('https://konferencii.ru', headers)
src = req.text
soup = BeautifulSoup(src, 'html.parser')
text_v2 = []
text_html = soup.select('div.index_cat_txt')
text_v1 = [i.text for i in text_html]

for i in text_v1:
    i = i.replace('  ', '')
    text_v2.append(i.split('\n'))
text_v3 = [[] for i in range(len(text_v2))]

for i in text_v2:
    for j in i:
        if j != '':
            text_v3[text_v2.index(i)].append(j)

for i in text_v3:
    for j in i:
        x = i.index(j)
        if x == 0:
            print(f'Время проведения: {j}', end='')
        elif x == 2:
            print(j, end='')
        elif x == 4:
            print(f'Название: {j}')
        elif x == 5:
            print('Темы:', end='')
        elif x == 7:
            print(f'Место проведения: {j}')
        elif x == 8:
            pass
        elif x == 9:
            print(j, end='\n\n')
        else:
            print(j)
input('Press ENTER to exit')
