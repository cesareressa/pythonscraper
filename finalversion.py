import requests 
from bs4 import BeautifulSoup
import smtplib #mail protocol


URL = 'https://www.amazon.it/Philips-Ambiance-Starter-Lampadine-Bridge/dp/B0797WGVWW?ref_=Oct_DLandingS_D_e9452f01_60&smid=A11IL2PNWYJU7H' #change the url here

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle") 
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])



    print(converted_price)
    print(title)

    if(converted_price < 200):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('***ADD YOUR EMAIL HERE***', '***ADD YOUR PASSWORD HERE***')       #Modify here

    subject = 'Price went down!'
    body = 'Check the link: https://www.amazon.it/Philips-Ambiance-Starter-Lampadine-Bridge/dp/B0797WGVWW?ref_=Oct_DLandingS_D_e9452f01_60&smid=A11IL2PNWYJU7H '

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        '***ADD YOUR EMAIL HERE***@gmail.com',                                      #Modify here
        '***ADD EMAIL ADDRESS WHERE YOU WANT TO RECEIVE THE EMAIL HERE***',         #Modify here
        msg
    )
    print('email has been sent')

    server.quit()


# check_price()         <--- remove comment here



