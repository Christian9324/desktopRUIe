from sqlalchemy import create_engine, Column, Integer, String, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///res/ruie_sqlite.db', echo=True)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    idUser = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String)
    nombre = Column(String)
    apellido = Column(String)
    password = Column(String)
    estado = Column(String)
    tipo = Column(String)

class Fuerza(Base):
    __tablename__ = 'fuerza'
    idFuerza = Column(Integer, primary_key=True, autoincrement=True)
    oficinaR = Column(String)
    numPunto = Column(Integer)
    nomPuntoRevision = Column(String)
    tipoP = Column(String)
    ubicacion = Column(String)
    coordenadasTexto = Column(String)
    latitud = Column(FLOAT)
    longitud = Column(FLOAT)
    personalINM = Column(Integer)
    personalSEDENA = Column(Integer)
    personalMarina = Column(Integer)
    personalGuardiaN = Column(Integer)
    personalOTROS = Column(Integer)
    vehiculos = Column(Integer)
    seccion = Column(Integer)

class Municipio(Base):
    __tablename__ = 'municipio'
    idMunicipio = Column(Integer, primary_key=True, autoincrement=True)
    estado= Column(String)
    estadoAbr= Column(String)
    nomMunicipio= Column(String)

class Pais(Base):
    __tablename__ = 'pais'
    idPais = Column(Integer, primary_key=True, autoincrement=True)
    nombre_pais = Column(String)
    iso3 = Column(String)

class PuntosInter(Base):
    __tablename__ = 'puntosInter'
    idPuntosI = Column(Integer, primary_key=True, autoincrement=True)
    nombrePunto= Column(String)
    estadoPunto= Column(String)
    tipoPunto= Column(String)


Base.metadata.create_all(engine)