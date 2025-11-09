from classes.digital_asset import DigitalAsset


class AssetPortfolio:
    def __init__(self):
        self.__assets = []
        self.__file_name = "digital_asset.csv"

    def add_asset(self, asset: DigitalAsset):
        self.__assets.append(asset)

    def calculate_total_net_worth(self):
        asset_cost = []
        for asset in self.__assets:
            asset_cost.append(asset.get_cost)
        return asset_cost


a = DigitalAsset("hagay", 123)
b = DigitalAsset("efrat", 90)

asset = AssetPortfolio()
asset.add_asset(a)
asset.add_asset(b)
print(asset.calculate_total_net_worth())