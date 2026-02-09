from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
    
class Place (db.Model):
    __tablename__ ="planet"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(120), unique=True, nullable=False)
    climate:Mapped[str]=mapped_column(String(120), nullable=False)

    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
            "climate":self.climate
        }
    

class Character(db.Model):
    __tablename__ ="Character"

    id:Mapped[int]=mapped_column(primey_key=True)
    name: Mapped[str]=mapped_column(String(100), unique=True, nullable=False)
    gender:Mapped[str]=mapped_column(String(50),nullable=False)

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender
        }