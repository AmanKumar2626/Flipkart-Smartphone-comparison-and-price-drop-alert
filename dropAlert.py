import requests 
from bs4 import BeautifulSoup 
import time 
import constant as const
import smtplib


def check_price(): 
	# fetch webpage 
	r = requests.get(const.FLIPKART_URL) 
	# parse the html 
	soup = BeautifulSoup(r.content, 'html5lib') 
	# extract price using class '_16Jk6d' 
	price = soup.find('div', attrs={"class": "_16Jk6d"}).text 
	# remove Rs symbol from price 
	price_without_Rs = price[1:] 
	# remove commas from price 
	price_without_comma = price_without_Rs.replace(",", "") 
	# convert price from string to int 
	int_price = int(price_without_comma) 
	return int_price 

def send_email(website, URL, price):
        
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('amankumarnitkkr@gmail.com', 'eqgpkynahrcuesxy')

    subject = f"Price drop alert for {const.PRODUCT_NAME} on {website}"

    body = f'''Dear {const.USERNAME},

We hope this email finds you well. We wanted to inform you that there has been a significant drop in the price of the product you've been tracking on our platform.

Product: {const.PRODUCT_NAME}
Current Price: {price}
Target Price: {const.WISH_PRICE} 
Website : Flipkart

This is a great opportunity for you to make a purchase and save on your desired product.

Thank you for using our price tracking service, and we hope you enjoy the savings!

Best regards,

URL:- {const.FLIPKART_URL}'''
    msg = f"Subject:{subject}\n{body}"
    server.sendmail('amankumarnitkkr@gmail.com',const.EMAIL_ID, msg)
    print("Email Sent!\n")
    print("--------------------------------------")
    print("Email Content:\n")
    print(msg)
    print("--------------------------------------")
    server.quit()
		
def excute():     
		
    cur_price = check_price() 
    print(f"Current price is {cur_price}") 
    print("We will inform you, once price of product hits out target price") 
    print("Waiting...") 
    while True: 
        # get current price 
        cur_price = check_price() 
        if cur_price <= const.WISH_PRICE: 
          print(f"Its time to buy product, its current price is {cur_price}") 
          send_email('Flipkart', const.FLIPKART_URL, const.WISH_PRICE)
          break
    
        # wait for 1 day to check again
        print("Still not under the target price.") 
        time.sleep(86400) 
