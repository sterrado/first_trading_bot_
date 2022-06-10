import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

xlsx = pd.ExcelFile('backtest1.xlsx')
df = pd.read_excel(xlsx,  'Hoja1')
df = pd.DataFrame(df)

row_count = 0
eth_qty = 0
usdt = 3398


for row in df.index:
    row_count += 1
    if row_count < 160:
        continue
    else:
        MA30 = df['MA30'][row]
        price = df['Precio_eth'][row]
        tendency = MA30 > df['MA30'][row - 1]
        if tendency:
            if usdt > 10:
                eth_qty = usdt / price
                df['ETH'][row] = eth_qty
                usdt = 0
                # print('row_count: ' + str(row_count) + ' MA30: ' + str(MA30) + ' usdt: ' +
                #     str(usdt) + ' eth_qty: ' + str(eth_qty))
            else:
                continue
        else:
            if eth_qty * price > 10:
                usdt = eth_qty * price
                df['USDT'][row] = usdt
                eth_qty = 0
              #  print('row_count: ' + str(row_count) + ' usdt: ' +
               #       str(usdt) + ' eth_qty: ' + str(eth_qty))
            else:
                continue

df.to_excel('testing_MA7_sept.xlsx')
