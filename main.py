import requests
from bs4 import BeautifulSoup as BS

class Coin:
    __name = str
    __symbol = str
    __price = str
    __marketcap = str

    def __init__(self, name : str, symbol : str, price : str, marketcap : str) -> None:
        self.__name = name
        self.__symbol = symbol
        self.__price = price
        self.__marketcap = marketcap

    def getName(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"{self.__name} {self.__symbol} {self.__price} {self.__marketcap}"


def parse_coins() -> list[Coin]:
    url = 'https://coinmarketcap.com/'
    resp = requests.get(url)
    soup = BS(resp.text, "lxml")
    tbody = soup.find("tbody")
    coins = tbody.find_all("tr")
    parsed_coins = []
    
    for coin in coins:
        name = coin.find_all("td")[2]
        symbol = coin.find_all("td")[2].find(class_ = "crypto-symbol")
        marketcap = coin.find(class_ = "sc-7bc56c81-0")
        price = coin.find_all("td")[3]

        if symbol == None:
            symbol = coin.find(class_ = "coin-item-symbol")
        
        if not (marketcap == None):
            parsed_coins.append(Coin(name.text, symbol.text, price.text, marketcap.text))
    return parsed_coins

coins = parse_coins()



for coin in coins:
    print(coin)
    


