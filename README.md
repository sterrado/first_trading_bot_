<h1> Binance Trading Bot (Moving Averages) </h1>

Lo que hace este bot es consultar el indicador MA7 (el promedio del precio de los ultimos 7 dias) de Ethereum y compararlo con el valor de ayer. 
Si es positivo significa que la tendencia de los ultimos 7 dias es alcista, entonces compra Ethereum si es que hay USDT disponible. Si es negativo,
significa que la tendencia es bajista entonces vende Ethereum si es que hay disponibles y se queda con USDT. Cada vez que el bot realiza un trade
envia un mail y guarda el trade en una base de datos. Si algo falla, envia un mail con la información del error.

Para que funcione hay que configurar las API keys de Binance y las del Gmail en un file que se llame secrets.py y configurar bien la base de datos (Mongo DB)

El bot opera por default con Ethereum y con el MA7 pero se puede cambiar el valor del MA a cualquiera (por ejemplo MA15 seria el promedio de los ultimos 15 dias)
y cambiando el simbolo se puede operar cualquier otra moneda que este en Binance (ej: 'BTCUSDT')
