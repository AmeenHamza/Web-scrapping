from bs4 import BeautifulSoup
import requests


url = requests.get('https://www.daraz.pk/products/apple-iphone-14-pro-max-67-inch-display-dual-sim-hongkong-i356873821-s1795445316.html?')
html_content = url.content

soup = BeautifulSoup(html_content,'html.parser')
all_products = soup.find(id='module_product_title_1')
title = soup.find(id='a2a0e.pdp.0.i4.3a99Apu3Apu3Li')
print(title)