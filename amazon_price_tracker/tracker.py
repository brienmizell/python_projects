import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/All-new-Sonos-Beam-built-Streaming/dp/B07D4734HR/ref=sr_1_14?keywords=sonos&qid=1564365907&s=gateway&sr=8-14"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}

def check_price():

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:5])

    if(converted_price < 350):
        send_mail()

    print(converted_price)

    print(title.strip())

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login("brienmizell2@gmail.com", "iricbixiiycsbzbp")

    subject= "Price fell down!"
    body = "Check the Amazon link https://www.amazon.com/All-new-Sonos-Beam-built-Streaming/dp/B07D4734HR/ref=sr_1_14?keywords=sonos&qid=1564365907&s=gateway&sr=8-14"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "brienmizell2@gmail.com",
        "brienmizell@me.com",
        msg
    )

    print("HEY EMAIL HAS BEEN SENT!")

    server.quit()

while(True):
    check_price()
    time.sleep((60 * 60) * 24)