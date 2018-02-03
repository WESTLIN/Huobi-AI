# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Huobi(Base):
    __tablename__ = 'huobi'

    id = Column(BigInteger, primary_key=True)
    symbol = Column(String(20), nullable=False)
    period = Column(String(10), nullable=False)
    amount = Column(Float(asdecimal=True), nullable=False)
    count = Column(Float(asdecimal=True), nullable=False)
    price_open = Column(Float(asdecimal=True), nullable=False)
    price_close = Column(Float(asdecimal=True), nullable=False)
    price_low = Column(Float(asdecimal=True), nullable=False)
    price_high = Column(Float(asdecimal=True), nullable=False)
    vol = Column(Float(asdecimal=True), nullable=False)
    price_avg = Column(Float(asdecimal=True), nullable=False)
    timestamp = Column(BigInteger, nullable=False)
