from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Result(Base):

    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String)
    file_data = Column(LargeBinary)
