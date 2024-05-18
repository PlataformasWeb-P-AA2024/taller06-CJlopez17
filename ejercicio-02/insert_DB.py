# imports necesario 
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_DB import Pais

# Conexion con la base  de datos
engine = create_engine('sqlite:///basePais.db')
Session = sessionmaker(bind=engine)
session = Session()

# URL del archivo JSON
url = "https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json"

# Realiza la solicitud HTTP para obtener los datos JSON
response = requests.get(url)
datos_json = response.json()

# Procesa los datos JSON
for d in datos_json:
    print(d)
    print(len(d.keys()))
    p = Pais(
        nombrePais=d.get('CLDR display name', 'N/A'),
        capital=d.get('Capital', 'N/A'),
        continente=d.get('Continent', 'N/A'),
        dial=d.get('Dial', 'N/A'),
        geoname=d.get('Geoname ID', 'N/A'),
        itu=d.get('ITU', 'N/A'),
        lenguaje=d.get('Languages', 'N/A'),
        independt=d.get('is_independent', 'N/A')
    )
    session.add(p)

# Confirmar transacciones
session.commit()