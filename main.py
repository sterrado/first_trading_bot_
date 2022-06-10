# imports
from indicator import *
from time import sleep
from binance_apis import *
from bot_emails import send_email
import logging
import logging.handlers
from secrets import email_pass

smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.gmail.com", 587), credentials=('santiagoterrado@gmail.com', email_pass),
                                            fromaddr="santiagoterrado@gmail.com",
                                            toaddrs="santiagoterrado@gmail.com",
                                            subject="El bot arrojo una excepcion",
                                            secure=())


logger = logging.getLogger()
logger.addHandler(smtp_handler)


# Loop While True

while 2 > 1:
    try:
        print('Initializing...')
        tendency = analyze_tendency()
        print("Tendency:" + str(tendency))
        if (tendency == True):
            usdt_balance = get_usdt_balance()['free']
            usdt_balance = float(usdt_balance)
            if (float(usdt_balance) > 10):
                print("making market buy order")
                buy_market_order(usdt_balance)
                to = ['santiagoterrado@gmail.com']
                subject = 'El bot ejecuto una orden de compra'
                eth_price = float(get_eth_price())
                body = 'El bot ejecuto una orden de compra por ' + \
                    str(usdt_balance) + 'USDT. El precio de ETH es de ' + \
                    str(eth_price) + 'USDT'
                send_email(to, subject, body)
                print('going to sleep. USDT BALANCE: ' + str(usdt_balance))
                sleep(60*30)
            else:
                print('going to sleep. USDT BALANCE: ' + str(usdt_balance))
                sleep(60*30)
        else:
            eth_balance = get_eth_balance()['free']
            eth_balance = round(float(eth_balance), 4)
            eth_price = float(get_eth_price())
            eth_balance_usdt = eth_balance * eth_price
            eth_balance_usdt = float(eth_balance_usdt)
            if (float(eth_balance_usdt) > 10):
                print("making market sell order")
                sell_market_order(float(eth_balance))
                to = ['santiagoterrado@gmail.com']
                subject = 'El bot ejecuto una orden de venta'
                body = 'El bot ejecuto una orden de venta por ' + str(eth_balance) + 'ETH, o ' + \
                    str(eth_balance_usdt) + 'USDT. El precio de ETH es de ' + \
                    str(eth_price) + 'USDT'
                send_email(to, subject, body)
                print('going to sleep. USDT BALANCE in ETH: ' +
                      str(eth_balance_usdt))
                sleep(60*30)
            else:
                print('going to sleep. USDT BALANCE in ETH: ' +
                      str(eth_balance_usdt))
                sleep(60*30)
        print('going to sleep')
        sleep(60*30)
    except Exception as e:
        logger.exception('Unhandled Exception')
        raise Exception
