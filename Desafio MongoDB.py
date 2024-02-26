from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import pymongo

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship('Cliente', back_populates='contas')

engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

cliente1 = Cliente(nome='Cliente 1')
conta1 = Conta(numero='123', saldo=1000, cliente=cliente1)

session.add(cliente1)
session.commit()

client = pymongo.MongoClient("65dd0b93520f013f22f385b7")
db = client['banco_nosql']

collection = db['bank']

documento_cliente1 = {
    'nome': 'Cliente 1',
    'contas': [
        {'numero': '123', 'saldo': 1000},
    ]
}

collection.insert_one(documento_cliente1)

cliente_recuperado = collection.find_one({'nome': 'Cliente 1'})

contas_cliente1 = cliente_recuperado['contas']

clientes_com_saldo_maior_que_500 = collection.find({'contas.saldo': {'$gt': 500}})
