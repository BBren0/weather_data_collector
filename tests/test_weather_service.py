import unittest
from src.services.weather_service import get_weather

class TestWeatherService(unittest.TestCase):

    def test_get_weather(self):
        # Teste para verificar se a função retorna um dicionário com temperatura e descrição
        result = get_weather("São Paulo")
        self.assertIn("temperature", result)
        self.assertIn("description", result)

if __name__ == "__main__":
    unittest.main()
