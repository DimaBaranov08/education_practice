import requests
from bs4 import BeautifulSoup as BS
import os
import json

class Coin:
    name = str
    symbol = str
    price = str
    marketcap = str

    def __init__(self, name : str, symbol : str, price : str, marketcap : str) -> None:
        self.name = name
        self.symbol = symbol
        self.price = price
        self.marketcap = marketcap

    def getName(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"{self.name} {self.symbol} {self.price} {self.marketcap}"
    
class Parser:
    url = str
    coins = []

    def __init__(self):
        self.url = 'https://coinmarketcap.com/'
        self.parseCoins()

    def parseCoins(self):
        resp = requests.get(self.url)
        soup = BS(resp.text, "lxml")
        tbody = soup.find("tbody")
        coins = tbody.find_all("tr")
        for coin in coins:
            name = coin.find_all("td")[2].find("p")
            symbol = coin.find_all("td")[2].find(class_ = "crypto-symbol")
            marketcap = coin.find(class_ = "sc-7bc56c81-0")
            price = coin.find_all("td")[3]

            if symbol == None:
                symbol = coin.find(class_ = "coin-item-symbol")
            
            if not (marketcap == None):
                self.coins.append(Coin(name.text, symbol.text, price.text, marketcap.text))

    def getCoins(self):
        return self.coins
    

class Menu:
    coins = []

    def __init__(self):
        coinParser = Parser()
        self.coins = coinParser.getCoins()
        self.Start()

    def printMenu(self):
        print("1) Вывести все монеты на экран.")
        print("2) Поиск монеты по названию.")
        print("3) Запись данных в файл в формате JSON.")
        print("4) Выход из программы.")


    def Start(self):
        flag = 1
        self.printMenu()
        while(flag):
            
            choice = int(input("Введите число от 1 до 4: "))

            match choice:
                case 1: 
                    self.printCoins()
                    os.system("pause")
                    os.system('cls || clear')
                    self.printMenu()
                case 2:
                    self.searchCoin()
                    os.system("pause")
                    os.system('cls || clear')
                    self.printMenu()
                case 3:
                    self.writeData()
                    os.system("pause")
                    os.system('cls || clear') 
                    self.printMenu()
                case 4:
                    os.system('cls || clear')
                    break

    def searchCoin(self):
        flag = 0
        coinName  = input("Введите полное название монеты: ")
        for coin in self.coins:
            if coinName == coin.getName(): 
                print(coin)
                flag = 1
                break
        if (not flag) : print("Монета не найдена.")

    def writeData(self):
        fileName = "test.txt"

        with open(fileName, "w") as file:
            for coin in self.coins:
                json_coin = json.dumps(coin_serializer(coin))
                file.write(json_coin + "\n")
        print("Данные записаны в файл.\n")

    def printCoins(self):
        for coin in self.coins:
            print(coin)
            

def coin_serializer(coin: Coin):
    return{
        "name" : coin.getName(),
        "symbol" : coin.symbol,
        "price" : coin.price,
        "marketcap" : coin.marketcap 
    }

def coin_desirializer(coin: dict):
    assert len(coin.keys()) == 4
    assert "name" in coin
    assert "symbol" in coin
    assert "price" in coin
    assert "marketcap" in coin
    return Coin(**coin)

menu = Menu()




    


