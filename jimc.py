import requests
from bs4 import BeautifulSoup

# html_content = requests.get("https://www.geeksforgeeks.org/").text
# soup = BeautifulSoup(html_content,'html.parser')
# # print(soup) Abhi sab aesi hi uth kar agaya h
# formatted_text = soup.prettify()
# # FOr store this information in file
# # print(formatted_text)
# img_count = soup.find_all('img')
# counting = len(img_count)
# print(f"The image tag is {counting}")

# a_count = soup.find_all('a')
# counting_a = len(a_count)
# print(f"The a tag is {counting_a}")

# text_find = soup.find("div",class_='text').text
# # print(text_find)
# # print((soup.title).text)
# paragraph = soup.find('p')
# # print(paragraph)

# anchors = soup.find_all('a')
# all_links = set()
# for link in anchors:
#     if (link.get("href")!="#"):
#         linkText = link.get('href')
#         all_links.add(linkText)
#         print(linkText)

#################### JImshaped practice #################################################
url2 = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
html_text = url2.text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for index,job in enumerate(jobs):
    company_name = job.find('h3',class_='joblist-comp-name').text
    skills = job.find('span',class_='srp-skills').text.replace(' ','')
    published_date = job.find('span',class_='sim-posted').text.replace(' ','')
    more_info = job.header.h2.a['href']
    with open(f'{index}.txt','w') as f:
        f.write(f"Comapany name : {company_name.strip()}\n")
        f.write(f"Required Skills : {skills.strip()}\n")
        f.write(f'Published Date : {published_date.strip()}\n')
        f.write(f'For more information please click on this link : {more_info}\n')

    print(f'File saved {index}')
