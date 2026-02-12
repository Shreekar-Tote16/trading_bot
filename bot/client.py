# # from binance.client import Client
# # from dotenv import load_dotenv
# # import os
# # import logging

# # logger = logging.getLogger(__name__)

# # class BinanceFuturesClient:
# #     def __init__(self):
# #         load_dotenv()

# #         api_key = os.getenv("BINANCE_API_KEY")
# #         api_secret = os.getenv("BINANCE_SECRET_KEY")

# #         if not api_key or not api_secret:
# #             raise ValueError("API credentials not found in environment.")

# #         self.client = Client(api_key, api_secret)

# #         # Demo Futures endpoint
# #         self.client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"

# #         # 🔥 Sync time with Binance server
# #         self.client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"
# #         self.client.API_URL = "https://demo-fapi.binance.com/api"

# #         # Adjust timestamp offset automatically
# #         self.client = Client(api_key, api_secret)
# #         self.client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"
# #         self.client.ping()
# #         self.client.futures_time()

# from binance.client import Client
# from dotenv import load_dotenv
# import os
# import logging
# import time

# logger = logging.getLogger(__name__)

# class BinanceFuturesClient:
#     def __init__(self):
#         load_dotenv()

#         api_key = os.getenv("BINANCE_API_KEY")
#         api_secret = os.getenv("BINANCE_SECRET_KEY")

#         if not api_key or not api_secret:
#             raise ValueError("API credentials not found in environment.")

#         self.client = Client(api_key, api_secret)

#         # Demo Futures endpoint
#         self.client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"

#         # 🔥 Proper timestamp sync
#         server_time = self.client.futures_time()["serverTime"]
#         local_time = int(time.time() * 1000)
#         self.client.timestamp_offset = server_time - local_time

#         logger.info("Binance Futures DEMO client initialized.")

#         try:
#             logger.info(f"Placing order: {kwargs}")
#             response = self.client.futures_create_order(**kwargs)
#             logger.info(f"Order response: {response}")
#             return response
#         except Exception as e:
#             logger.error(f"API Error: {str(e)}", exc_info=True)
#             raise



from binance.client import Client
from dotenv import load_dotenv
import os
import logging
import time

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        if not api_key or not api_secret:
            raise ValueError("API credentials not found in environment.")

        self.client = Client(api_key, api_secret)

        # Demo Futures endpoint
        self.client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"

        # Proper timestamp sync
        server_time = self.client.futures_time()["serverTime"]
        local_time = int(time.time() * 1000)
        self.client.timestamp_offset = server_time - local_time

        logger.info("Binance Futures DEMO client initialized.")

    def place_order(self, **kwargs):
        try:
            logger.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(f"API Error: {str(e)}", exc_info=True)
            raise
