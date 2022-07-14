from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(230), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    roles = db.Column(db.String(128), nullable=False)
    no_telp = db.Column(db.String(128), nullable=False)
    user_id_telegram = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    campaigns = db.relationship("Campaign", lazy='select', backref=db.backref('campaigns', lazy='joined'))
    profiles = db.relationship("Profile", lazy='select', backref=db.backref('profiles', lazy='joined'))

    

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)