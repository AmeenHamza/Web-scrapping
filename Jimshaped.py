# FIrst we install lxml parser library 
from bs4 import BeautifulSoup
import requests
import time

# print(url)
# now i am going to create a object of Beautiful soup
 # Idher ham html.parser bhi karsakte h
#  Ab ye hamari pehli class h main jis mein sari jobs h ab ek ek job k lye kya alag alag code likhna parega nhi iske lye ham isi parent class karte hue for loop se kaam lainge
# print(company) # Ye pehli job ki company ka naam lakar dega
# Ager iska text chaihiye to .text lagana parega
# print(jobs) # YE main class h jiss mein sari jobs ki detail h to baqi jobs ko ham ishi se call karsakte h
# For post of job kitna time hogaya h job ko post kiye hue
# print("Put some skills that you are not familiar with")
# unfamiliar_skills = input('>')
# print(f'Filtering out {unfamiliar_skills} ')
print("Put some skills that you are not familiar with")
unfamiliar_skills2 = input('>')
print(f'Filtering out {unfamiliar_skills2} ')


def findjobs():
    url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
    html_content = url.text
    soup = BeautifulSoup(html_content,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx') # This find all the jobs on the job find_all()
    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').text
        if 'few' in published_date: # Hamin khali wo jobs chihiyen jo few days pehli ki hon
        # company_name = job.find('h3',class_='joblist-comp-name') # Jis cheez ko find karna ho uskpe click karke usko inspect karo to uske code per lejaega 
            company_text = job.find('h3',class_='joblist-comp-name').text.replace(' ','') # FOr deleting the spaces
            skills = job.find('span',class_='srp-skills').text.replace(' ','') # This is the requirment of first company
            more_info = job.header.h2.a['href'] # Ager href ko list mein nhi likhainge to ye bhi saat mein print hoga ye karne se khali iska content print hoga

            if unfamiliar_skills2 not in skills: # Ye ye karega k jo skills user enter karega usko chorke sab dikhaega jis company ki wo skills hongi wo bhi nhi aaegi
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company name : {company_text.strip()}\n")
                    f.write(f"Required Skills : {skills.strip()}\n")
                    f.write(f"More Info : {more_info}\n")

                print(f'File saved : {index}')

# Here i write a code for running a program every 10 minutes
if __name__ == '__Jimshaped__':
    while True:
        findjobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes ...")
        time.sleep(time_wait * 60)

findjobs()