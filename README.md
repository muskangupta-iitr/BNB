**File name:**
*project.py*, *plot.py*, *daily_return.py*
project.py: used for computing values of different parameters and writing the, to excel <br>
plot.py: used for graphs plotting
daily_return.py: used for calculating daily returns
**Packages used:**
`Pandas`, `Numpy`, `Datetime`, `Dateutil`, `Stastics`, `Openpyxl`, `Matplot`

**Excel Files used:** <br>
*btc.xlsx*: BTC <br>
*bletchley_index.xlsx*: Bletchley Index <br>
*Coinbase_index.xlsx*: Coinbase index  <br>
*Amun_index.xlsx*: AMUN Index<br>
*bitx.xlsx*: BITX
*mvis.xlsx*: MVIS CC DA 10 Index  <br>
*SEBAX.xlsx*: SEBAX  <br>
*crix_index.xlsx*: CRIX Index <br>
\n
**Final Excel**: *Peer Analysis.xlsx*  <br>

 The code has to be run only after each excel has the data and index sorted from *newest to oldest*. Date in the report and the rest of the files must be in same format. 

**Parameters Calculated:**
For each parameter a seperate function hs been defined with each function calculating the parameter by passing the dataframe for which the calculation has to be done and the file name where it has to be stored.
## Absolute Return: 
Function: absolute_return passed with parameters dataframe and file_name <br>
Formula: price after time t/price today

## Annualised volatility:
Function: annualised_volatility passed with parameters dataframe and file_name <br>
Formula: (standard deviation of daily return data over t time)*(square root of t)

## Absolute Return by Drawdown:
Calculated in the function absolute_return passed with parameters dataframe and file_name  <br>
Formula: Absoulte Return/Drawdown

## Return by volatility:
Calculated in the function annualised_volatility passed with parameters dataframe and file_name <br>
Formula: Daily Return/volatility

## Drawdown:
Function: Drawdown passed with parameters dataframe and file_name  <br>
Formula: max(0, max(X(t)-x(T)) where t belongs from (0, T))

## Maximum Drawdown:
Calculated in the function in Drawdown passed with parameters dataframe and file_name <br>
Formula: Minimun of drawdown

## Correlation:
Calculated directly in the excel files and then copied to the final report <br>
Formula: Covariance(X,Y)/Std(X)*Std(Y) <br>

## Beta:
Calculated directly in the excel files and then copied to the final report <br>
Formula: Covariance(X,Y)/Var(X) <br>

A seperate function has been defined to write each parameter *(write_excel)* to its corresponding sheet and call each dataframe *(call_all_function)* .

**Window sizes:**
As per the requirement of report, each parameter has been calculated on a weekly basis, monthly basis, 3-month basis, annually, two-year basis, 3-year basis, year to date basis, and inception till date basis. <br>
Each window size has been definied in the function window_size passed with parameters of inception date and window type. 

