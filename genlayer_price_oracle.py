import requests

class GenLayerPriceOracle:
    """
    A 3rd-party integration toolkit for GenLayer Intelligent Contracts 
    to fetch real-time off-chain price data.
    """
    
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3/simple/price"

    def get_crypto_price(self, coin_id="bitcoin", currency="usd"):
        """
        Fetches the current price of a specific cryptocurrency.
        """
        try:
            params = {
                "ids": coin_id,
                "vs_currencies": currency
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            price = data.get(coin_id, {}).get(currency)
            if price:
                return {"status": "success", "asset": coin_id, "price": price, "currency": currency}
            else:
                return {"status": "error", "message": "Invalid coin ID or currency"}
                
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": str(e)}
 
