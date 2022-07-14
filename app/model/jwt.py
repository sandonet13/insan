from app import db
from datetime import datetime


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return '<JWT {}>'.format(self.id)