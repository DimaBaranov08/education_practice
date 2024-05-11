import requests
from bs4 import BeautifulSoup as BS
import os


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
    
class Parser:
    __url = str
    __coins = []

    def __init__(self):
        self.__url = 'https://coinmarketcap.com/'
        self.__parseCoins()

    def __parseCoins(self):
        resp = requests.get(self.__url)
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
                self.__coins.append(Coin(name.text, symbol.text, price.text, marketcap.text))

    def getCoins(self):
        return self.__coins
    

class Menu:
    coins = []

    def __init__(self):
        coinParser = Parser()
        self.coins = coinParser.getCoins()
        self.Start()

    def printMenu(self):
        print("1) Вывести все монеты на экран.")
        print("2) Поиск монеты по названию.")
        print("3) Выход.\n")


    def Start(self):
        flag = 1
        self.printMenu()
        while(flag):
            
            choice = int(input("Введите число от 1 до 3: "))

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
                    os.system('cls || clear') 
                    break
                case _:
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


    def printCoins(self):
        for coin in self.coins:
            print(coin)
            

menu = Menu()



    


