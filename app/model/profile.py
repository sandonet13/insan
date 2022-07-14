from app import db
from datetime import datetime
from app.model.user import Users


class Profile(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_lengkap= db.Column(db.String(230), nullable=False)
    alamat = db.Column(db.String(120), index=True, unique=True, nullable=False)
    kategori = db.Column(db.String(128), nullable=False)
    kategori_influencer = db.Column(db.String(128), nullable=False)
    foto_profil = db.Column(db.String(128), nullable=False)
    instagram = db.Column(db.String(128), nullable=False)
    twitter = db.Column(db.String(128), nullable=False)
    facebook = db.Column(db.String(128), nullable=False)
    tiktok = db.Column(db.String(128), nullable=False)
    youtube = db.Column(db.String(128), nullable=False)
    instagram_link = db.Column(db.String(128), nullable=False)
    twitter_link = db.Column(db.String(128), nullable=False)
    facebook_link = db.Column(db.String(128), nullable=False)
    tiktok_link = db.Column(db.String(128), nullable=False)
    youtube_link = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    users = db.relationship("Users", backref="profile")
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Profile {}>'.format(self.user_id)