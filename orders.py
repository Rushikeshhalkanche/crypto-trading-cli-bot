import logging
from bot.client import get_client

logger = logging.getLogger()


def place_order(symbol, side, order_type, quantity, price=None):

    client = get_client()

    try:

        logger.info(f"Placing order {symbol} {side} {order_type}")

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        else:

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order response: {order}")

        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise