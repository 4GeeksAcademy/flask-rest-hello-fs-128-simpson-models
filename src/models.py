from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

favorites_character = Table(
    "favorites_character",
    db.Model.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("character_id",ForeignKey("character.id"), primary_key=True)
)

favorites_location = Table(
    "favorites_location",
    db.Model.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("location_id",ForeignKey("location.id"), primary_key=True)
)

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    favorites_character: Mapped[list["Character"]]= relationship(
        "Character",
        secondary= favorites_character,
        back_populates ="favorited_by"
    )
    favorites_location: Mapped[list["Location"]]= relationship(
        "Location",
        secondary= favorites_location,
        back_populates ="favorited_by"
    )


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            
        }
    def serialize_favorites(self):
        return {
            "favorites_character":[character.serialize()for character in self.favorites_character],
            "favorites_location":[location.serialize()for location in self.favorites_location],
        }
    

class Character(db.Model):
    __tablename__ ="character"

    id:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(100), unique=True, nullable=False)
    quote:Mapped[str]=mapped_column(String(200),nullable=False)
    img:Mapped[str]= mapped_column(String(500),nullable=False)
    favorited_by:Mapped[list["User"]]= relationship(
        "User",
        secondary= favorites_character,
        back_populates ="favorites_character"
    )

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "quote": self.quote,
            "img": self.img
        }
    

class Location (db.Model):
    __tablename__ ="location"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(120), unique=True, nullable=False)
    img:Mapped[str]=mapped_column(String(500), nullable=False)
    use:Mapped[str]=mapped_column(String(200), nullable=False)
    town:Mapped[str]=mapped_column(String(200), nullable=False)
    favorited_by: Mapped[list["User"]] = relationship(
        "User",
        secondary=favorites_location,
        back_populates="favorites_location"
    )

    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
            "use":self.use,
            "town":self.town,
            "img":self.img
        }
    

