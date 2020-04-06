import pandas as pd
import matplotlib.pyplot as plt

#plotting absoute return

df1 = pd.read_excel('btc.xlsx', sheet_name='Absolute Return')
df2 = pd.read_excel('bletchley_index.xlsx', sheet_name='Absolute Return')
df3 = pd.read_excel('Coinbase_index.xlsx', sheet_name='Absolute Return')
df4 = pd.read_excel('Amun_index.xlsx', sheet_name='Absolute Return')
df5 = pd.read_excel('bitx.xlsx', sheet_name='Absolute Return')
df6 = pd.read_excel('mvis.xlsx', sheet_name='Absolute Return')
df7 = pd.read_excel('SEBAX.xlsx', sheet_name='Absolute Return')
df8 = pd.read_excel('crix_index.xlsx', sheet_name='Absolute Return')


data1 = pd.DataFrame(df1, columns=['Date', 'ITD'])
data2 = pd.DataFrame(df2, columns=['Date', 'ITD'])
data3 = pd.DataFrame(df3, columns=['Date', "ITD"])
data4 = pd.DataFrame(df4, columns=['Date', "ITD"])
data5 = pd.DataFrame(df5, columns=['Date', "ITD"])
data6 = pd.DataFrame(df6, columns=['Date', "ITD"])
data7 = pd.DataFrame(df7, columns=['Date', "ITD"])
data8 = pd.DataFrame(df8, columns=['Date', "ITD"])

fig = plt.figure(figsize=(50, 35))

ax1 = fig.add_subplot(111, ylabel='Date')
data1['ITD'].plot(ax=ax1, color='black', lw=7.)
data2["ITD"].plot(ax=ax1, color='red', lw=7.)
data3["ITD"].plot(ax=ax1, color='green', lw=7.)
data4["ITD"].plot(ax=ax1, color='blue', lw=7.)
data5["ITD"].plot(ax=ax1, color='orange', lw=7.)
data6["ITD"].plot(ax=ax1, color='magenta', lw=7.)
data7["ITD"].plot(ax=ax1, color='brown', lw=7.)
data8["ITD"].plot(ax=ax1, color='cyan', lw=6.)

plt.savefig("performance since inception.png")


#plotting volatility

df1 = pd.read_excel('btc.xlsx', sheet_name='Volatility')
df2 = pd.read_excel('bletchley_index.xlsx', sheet_name='Volatility')
df3 = pd.read_excel('Coinbase_index.xlsx', sheet_name='Volatility')
df4 = pd.read_excel('Amun_index.xlsx', sheet_name='Volatility')
df5 = pd.read_excel('bitx.xlsx', sheet_name='Volatility')
df6 = pd.read_excel('mvis.xlsx', sheet_name='Volatility')
df7 = pd.read_excel('SEBAX.xlsx', sheet_name='Volatility')
df8 = pd.read_excel('crix_index.xlsx', sheet_name='Volatility')

data1 = pd.DataFrame(df1, columns=['Date', '3M'])
data2 = pd.DataFrame(df2, columns=['Date', '3M'])
data3 = pd.DataFrame(df3, columns=['Date', "3M"])
data4 = pd.DataFrame(df4, columns=['Date', "3M"])
data5 = pd.DataFrame(df5, columns=['Date', "3M"])
data6 = pd.DataFrame(df6, columns=['Date', "3M"])
data7 = pd.DataFrame(df7, columns=['Date', "3M"])
data8 = pd.DataFrame(df8, columns=['Date', "3M"])

fig = plt.figure(figsize=(50, 35))

ax1 = fig.add_subplot(111, ylabel='Date')
data1['3M'].plot(ax=ax1, color='black', lw=7.)
data2["3M"].plot(ax=ax1, color='red', lw=7.)
data3["3M"].plot(ax=ax1, color='green', lw=7.)
data4["3M"].plot(ax=ax1, color='blue', lw=7.)
data5["3M"].plot(ax=ax1, color='orange', lw=7.)
data6["3M"].plot(ax=ax1, color='magenta', lw=7.)
data7["3M"].plot(ax=ax1, color='brown', lw=7.)
data8["3M"].plot(ax=ax1, color='cyan', lw=6.)

plt.savefig("volatility.png")


#plotting maximum drawdown

