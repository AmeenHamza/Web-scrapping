import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
html_text = url.text
soup = BeautifulSoup(html_text,'html.parser')

head = soup.find_all('div',class_='_3pLy-c row')
# print(len(head)) # There are 24 products present on the webpage


# Now i am trying for find the head of the phone
names = soup.find_all('div','_4rR01T')
# print(name)
for index,name in enumerate(head):
    bname = name.find('div','_4rR01T').text
    description = name.find('div','fMghEO').text
    ratings = name.find('div','gUuXy-').text
    price = name.find('div','_30jeq3 _1_WHN1').text
    with open(f'phone {index}.txt','w') as f:
        print(f"Mobile Name : {bname}")
        print(f"Description : {description}")
        print(f"Ratings : {ratings}")
        print(f"Price : {price}")
    

    print(f'File {index} saved !')

