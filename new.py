import requests
import bs4

# The task for this web scrapping is that to formatted the html content 
# To find the all image tags
# To find the all anchors tag
url = input("Enter url which you want to scrap a website :")
response = requests.get(url)
# print(type(response))
# print(response.text)

filename = "temp.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")
formatted_text = bs.prettify()
# print(formatted_text)

# FOr store data in file
with open(filename,"w") as f:
    f.write(formatted_text) # File is created now

# FOr finding image tag
list_img = bs.find_all('img')
# FOr counting the image element in list
counting_ele = len(list_img)
print(counting_ele)

# FOr counting anchors tag
anchors_tag = bs.find_all('a')
print(anchors_tag)
counting_a = len(anchors_tag)
print(counting_a)

print(response)