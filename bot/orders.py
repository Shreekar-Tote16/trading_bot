import logging
from bot.client import BinanceFuturesClient

logger = logging.getLogger(__name__)

def create_order(symbol, side, order_type, quantity, price=None):
    client = BinanceFuturesClient()

    order_params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        order_params.update({
            "price": price,
            "timeInForce": "GTC"
        })

    response = client.place_order(**order_params)

    return {
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice"),
        "raw": response
    }
