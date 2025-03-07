import requests

class StockDataFetcher:
    def __init__(self):
        self.sources = [
            {"name": "alpha_vantage", "url": "https://www.alphavantage.co/query"},
            {"name": "fmp", "url": "https://financialmodelingprep.com/api/v3"}
        ]

    async def get_stock_data(self, symbol: str):
        """Try sources in order until successful response"""
        for source in self.sources:
            try:
                if source["name"] == "alpha_vantage":
                    params = {
                        "function": "OVERVIEW",
                        "symbol": symbol,
                        "apikey": os.getenv("ALPHA_VANTAGE_KEY")
                    }
                    response = requests.get(source["url"], params=params)
                    return self._parse_alpha_vantage(response.json())
                
                # Add other sources...
                
            except Exception as e:
                continue
        raise ValueError("All data sources failed")

    def _parse_alpha_vantage(self, data):
        return {
            "pe_ratio": float(data.get("PERatio")),
            "eps": float(data.get("EPS")),
            "market_cap": data.get("MarketCapitalization")
        }
