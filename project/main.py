import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'https://news.google.com/topstories?hl=es-419&amp;gl=MX&amp;ceid=MX:es-419'

if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text
    
        soup = BeautifulSoup(content, 'html.parser')
        now = datetime.now().strftime('%d-%m-%Y %H:%M')  
        with open(f'news/titles_{now}.txt', 'w+') as file:

            for element in soup.find_all('h4', class_= 'gPFEn', limit=15):
                title = element.text
                file.write(title + '\n')

        print('Done')