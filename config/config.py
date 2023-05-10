import os
from dotenv import load_dotenv
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'mysql+pymysql://root:0552588647@localhost:3306/fastapi'
engine = create_engine(DATABASE_URL,echo=True)
meta = MetaData()
conn = engine.connect()   
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'tb_users_'
    id= Column(Integer, primary_key=True)
    firstname= Column("firstname", String(50))
    lastname= Column("lastname", String(50))
    mail= Column("mail", String(50))

Base.metadata.create_all(bind=engine)
