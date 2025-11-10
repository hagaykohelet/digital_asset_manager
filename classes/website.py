import datetime

from classes.digital_asset import DigitalAsset
from classes.reportable import Reportable


class Website(DigitalAsset, Reportable):
    def __init__(self, name: str, cost: float, monthly_traffic: int, monetization_rate: float):
        super().__init__(name, cost)
        self.__monthly_traffic = monthly_traffic
        self.__monetization_rate = monetization_rate

    def asset_type(self) -> str:
        return "WEBSITE"

    def calculate_value(self) -> float:
        value = self.__monthly_traffic * self.__monetization_rate * 12
        return value

    def to_report_line(self):
        return f"type: {self.asset_type()},name: {self.get_name}, date: {self.get_registration_date}, cost: {self.get_cost},movement: {self.__monthly_traffic}, monetization: {self.__monetization_rate},current value: {self.calculate_value()},"


d = Website("hagay", 123.3, 213, 213)
print(d.to_report_line())
