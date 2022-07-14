from app import db
from datetime import datetime
from app.model.user import Users


class Campaign(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_campaign= db.Column(db.String(230), nullable=False)
    status_campaign = db.Column(db.String(120), index=True, unique=True, nullable=False)
    type_campaign = db.Column(db.String(128), nullable=False)
    phase_campaign = db.Column(db.String(128), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    product_campaign = db.Column(db.String(128), nullable=False)
    tasks = db.Column(db.String(128), nullable=False)
    id_socmed = db.Column(db.String(128), nullable=False)
    publish_plan = db.Column(db.String(128), nullable=False)
    caption = db.Column(db.String(128), nullable=False)
    tag_people = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    users = db.relationship("Users", backref="user_id")

    #created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Campaign {}>'.format(self.user_id)