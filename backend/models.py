from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)  # expert / entreprise
    category = Column(String)  # finance, agriculture...
    verified = Column(Integer, default=0)  # 0=non,1=oui
    balance = Column(Float, default=0.0)

class Contribution(Base):
    __tablename__ = "contributions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)  # CSV, report, annotation
    category = Column(String)
    file_path = Column(String)
    status = Column(String, default="pending")  # pending, approved, rejected
    quality_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User") Models)