from services.weather_service import get_weather
import time

def main():
    cidade = input("Digite o nome da cidade: ")
    while True:
        weather_data = get_weather(cidade)
        if weather_data:
            print(f"Temperatura em {cidade}: {weather_data['temperature']}°C")
            print(f"Condições climáticas: {weather_data['description']}")
        else:
            print("Não foi possível obter dados da API.")
        
        print("Aguardando 15 minutos para a próxima atualização...")
        time.sleep(900)  # Pausa por 300 segundos (5 minutos)

if __name__ == "__main__":
    main()
