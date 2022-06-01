"""Things to include: 
 - record all trades that occur
"""

import pandas as pd
from pathlib import Path


class Company:

    def __init__(self,ticker:str, shares:float=None, price:float=None,total_value:float=None) -> None:
        self.ticker:str = ticker
        self.shares:float = shares
        self.price:float = price
        self.total_value:float = total_value
        
        self.last_dividend:float = None
        self.beta:float = None
        # fiscal_end_date

    @property
    def market_cap(self):
        return self.shares * self.price


    def __repr__(self) -> str:
        return f'{self.ticker}'


class Investor:
    def __init__(self, name:str='Patrick', capital:float=100_000) -> None:
        self.name = name
        self.capital = capital

        # Positions dataframe will indicate share count. Negative shares can indicate shorts.
        self.positions:pd.DataFrame = pd.DataFrame()
        self.value_estimates:pd.DataFrame = pd.DataFrame()

    def __repr__(self) -> str:
        return f'{self.name}-{self.__class__.__name__}'

class DCFInvestor(Investor):

    def __init__(self, name: str = 'Patrick', capital: float = 100_000) -> None:
        super().__init__(name, capital)

class MarketMaker(Investor):
    pass





vito = DCFInvestor(name='vito',capital=20)



if __name__ == 'main':
    print('done')