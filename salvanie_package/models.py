from salvanie_package import db, login_manager
from salvanie_package import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(player_id):
    return Player.query.get(int(player_id))

class Player(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    characters = db.relationship('Character', backref='owned_player', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Character(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    ancestry = db.Column(db.Integer(), db.ForeignKey('ancestry.id'))
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('player.id'))
    items = db.relationship('Item', backref='owned_character', lazy=True)
    def __repr__(self):
        return f'Item {self.name}'
    
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=1024))
    owner = db.Column(db.Integer(), db.ForeignKey('character.id'))
    
class Skill(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    gives_hp = db.Column(db.Boolean(), nullable=False)
    def __repr__(self):
        return f'Item {self.name}'

class Ancestry(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=20), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    hp = db.Column(db.Integer(), nullable=False)
    def __repr__(self):
        return f'Item {self.name}'
    
class SkillCharacterRelationship(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    character = db.Column(db.Integer(), db.ForeignKey('character.id'))
    skill = db.Column(db.Integer(), db.ForeignKey('skill.id'))