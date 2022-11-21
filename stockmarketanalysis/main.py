# By: Ryan Alumkal

import requests
from bs4 import BeautifulSoup

#URL = "https://www.google.com/finance/quote/AAPL:NASDAQ?hl=en"
URL = [
"https://www.google.com/finance/quote/TSLA:NASDAQ?hl=en", 
"https://www.google.com/finance/quote/AAPL:NASDAQ?hl=en",
"https://www.google.com/finance/quote/NFLX:NASDAQ?hl=en",
"https://www.google.com/finance/quote/GOOGL:NASDAQ?hl=en"
]

def main():
    soup = BeautifulSoup(page.text, "html.parser")
    company = soup.find('div',{'class': 'zzDege'}).text
    price = soup.find('div', {'class': 'YMlKec fxKbKc'} ).text
    after_hours_down = soup.find('span', {'class': 'JwB6zf'}).text # after hours percentage, change
    print(f"\nCompany: {company}")
    print(f"Price: {price}")
    print(f"After Hours:{after_hours_down}")

if __name__ == '__main__':
    for i in range(len(URL)):
        page = requests.get(URL[i])
        main()