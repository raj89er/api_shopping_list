
from . import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    date_added = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.save()
    
    def __repr__(self) -> str:
        return f"<Ingredient {self.ingredient_id} | {self.ingredient}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, **kwargs):
        for field, value in kwargs.items():
            if field in { 'ingredient', 'description', 'status' }:
                setattr(self, field, value)
        self.save()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            'ingredient_id': self.ingredient_id,
            'ingredient': self.ingredient,
            'description': self.description,
            'status': self.status,
            'date_added': self.date_added
        }



class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    name_first = db.Column(db.String, nullable=False)
    name_last = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_password(kwargs.get('password', ''))
    
    def __repr__(self):
        return f"<User {self.user_id} | {self.username}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def set_password(self, plaintext_password):
        self.password = generate_password_hash(plaintext_password)
        self.save()
    
    def check_password(self, plaintext_password):
        return check_password_hash(self.password, plaintext_password)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'name_first': self.name_first,
            'name_last': self.name_last,
            'email': self.email,
            'date_added': self.date_added
        }

