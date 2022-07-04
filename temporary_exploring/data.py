import pandas as pd
import numpy as np
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo

# df = pd.read_csv('https://raw.githubusercontent.com/Brandt-moreThan4/Data/main/french_monthly.csv',parse_dates=['date'])
# df['date'] = pd.to_datetime(df.date,format='%Y%m')


# df.to_excel('temp.xlsx')

# class bFrame(pd.DataFrame):
#     pass

#     def describe(self):
#         print(df.mean())

# b = bFrame(df)
# b.describe()

# for row in df.itertuples():
#     print(row)

wb = openpyxl.load_workbook('temp.xlsx')
ws = wb.worksheets[0]
tab = Table(displayName="Table1", ref="A1:E5")

# Add a default style with striped rows and banded columns
style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                       showLastColumn=False, showRowStripes=True, showColumnStripes=True)
tab.tableStyleInfo = style

ws.add_table(tab)
wb.save("table.xlsx")

print(wb)