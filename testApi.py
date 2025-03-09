from bitgetApi import BitgetApi

api = BitgetApi(
    apiKey = 'myApiKey',
    secretKey = 'mySecretKey',
    password = 'myPassword'
)

# -------------------------------------------------------------

print("Get server time")

result = api.getRequest(
    endpoint="/api/v2/public/time"
)

print(result)

# -------------------------------------------------------------

print("Get account info")

parameters = {
    "symbol": "SETHSUSDT", 
    "productType": "susdt-futures", 
    "marginCoin": "SUSDT"
}

result = api.getRequest(
    endpoint="/api/v2/mix/account/account",
    parameters=parameters
)

print(result)

# -------------------------------------------------------------

print("Place order")

parameters = {
    "symbol": "SETHSUSDT",
    "productType": "susdt-futures",
    "marginMode": "isolated",
    "marginCoin": "SUSDT",
    "size": "0.01",
    "price": "3000",
    "side": "buy",
    "tradeSide": "open",
    "orderType": "limit",
    "force": "gtc",
    "clientOid": "12121212122",
    "reduceOnly": "NO",
    "presetStopSurplusPrice": "3300",
    "presetStopLossPrice": "2300"
}

result = api.postRequest(
    endpoint="/api/v2/mix/order/place-order",
    parameters=parameters,
)

print(result)

# -------------------------------------------------------------