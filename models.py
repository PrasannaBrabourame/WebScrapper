import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, UniqueConstraint

Base = declarative_base()


class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)


class Cyclone(Base):
    __tablename__ = 'cyclone'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))


class TrackingInfo(Base):
    __tablename__ = 'trackinginfo'

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(Region)
    cyclone_id = Column(Integer, ForeignKey('cyclone.id'))
    cyclone = relationship(Cyclone)
    __table_args__ = (UniqueConstraint('region_id', 'created_date'),)

engine = create_engine('postgresql+psycopg2://postgres:integra@localhost:5432/postgres')

Base.metadata.create_all(engine)