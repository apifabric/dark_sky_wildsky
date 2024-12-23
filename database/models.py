# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 23, 2024 22:30:52
# Database: sqlite:////tmp/tmp.yyLLRA05tc-01JFTT9D0GFXVNN4ME40T4VA00/dark_sky_wildsky/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class DarkSkyRegulation(SAFRSBaseX, Base):
    """
    description: Details regarding specific dark sky regulations.
    """
    __tablename__ = 'dark_sky_regulation'
    _s_collection_name = 'DarkSkyRegulation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    effective_date = Column(Date)
    expiration_date = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)



class EconomicBenefit(SAFRSBaseX, Base):
    """
    description: Records the economic benefits of implementing dark sky policies.
    """
    __tablename__ = 'economic_benefit'
    _s_collection_name = 'EconomicBenefit'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    benefit_description = Column(String)
    observation_date = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)



class EnvironmentalBenefit(SAFRSBaseX, Base):
    """
    description: Details on the environmental benefits of the dark sky program.
    """
    __tablename__ = 'environmental_benefit'
    _s_collection_name = 'EnvironmentalBenefit'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    benefit_description = Column(String)
    observation_date = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)



class Resource(SAFRSBaseX, Base):
    """
    description: Information regarding resources available for dark sky program.
    """
    __tablename__ = 'resource'
    _s_collection_name = 'Resource'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    type = Column(String)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
