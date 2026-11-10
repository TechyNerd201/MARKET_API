import  yfinance as yf
from cache.yml_cache import  get_configs

index_configs = get_configs('index_derivations')
# currently supporting NSE and BSE only
class YahooFinanceAPI:
    def __init__(self,  company_names: list , stock_exchange: str ='NSE'):
        self.company_names = company_names
        if stock_exchange == 'NSE':
            self.stock_exchange = 'NS'
        elif stock_exchange == 'BSE':
            self.stock_exchange = 'BO'
        else:
            raise Exception('Invalid stock exchange')

    def get_company_info(self):
        company_info =[]
        for company in self.company_names:
            company = company.strip()
            print(f"{company}.{self.stock_exchange}")
            info = yf.Ticker(f"{company}.{self.stock_exchange}").info
            company_info.append({f'{company}': info})
        return company_info

    def get_historical_data(self , start_date, end_date ):
        historical_data =[]
        for company in self.company_names:
            company = company.strip()
            ticker = yf.Ticker(f"{company}.{self.stock_exchange}")
            data = ticker.history(start=start_date, end=end_date, auto_adjust=False)

            json_data = data.reset_index().to_dict(
                orient="records"
            )
            print(data.columns)
            historical_data.append({f'{company}': json_data})
        return historical_data

    def corporate_actions(self):
        corporate_actions =[]
        for company in self.company_names:
            company = company.strip()
            ticker = yf.Ticker(f"{company}.{self.stock_exchange}").actions
            ticker= ticker.to_dict()
            corporate_actions.append({f'{company}': ticker})

        return corporate_actions

    def get_indexes_data(self,  indexes: list):
        symbols = [index_configs['indexes'][index.strip().upper()]['symbols'][0]['yahoo'] for index in indexes ]
        index_data = yf.download(
        symbols,
        start="2024-01-01",
        end="2026-01-01",
        group_by='ticker'
        )
        return index_data.to_json()



if __name__ == '__main__':
    print(YahooFinanceAPI(company_names=['RELIANCE', 'INFY']).get_index_data(["sensex"]))