"""To do
- Simulate values that evolve with varying distributions. Some random walk, some geomtric walk, ect.
"""

import pandas as pd
import numpy as np
from pathlib import Path

from torch import normal

rng = np.random.default_rng()

from classes import Company, Investor
from valuation_funcs import ddm_valuation

# Market Variables
# Yield Curve

folder_path = Path(__file__).parent

# Load S&P companies
df_sp = pd.read_csv(folder_path / 'data' / 'sp_500_members.csv')
tickers = df_sp.iloc[:10].tic.to_list()


sim_dates = pd.date_range('2000-01-01','2002-01-01')

df_company_vals:pd.DataFrame = pd.DataFrame(index=sim_dates,columns=tickers)
asset_count = len(tickers)
# Put Random starting valuations
df_company_vals.iloc[0] = 10**rng.choice(range(5,9),asset_count)


for i in range(1,len(sim_dates)):
    # Need to replace below with better simulation assumption.
    # Each using its cost of capital?

    df_company_vals.iloc[i] = df_company_vals.iloc[i-1] * (1+rng.normal(loc=.17/365,scale=.2/365**.5,size=asset_count))


print('done')