df1 = pd.read_excel('btc.xlsx', sheet_name='Maximum drawdown')
df2 = pd.read_excel('bletchley_index.xlsx', sheet_name='Maximum drawdown')
df3 = pd.read_excel('Coinbase_index.xlsx', sheet_name='Maximum drawdown')
df4 = pd.read_excel('Amun_index.xlsx', sheet_name='Maximum drawdown')
df5 = pd.read_excel('bitx.xlsx', sheet_name='Maximum drawdown')
df6 = pd.read_excel('mvis.xlsx', sheet_name='Maximum drawdown')
df7 = pd.read_excel('SEBAX.xlsx', sheet_name='Maximum drawdown')
df8 = pd.read_excel('crix_index.xlsx', sheet_name='Maximum drawdown')


data1 = pd.DataFrame(df1, columns=['Date', 'ITD'])
data2 = pd.DataFrame(df2, columns=['Date', 'ITD'])
data3 = pd.DataFrame(df3, columns=['Date', "ITD"])
data4 = pd.DataFrame(df4, columns=['Date', "ITD"])
data5 = pd.DataFrame(df5, columns=['Date', "ITD"])
data6 = pd.DataFrame(df6, columns=['Date', "ITD"])
data7 = pd.DataFrame(df7, columns=['Date', "ITD"])
data8 = pd.DataFrame(df8, columns=['Date', "ITD"])

fig = plt.figure(figsize=(50, 35))

ax1 = fig.add_subplot(111, ylabel='Date')
data1['ITD'].plot(ax=ax1, color='black', lw=7.)
data2["ITD"].plot(ax=ax1, color='red', lw=7.)
data3["ITD"].plot(ax=ax1, color='green', lw=7.)
data4["ITD"].plot(ax=ax1, color='blue', lw=7.)
data5["ITD"].plot(ax=ax1, color='orange', lw=7.)
data6["ITD"].plot(ax=ax1, color='magenta', lw=7.)
data7["ITD"].plot(ax=ax1, color='brown', lw=7.)
data8["ITD"].plot(ax=ax1, color='cyan', lw=7.)

plt.savefig("max_drawdown.png")


#plotting drawdown

df1 = pd.read_excel('btc.xlsx', sheet_name='Drawdown')
df2 = pd.read_excel('bletchley_index.xlsx', sheet_name='Drawdown')
df3 = pd.read_excel('Coinbase_index.xlsx', sheet_name='Drawdown')
df4 = pd.read_excel('Amun_index.xlsx', sheet_name='Drawdown')
df5 = pd.read_excel('bitx.xlsx', sheet_name='Drawdown')
df6 = pd.read_excel('mvis.xlsx', sheet_name='Drawdown')
df7 = pd.read_excel('SEBAX.xlsx', sheet_name='Drawdown')
df8 = pd.read_excel('crix_index.xlsx', sheet_name='Drawdown')


data1 = pd.DataFrame(df1, columns=['Date', 'ITD'])
data2 = pd.DataFrame(df2, columns=['Date', 'ITD'])
data3 = pd.DataFrame(df3, columns=['Date', "ITD"])
data4 = pd.DataFrame(df4, columns=['Date', "ITD"])
data5 = pd.DataFrame(df5, columns=['Date', "ITD"])
data6 = pd.DataFrame(df6, columns=['Date', "ITD"])
data7 = pd.DataFrame(df7, columns=['Date', "ITD"])
data8 = pd.DataFrame(df8, columns=['Date', "ITD"])

fig = plt.figure(figsize=(50, 35))

ax1 = fig.add_subplot(111, ylabel='Date')
data1['ITD'].plot(ax=ax1, color='black', lw=7.)
data2["ITD"].plot(ax=ax1, color='red', lw=7.)
data3["ITD"].plot(ax=ax1, color='green', lw=7.)
data4["ITD"].plot(ax=ax1, color='blue', lw=7.)
data5["ITD"].plot(ax=ax1, color='orange', lw=7.)
data6["ITD"].plot(ax=ax1, color='magenta', lw=7.)
data7["ITD"].plot(ax=ax1, color='brown', lw=7.)
data8["ITD"].plot(ax=ax1, color='cyan', lw=7.)

plt.savefig("drawdown.png")
