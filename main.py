# First we install requests
# Second we install bs4
# Third we install html5lib

#      NOw start the working       #
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#  Step :1 : GEt THe HTML First step
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup)
title = soup.title
# print(type(soup)) # Beautifulsoup
# paras = soup.find_all('p')
# print(paras)

# markup = "<p><!-- This is a comment></p>"
# soup2 = BeautifulSoup(markup)
# # print(soup2.p) Ye comment print kardega
# # print(soup2.p.string) # YE only string print karega
# print(type(soup2.p.string))

# GEt anchors tag
# anchors = soup.find_all('a')  idhar find all tha jiski waja se sab tag arahe the
# print(anchors)

# For finding first paragraph  
para1 = soup.find('p')
# print(para1)

paras1 = soup.find('p')['class']

# print(paras1)
# get all the elements of lead class
# print(soup.find_all("p", class_="lead"))

# Get the text from the text
# print(soup.find('p').get_text())

# print(soup.get_text())

# Get all links present on the page
# anchors = soup.find_all('a')
# all_links = set()
# for link in anchors:
#     if (link.get("href")!="#"):
#         linkText = "https://codewithharry.com"+link.get('href')
#         all_links.add(linkText)
#         print(linkText)

# .children function id mein jitne function h wo sare lakar dega ye as a generator kaam karega
# .contents function bhi wohi kaam karega bs ye normally kaam karega
# .strings function import all the strings
# .stripped_strings
imgpreview2 = soup.find(id='imgpreview2' )
# for elem in imgpreview2.stripped_strings:
    # print(elem)
    # print()

# print(imgpreview2.parent)  # Is mein sub kuch ajega is id ka
# for gen in imgpreview2.parents:
    # print(gen.name) # is id k jitne parents h un sab k naam bataega
# print(imgpreview2.next_sibling) # is ke baad wala jo div hoga wo batega

# print(imgpreview2.next_sibling.next_sibling) # is ke baad wala se baad wala jo div hoga wo batega

# print(imgpreview2.previous_sibling) # ye iski peeche wali div ki class laega

print(imgpreview2.previous_sibling.previous_sibling) # ye iski peeche se pichli  wali div ki class laega kyunki wo h nhi
# araha 

ele = soup.select("#search-toggle")  # YE iski class lakar dega
print(ele)



