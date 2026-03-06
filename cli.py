import typer
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logging

setup_logging()

app = typer.Typer()


@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):

    try:

        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price)

        if order_type == "LIMIT" and price is None:
            raise ValueError("Price required for LIMIT order")

        print("\nOrder Request Summary")
        print("---------------------")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")

        order = place_order(symbol, side, order_type, quantity, price)

        print("\nOrder Response")
        print("--------------")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")

        print("\n✅ Order placed successfully")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    app()