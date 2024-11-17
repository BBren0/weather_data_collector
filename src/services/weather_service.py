import requests
from config import API_KEY, BASE_URL, cnx
from datetime import datetime

def convert_timestamp(timestamp):
    """Converte um timestamp Unix para datetime."""
    return datetime.fromtimestamp(timestamp)

def get_weather(cidade):
    url = f"{BASE_URL}?q={cidade}&APPID={API_KEY}&units=metric"
    print(f"Requisitando dados da API para: {cidade}")

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        weather_data = {
            "cidade": cidade,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temperature_min": data["main"]["temp_min"],
            "temperature_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "speed_wind": data["wind"]["speed"],
            "direct_wind": data["wind"]["deg"],
            "description": data["weather"][0]["description"],
            "sunrise": convert_timestamp(data["sys"]["sunrise"]),
            "sunset": convert_timestamp(data["sys"]["sunset"]),
            "timestamp": convert_timestamp(data["dt"])
        }
        
        insert_query = """INSERT INTO WeatherData (City, Temperature, FeelsLike, TemperatureMin, TemperatureMax, Humidity, SpeedWind, DirectWind, Description, Sunrise, Sunset, Timestamp)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (
            weather_data["cidade"], weather_data["temperature"], weather_data["feels_like"],
            weather_data["temperature_min"], weather_data["temperature_max"], weather_data["humidity"],
            weather_data["speed_wind"], weather_data["direct_wind"], weather_data["description"],
            weather_data["sunrise"], weather_data["sunset"], weather_data["timestamp"]
        )

        cursor = cnx.cursor()
        cursor.execute(insert_query, values)
        cnx.commit()
        cursor.close()

        return weather_data  # Retorna os dados para que `main.py` possa exibir
    else:
        print("Erro ao obter dados do clima:", response.status_code)
        return None
