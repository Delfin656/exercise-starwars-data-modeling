import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(30), nullable=False)
    user_name = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    favorites = relationship("Favorites")


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(30), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    height = Column(String(30), nullable=False)
    favorites = relationship("Favorites")


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(30), nullable=False)
    terrain = Column(String(30), nullable=False)
    population = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    favorites = relationship("Favorites")


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    color = Column(String(30), nullable=False)
    length = Column(Integer, nullable=False)
    favorites = relationship("Favorites")


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
