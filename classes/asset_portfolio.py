import csv

from classes.digital_asset import DigitalAsset
from classes.mobile_app import MobileApp
from classes.website import Website

class AssetPortfolio:
    def __init__(self):
        self.__assets = []
        self.__file_name = "digital_asset.csv"

    def add_asset(self, asset):
        self.__assets.append(asset)

    def calculate_total_net_worth(self):
        sum = 0
        for asset in self.__assets:
            sum += asset.calculate_value()
            sum -= asset.get_cost
        return sum





    def save_portfolio(self):
        with open(self.__file_name,"w",newline= "") as f:
            for asset in self.__assets:
                f.write(asset.to_report_line())


    def load_portfolio(self):
        self.__assets = []
        with open(self.__file_name,"r") as f:
            try:
                csv_1 = csv.reader(f)
            except FileNotFoundError:
                print("this file not exist")
            for row in csv_1:
                if type == "MOBILE_APP":
                    print("d")





a = MobileApp("sda",123.3,213,213)
b = Website("sda",123.3,213,213)

asset = AssetPortfolio()
asset.add_asset(a)
asset.add_asset(b)
print("----")
print(asset.calculate_total_net_worth())
asset.save_portfolio()
print(asset.load_portfolio())