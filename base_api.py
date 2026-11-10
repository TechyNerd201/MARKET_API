from abc import ABC, abstractmethod
import pandas_market_calendars as mcal

class BaseApi(ABC):
    @abstractmethod
    def get_company_info(self):
        pass
    @abstractmethod
    def get_historical_data(self):
        pass
    @abstractmethod
    def corporate_actions(self):
        pass

    @abstractmethod
    def get_indexes_data(self):
        pass
    @staticmethod
    def get_market_calender(self, stock_exchange:str):
        # Load the National Stock Exchange of India calendar
        nse = mcal.get_calendar('NSE')

        # Get valid trading days for a date range (excluding weekends and holidays)
        schedule = nse.schedule(start_date='2026-01-01', end_date='2026-12-31')
        trading_days = mcal.date_range(schedule, frequency='1D')

        print(schedule[['market_open', 'market_close']].head())

if __name__ == '__main__':

    BaseApi.get_market_calender('AAPL', 'adsfg')