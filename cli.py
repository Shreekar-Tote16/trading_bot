import argparse
import logging
from bot.orders import create_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n--- Order Request Summary ---")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if order_type == "LIMIT":
            print(f"Price: {price}")

        result = create_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n--- Order Response ---")
        print(f"Order ID: {result['orderId']}")
        print(f"Status: {result['status']}")
        print(f"Executed Quantity: {result['executedQty']}")
        avg_price = result.get("avgPrice") or "N/A"
        print(f"Average Price: {avg_price}")

        print("\nOrder placed successfully.")

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        print(f"\nOrder failed: {str(e)}")

if __name__ == "__main__":
    main()
