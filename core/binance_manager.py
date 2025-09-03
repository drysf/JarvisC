from binance.client import Client
import os
from dotenv import load_dotenv

class BinanceManager:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('API_KEY')
        self.api_secret = os.getenv('SECRET_KEY')
        self.client = Client(self.api_key, self.api_secret)
    
    def test_connection(self):
        try:
            print(self.client)
            return True
        except Exception as e:
            print(f"Erreur de connexion: {e}")
            return False
    

if __name__ == "__main__":
    binance_manager = BinanceManager()
    binance_manager.test_connection()