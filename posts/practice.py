import requests
from bs4 import BeautifulSoup


# url = requests.get("https://www.youtube.com/c/KGMIT")
# html_content = url.content
# soup = BeautifulSoup(html_content,'lxml')
# formatted_text = soup.prettify()
# print(formatted_text)

url = requests.get('https://Codewithharry.com')
html_content = url.text
soup = BeautifulSoup(html_content,'html.parser')
formatted_text = soup.prettify()
# print(formatted_text)

file_name = 'harry.html'
with open(file_name,'w') as f:
    f.write(formatted_text)

count_a = soup.find_all('a')
all_links = set()
for link in count_a:
    if(link.get('href')!='#'):
        link_text = f'https://Codewithharry.com'+link.get('href')
        all_links.add(link_text)
        print(link_text)