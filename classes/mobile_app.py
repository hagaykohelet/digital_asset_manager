from classes.digital_asset import DigitalAsset
from classes.reportable import Reportable


class MobileApp(DigitalAsset, Reportable):
    def __init__(self, name, cost, downloads, avg_rating):
        super().__init__(name, cost)
        self.__downloads = downloads
        self.__avg_rating = avg_rating

    def asset_type(self) -> str:
        return f"MOBILE_APP"

    def calculate_value(self) -> float:
        value = self.__downloads * 0.5 * self.__avg_rating * 1000
        return value

    def to_report_line(self):
        return f"type: {self.asset_type()},name: {self.get_name}, date: {self.get_registration_date}, cost: {self.get_cost},average raring: {self.__avg_rating}, downloads: {self.__downloads},current value: {self.calculate_value()},"
