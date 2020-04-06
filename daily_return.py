# Libraries and Packages used
import pandas as pd
from pandas import ExcelWriter
import datetime as dt
from pandas import read_excel
from dateutil import relativedelta



# Storing the excel sheets into dataframes
df1 = pd.read_excel('btc.xlsx')
df2 = pd.read_excel('bletchley_index.xlsx')
df3 = pd.read_excel('Coinbase_index.xlsx')
df4 = pd.read_excel('Amun_index.xlsx')
df5 = pd.read_excel('bitx.xlsx')
df6 = pd.read_excel('mvis.xlsx')
df7 = pd.read_excel('SEBAX.xlsx')
df8 = pd.read_excel('crix_index.xlsx')


def calculate_daily_return(dataframe, name):
    for i in range(1, len(dataframe['Date'])):
        dataframe['% Change'][i] = (
            dataframe['Price'][i] - dataframe['Price'][i-1])*100/dataframe['Price'][i-1]
        dataframe['daily return'][i] = dataframe['% Change'][i]/100

    with ExcelWriter(name) as writer:
        dataframe.to_excel(writer)


print('\n' + '\x1b[6;30;42m' +
      'Calulating for BTC....' + '\x1b[0m')
calculate_daily_return(df1, 'btc.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for Bletchley Index ....' + '\x1b[0m')
calculate_daily_return(df2, 'bletchley_index.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for Coinbase index....' + '\x1b[0m')
calculate_daily_return(df3, 'Coinbase_index.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for AMUN Index....' + '\x1b[0m')
calculate_daily_return(df4, 'Amun_index.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for BITX....' + '\x1b[0m')
calculate_daily_return(df5, 'bitx.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for MVIS CC DA 10 Index....' + '\x1b[0m')
calculate_daily_return(df6, 'mvis.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for SEBAX....' + '\x1b[0m')
calculate_daily_return(df7, 'SEBAX.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for CRIX Index....' + '\x1b[0m')
calculate_daily_return(df8, 'crix_index.xlsx')
