import requests 
from bs4 import BeautifulSoup

URL = 'https://www.amazon.it/Philips-Ambiance-Starter-Lampadine-Bridge/dp/B0797WGVWW?ref_=Oct_DLandingS_D_e9452f01_60&smid=A11IL2PNWYJU7H' #change the url here

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle") 

print(title)



