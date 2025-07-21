from sqlalchemy import (Column, Integer, String, Float, DateTime, CheckConstraint, PrimaryKeyConstraint, Index)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='id_pk'),
        CheckConstraint('amount BETWEEN 10 AND 2500',name='amount_between_10_and_2500'),
        Index('index_name', 'category')
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"<Expense(category={self.category}, amount={self.amount})>"





