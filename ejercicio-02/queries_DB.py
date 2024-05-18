# Imports necesario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and y or


# se importa la clase(s) del
# archivo genera_tablas
from create_DB import Pais
from create_DB import engine

# Crea una sesión vinculada al motor de la base de datos,
Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de la entidad Pais
docentes = session.query(Pais).all()

# Consultas 
# Todos los países del continente americano
consulta_uno = session.query(Pais).filter(Pais.continente.in_(['SA', 'NA'])).order_by(Pais.nombrePais).all()
print(consulta_uno)

print('-----------------------------------------------')

# Países de Asía, ordenados por el atributo Dial.
consulta_dos = session.query(Pais).filter(Pais.continente == 'AS').order_by(Pais.dial).all()
print(consulta_dos)

print('-----------------------------------------------')

# Lenguajes de cada país.
consulta_tres = session.query(Pais).order_by(Pais.lenguaje).all()
print(consulta_tres)

print('-----------------------------------------------')

# Los países ordenados por la capital, siempre que el país pertenezca a Europa
consulta_cuatro = session.query(Pais).filter(Pais.continente == "EU").order_by(Pais.capital).all()
print(consulta_cuatro)

print('-----------------------------------------------')

# Todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
consulta_cinco = session.query(Pais).filter(or_(Pais.nombrePais.like('%uador%'),Pais.capital.like('%ito%'))).all()
# print(consulta_cinco)

for pais in consulta_cinco:
    print(f"Nombre: {pais.nombrePais}, Capital: {pais.capital}")

