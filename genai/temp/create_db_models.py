# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class DarkSkyRegulation(Base):
    """description: Details regarding specific dark sky regulations."""
    __tablename__ = 'dark_sky_regulation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    effective_date = Column(Date)
    expiration_date = Column(Date)


class Resource(Base):
    """description: Information regarding resources available for dark sky program."""
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    url = Column(String)
    type = Column(String)
    description = Column(String)


class EnvironmentalBenefit(Base):
    """description: Details on the environmental benefits of the dark sky program."""
    __tablename__ = 'environmental_benefit'

    id = Column(Integer, primary_key=True, autoincrement=True)
    benefit_description = Column(String)
    observation_date = Column(Date)


class EconomicBenefit(Base):
    """description: Records the economic benefits of implementing dark sky policies."""
    __tablename__ = 'economic_benefit'

    id = Column(Integer, primary_key=True, autoincrement=True)
    benefit_description = Column(String)
    observation_date = Column(Date)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    reg1 = DarkSkyRegulation(id=1, name='Protect Night Sky', description='Regulate light pollution.', effective_date=date(2023, 1, 15), expiration_date=date(2030, 12, 31))
    resource1 = Resource(id=1, name='Sky Protection Guide', url='http://example.com/guide', type='Guide', description='Guide on how to minimize light pollution.')
    env_ben1 = EnvironmentalBenefit(id=1, benefit_description='Improved star visibility', observation_date=date(2023, 6, 1))
    econ_ben1 = EconomicBenefit(id=1, benefit_description='Reduced energy consumption', observation_date=date(2023, 6, 1))
    
    
    
    session.add_all([reg1, resource1, env_ben1, econ_ben1])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
