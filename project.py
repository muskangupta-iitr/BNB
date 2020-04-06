# Libraries and Packages used
import pandas as pd
import statistics
import datetime as dt
from dateutil import relativedelta
from openpyxl import load_workbook

# Storing the excel sheets into dataframes
df1 = pd.read_excel('btc.xlsx')
df2 = pd.read_excel('bletchley_index.xlsx')
df3 = pd.read_excel('Coinbase_index.xlsx')
df4 = pd.read_excel('Amun_index.xlsx')
df5 = pd.read_excel('bitx.xlsx')
df6 = pd.read_excel('mvis.xlsx')
df7 = pd.read_excel('SEBAX.xlsx')
df8 = pd.read_excel('crix_index.xlsx')

# Defining the window size for calculations
window_type = ['1W', '1M', '3M', '1Y', '2Y', '3Y', 'YTD', 'ITD']

# Calling different functions made for calculating different parameters
def call_all_function(dataframe, file_name):
    print('\n' + '\x1b[6;30;42m' +
          'Calulating drawdown and maximum drawdown....' + '\x1b[0m')
    drawdown_df = drawdown(dataframe, file_name)
    print('\n' + '\x1b[6;30;42m' +
          'Calulating absolute return....' + '\x1b[0m')
    absolute_return(dataframe, file_name, drawdown_df)
    print('\n' + '\x1b[6;30;42m' +
          'Calulating annualised volatitlity and return by volume....' + '\x1b[0m')
    annualised_volatility(dataframe, file_name)
    print('\n' + '\x1b[6;30;42m' + 'Calulating monthly return....' + '\x1b[0m')
    monthly_return(dataframe, file_name)

