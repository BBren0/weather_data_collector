import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Configurações do MySQL
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

# Conexão com o MySQL
try:
    cnx = mysql.connector.connect(
        user=SQL_USERNAME,
        password=SQL_PASSWORD,
        host=SQL_SERVER,
        database=SQL_DATABASE,
        ssl_disabled=False  # Configure conforme necessário
    )
    print("Conexão estabelecida com o MySQL.")
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
