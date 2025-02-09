import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(50))
    password = Column(String(16), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    body = Column(String(2500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship('Planets')


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    director = Column(String(150), nullable=False)
    year = Column(Integer)


class CharactersFilms(Base):
    __tablename__ = 'characters_films'
    id = Column(Integer, primary_key=True)
    minutes = Column(Integer)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    film_id = Column(Integer, ForeignKey('films.id'))
    character = relationship('Characters', foreign_keys=['characters_id'])
    films = relationship('Films', foreign_keys=['film_id'])


class FavoritePlanets(Base):
    __tablename__  = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets', foreign_keys=['planet_id'])
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('Users', foreign_keys=['user_id'])


class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('Users', foreign_keys=['user_id'])
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Characters', foreign_keys=['character_id'])

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