# Wrtiing each parameter to excel file of corresponding index
def write_excel(dataframe, file_name, dataframe_name):
    book = load_workbook(file_name)
    writer = pd.ExcelWriter(file_name, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    dataframe.to_excel(writer, dataframe_name)
    writer.save()


# Defining window size for passing into the rolling function
def window_size(date_inception, window_type):
    if isinstance(date_inception, str):
        date_inception = dt.datetime.strptime(date_inception, '%Y-%m-%d')
    use_date = ''
    if window_type == '1W':
        use_date = date_inception + relativedelta.relativedelta(weeks=+1)
    elif window_type == '1M':
        use_date = date_inception + relativedelta.relativedelta(months=+1)
    elif window_type == '3M':
        use_date = date_inception + relativedelta.relativedelta(months=+3)
    elif window_type == '1Y':
        use_date = date_inception + relativedelta.relativedelta(years=+1)
    elif window_type == '2Y':
        use_date = date_inception + relativedelta.relativedelta(years=+2)
    elif window_type == '3Y':
        use_date = date_inception + relativedelta.relativedelta(years=+3)
    elif window_type == 'YTD':
        use_date = date_inception + relativedelta.relativedelta(month=1, day=1)
    elif window_type == 'ITD':
        use_date = dt.datetime(2020, 2, 19) #change according to the current date
    return abs((use_date - date_inception).days)


def date_price(dataframe, date_input):
    date_list = dataframe.loc[dataframe['Date'] ==
                              date_input.strftime('%Y-%m-%d'), 'Price'].to_list()
    if len(date_list) > 0:
        return date_list[0]
    else:
        return ''

# Calculating absolute return and absolute return by drawdown
def absolute_return(dataframe, file_name, drawdown_df):
    abs_return = pd.DataFrame(index=dataframe.index)
    abs_return['Date'] = dataframe['Date']
    abs_return['Price'] = dataframe['Price']
    absreturn_by_drawdown = pd.DataFrame(index=dataframe.index)
    absreturn_by_drawdown['Date'] = dataframe['Date']
    absreturn_by_drawdown['Price'] = dataframe['Price']

    for i in window_type:
        abs_return[i] = absreturn_by_drawdown[i] = ""

    for index in range(0, len(dataframe['Date'])):
        use_date = ''
        date_inception = dataframe['Date'][index]

        if isinstance(dataframe['Date'][index], str):
            date_inception = dt.datetime.strptime(
                dataframe['Date'][index], '%Y-%m-%d')

        for i in window_type:
            if i == '1W':
                use_date = date_inception + \
                    relativedelta.relativedelta(weeks=+1)
            elif i == '1M':
                use_date = date_inception + \
                    relativedelta.relativedelta(months=+1)
            elif i == '3M':
                use_date = date_inception + \
                    relativedelta.relativedelta(months=+3)
            elif i == '1Y':
                use_date = date_inception + \
                    relativedelta.relativedelta(years=+1)
            elif i == '2Y':
                use_date = date_inception + \
                    relativedelta.relativedelta(years=+2)
            elif i == '3Y':
                use_date = date_inception + \
                    relativedelta.relativedelta(years=+3)
            elif i == 'YTD':
                use_date = date_inception + \
                    relativedelta.relativedelta(month=1, day=1)
            elif i == 'ITD':
                use_date = dt.datetime(2020, 2, 16)  #change according to the current date

            if use_date:
                use_dt_price = date_price(dataframe, use_date)
                dt_inception_price = date_price(dataframe, date_inception)
                if use_dt_price and dt_inception_price:
                    abs_return[i][index] = (
                        use_dt_price / dt_inception_price)-1

                    if drawdown_df[i][index]:
                        absreturn_by_drawdown[i][index] = abs_return[i][index] / \
                            drawdown_df[i][index]
            else:
                abs_return[i][index] = ''

    write_excel(abs_return, file_name, 'Absolute Return')
    write_excel(absreturn_by_drawdown, file_name,
                'Absolute Return by Drawdown')

# Calculating annualised voltality and return by volatility
def annualised_volatility(dataframe, file_name):
    volatility = pd.DataFrame(index=dataframe.index)
    volatility['Date'] = dataframe['Date']
    volatility['Price'] = dataframe['Price']
    ret_by_vol = pd.DataFrame(index=dataframe.index)
    ret_by_vol['Date'] = dataframe['Date']
    ret_by_vol['Price'] = dataframe['Price']
    daily_return = dataframe['daily return']

    for i in window_type:
        volatility[i] = ret_by_vol[i] = ""

    for index in range(0, len(dataframe['Date'])):
        for i in window_type:
            window_size_num = window_size(dataframe['Date'][index], i)

            if index - window_size_num > -1 and i != 'ITD' and i != 'YTD':
                volatility[i][index] = daily_return[index -
                                                    window_size_num:index].std()*(window_size_num**0.5)
                ret_by_vol[i][index] = daily_return[index]/daily_return[index -
                                                                        window_size_num:index].std()
            elif i == 'YTD' and len(daily_return[index - window_size_num:index]) > 1:
                volatility[i][index] = daily_return[index -
                                                    window_size_num:index].std()*(window_size_num**0.5)
                ret_by_vol[i][index] = daily_return[index]/daily_return[index -
                                                                        window_size_num:index].std()
            elif i == 'ITD' and len(daily_return[1:index+1]) > 1:
                volatility[i][index] = daily_return[1:index+1].std(
                )*(len(daily_return[1:index])**0.5)
                ret_by_vol[i][index] = daily_return[index] / \
                    daily_return[1:index+1].std()
            else:
                volatility[i][index] = ''

    write_excel(volatility, file_name, 'Volatility')
    write_excel(ret_by_vol, file_name, 'Return By Volatitlity')

# Calculating drawdown and maximum drawdown
def drawdown(dataframe, file_name):
    drawdown = pd.DataFrame(index=dataframe.index)
    drawdown['Date'] = dataframe['Date']
    drawdown['Price'] = dataframe['Price']
    max_drawdown = pd.DataFrame(index=dataframe.index)
    max_drawdown['Date'] = dataframe['Date']
    max_drawdown['Price'] = dataframe['Price']

    for i in window_type:
        drawdown[i] = max_drawdown[i] = ""

    for index in range(0, len(dataframe['Date'])):
        for i in window_type:
            window_size_num = window_size(dataframe['Date'][index], i)

            if index - window_size_num > -1 and i != 'ITD':
                drawdown[i][index] = (dataframe['Price'][index] / dataframe['Price'][index -
                                                                                     window_size_num:index].max()) - 1
            elif i == 'ITD':
                drawdown[i][index] = (
                    dataframe['Price'][index] / dataframe['Price'][0:index+1].max()) - 1
            else:
                drawdown[i][index] = ''

    for index in range(0, len(dataframe['Date'])):
        for i in window_type:
            window_size_num = window_size(dataframe['Date'][index], i)

            if index - window_size_num > -1 and i != 'ITD' and i != 'YTD':
                parsed_drawdown = [elem for elem in drawdown[i][index -
                                                                window_size_num:index] if elem != '']
                if len(parsed_drawdown) > 0:
                    max_drawdown[i][index] = min(parsed_drawdown)
            elif i == 'YTD':
                if index - window_size_num < 0:
                    new_index = 0
                else:
                    new_index = index - window_size_num
                parsed_drawdown = [elem for elem in drawdown[i]
                                   [new_index:index] if elem != '']

                if len(parsed_drawdown) > 0:
                    max_drawdown[i][index] = min(
                        parsed_drawdown)
            elif i == 'ITD':
                max_drawdown[i][index] = drawdown[i][0:index+1].min()
            else:
                max_drawdown[i][index] = ''

    write_excel(drawdown, file_name, 'Drawdown')
    write_excel(max_drawdown, file_name, 'Maximum drawdown')

    return(drawdown)

# Calculating monthly return
def monthly_return(dataframe, file_name):
    monthly_return = pd.DataFrame(index=dataframe.index)
    monthly_return['Months'] = ''
    monthly_return['Monthly_Return'] = ''

    if isinstance(dataframe['Date'][0], str):
        month_num = dt.datetime.strptime(
            dataframe['Date'][0], '%Y-%m-%d').month
    else:
        month_num = dataframe['Date'][0].month

    product_value = 1
    month_index = 0
    for i in range(0, len(dataframe['Date'])):
        parsed_date = dataframe['Date'][i]

        if isinstance(dataframe['Date'][0], str):
            parsed_date = dt.datetime.strptime(
                dataframe['Date'][i], '%Y-%m-%d')

        product_value *= (dataframe['daily return'][i] + 1)

        if month_num != parsed_date.month:
            monthly_return['Months'][month_index] = parsed_date.strftime(
                '%b %Y')
            monthly_return['Monthly_Return'][month_index] = product_value-1
            product_value = 1
            month_num = parsed_date.month
            month_index += 1

    write_excel(monthly_return, file_name, 'Monthly Return')

#Print what is being computed
print('\n' + '\x1b[6;30;42m' +
      'Calulating for BTC....' + '\x1b[0m')
call_all_function(df1, 'btc.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for Bletchley Index ....' + '\x1b[0m')
call_all_function(df2, 'bletchley_index.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for Coinbase index....' + '\x1b[0m')
call_all_function(df3, 'Coinbase_index.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for AMUN Index....' + '\x1b[0m')
call_all_function(df4, 'Amun_index.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for BITX....' + '\x1b[0m')
call_all_function(df5, 'bitx.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for MVIS CC DA 10 Index....' + '\x1b[0m')
call_all_function(df6, 'mvis.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for SEBAX....' + '\x1b[0m')
call_all_function(df7, 'SEBAX.xlsx')
print('\n' + '\x1b[6;30;42m' +
      'Calulating for CRIX Index....' + '\x1b[0m')
call_all_function(df8, 'crix_index.xlsx')
