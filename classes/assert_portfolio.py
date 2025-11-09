from classes.digital_asset import DigitalAsset
class AssetPortfolio:
    def __init__(self, file_name):
        self.__assets = []
        self.__file_name = "digital_asset.csv"

    def add_asset(self, asset:DigitalAsset):
        self.__assets.append(asset)
    #
    # def calculate_total_net_worth(self):
    #     for asset in self.__assets:
    #         asset.calculate_value() - asset.cost

