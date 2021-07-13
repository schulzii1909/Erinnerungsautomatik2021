from bs4 import BeautifulSoup
import requests


url = 'https://nextcloud.industrieschule.de/index.php/apps/files/?dir=/Tauschen/school/Vertretungspl%C3%A4ne'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
anchors = soup.find_all('a', attrs={'class':'name'})

print(anchors)