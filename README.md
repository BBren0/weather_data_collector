# Weather Data Collector

Este projeto é uma aplicação Python que coleta dados meteorológicos da API OpenWeatherMap e armazena as informações em um banco de dados MySQL hospedado na Azure. A aplicação é projetada para executar continuamente, atualizando os dados a cada 5 minutos.

---

## Funcionalidades

- Consulta dados meteorológicos de uma cidade específica, incluindo:
  - Temperatura atual, sensação térmica, temperatura mínima e máxima.
  - Umidade, velocidade e direção do vento.
  - Horário do nascer e pôr do sol.
  - Descrição geral do clima.
- Armazena os dados coletados em um banco de dados MySQL para análises posteriores.
- Executa em loop contínuo, atualizando os dados periodicamente.

---

## Pré-requisitos

Certifique-se de ter as ferramentas e dependências a seguir instaladas:

1. **Python 3.8+**
2. **Bibliotecas Python**:
   - `requests`
   - `pymysql`
   - `python-dotenv`
3. **Banco de Dados MySQL** configurado e acessível.
4. **Conta na OpenWeatherMap** para obter uma chave de API.

--
## Estrutura do Projeto

weather-data-collector/

|─ src/

|   ├── main.py                # Entrada principal da aplicação

│   ├── services/

│   │   └── weather_service.py # Lógica de integração com a API e banco de dados

│   ├── config.py              # Configuração do banco de dados e API

├── .env                       # Variáveis de ambiente (não incluído no repositório)

├── example.env                # Exemplo de configuração do arquivo .env

├── requirements.txt           # Dependências do projeto

└── README.md                  # Documentação do projeto

--
## PowerBI
Com os dados armazenados em um banco MySQL instanciado na Azure, analisei os dados utilizando o Power BI, conectando-o via DirectQuery ao banco de dados.  
Com isso pude extrair os seguintes dados:
- Comparações de temperatura entre diferentes horários do dia.
- Tendências de mudanças climáticas ao longo do tempo.
- Horário do nascer e pôr do sol do dia atual
- Comparativo de humidade por cada status climático
![image](https://github.com/user-attachments/assets/eceff7bd-f504-4f11-87e3-e292f53834fd)

Saiba mais em: https://app.powerbi.com/groups/me/reports/394bf5f6-ca1d-48cf-910c-9d4b46d12927?ctid=17e73935-5784-4ce5-ab45-e190aac66a92&pbi_source=linkShare



Contato
- Autor: Breno Gabriel
- E-mail: breno430@outlook.com
- LinkedIn: https://www.linkedin.com/in/breno-gabriel-44a564229/
