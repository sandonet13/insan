from app.model.user import Users
from app.model.jwt import TokenBlocklist as Jwts
from app import response, app, db
from flask import request, session
from pprint import pprint
from flask_jwt_extended import *
from flask_sqlalchemy import SQLAlchemy
jwt = JWTManager(app)
import datetime



@jwt_required() 
def index():
    try:
        if 'email' in session:
            users = Users.query.all()
            data = transform(users)
            return response.ok(data, "")
        return 'You are not signed in!'
    except Exception as e:
        print(e)


def transform(users):
    array = []
    for i in users:
        array.append(singleTransform(i))
    return array

@jwt_required() 
def show(id):
    try:
        if 'email' in session:
            users = Users.query.filter_by(id=id).first()
            if not users:
                return response.badRequest([], 'No Data')

            data = singleTransform(users)
            return response.ok(data, "")
        return 'You are not signed in!'
    except Exception as e:
        print(e)

def singleTransform(users, withTodo=True):
    data = {
        'id': users.id,
        'username': users.username,
        'email': users.email,
        'roles' : users.roles,
        'no_telp' : users.no_telp,
        'user_id_telegram' : users.user_id_telegram,
    }

    if withTodo:
        campaigns = []
        profiles = []
        #pprint(vars(users.campaigns))
        for i in users.campaigns:
            campaigns.append({
                'id': i.id,
                'nama_campaign': i.nama_campaign,
                'status_campaign': i.status_campaign,
                'type_campaign': i.type_campaign,
                'phase_campaign': i.phase_campaign,
                'start_date': i.start_date,
                'end_date' : i.end_date,
                'product_campaign' : i.product_campaign,
                'tasks' : i.tasks,
                'id_socmed' : i.id_socmed,
                'publish_plan' : i.publish_plan,
                'caption' : i.caption,
                'tag_people' : i.tag_people,              
            })
        data['campaigns'] = campaigns
        
        for x in users.profiles:
            profiles.append({
                'id': x.id,
                'user_id': x.user_id,
                'nama_lengkap': x.nama_lengkap,
                'alamat': x.alamat,
                'kategori': x.kategori,
                'kategori_influencer': x.kategori_influencer,
                'foto_profil': x.foto_profil,
                'social_media': {
                    # 'instagram' : ig,
                    'instagram_link' : x.instagram_link,
                    # 'twitter' : tw,
                    'twitter_link' : x.twitter_link,
                    # 'facebook' : fb,
                    'facebook_link' : x.facebook_link,
                    # 'tiktok' : tt,
                    'tiktok_link' : x.tiktok_link,
                    # 'youtube' : yt,
                    'youtube_link' : x.youtube_link,              
            }})
        data['profiles'] = profiles

    return data


def store():
    try:
        if 'email' in session:
            username = request.json['username']
            roles = request.json['roles']
            email = request.json['email']
            no_telp = request.json['no_telp']
            user_id_telegram = request.json['user_id_telegram']
            password = request.json['password']

            users = Users(username=username, email=email, roles=roles, no_telp=no_telp, user_id_telegram=user_id_telegram)
            users.setPassword(password)
            db.session.add(users)
            db.session.commit()

            return response.ok('', 'Successfully create data!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)
        return response.ok('', 'Please, fill the data !')

@jwt_required() 
def update(id):
    try:
        if 'email' in session:
            username = request.json['username']
            roles = request.json['roles']
            email = request.json['email']
            no_telp = request.json['no_telp']
            user_id_telegram = request.json['user_id_telegram']
            password = request.json['password']

            user = Users.query.filter_by(id=id).first()
            user.email = email
            user.username = username
            user.roles = roles
            user.no_telp = no_telp
            user.user_id_telegram = user_id_telegram
            user.setPassword(password)

            db.session.commit()

            return response.ok('', 'Successfully update data!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)

def setPassword(self, password):
    self.password = generate_password_hash(password)

@jwt_required() 
def delete(id):
    try:
        if 'email' in session:
            user = Users.query.filter_by(id=id).first()
            if not user:
                return response.badRequest([], 'Empty....')

            db.session.delete(user)
            db.session.commit()

            return response.ok('', 'Successfully delete data!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)

def login():
    try:
        email = request.json['email']
        password = request.json['password']
        session['email'] = email

        user = Users.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Empty....')

        if not user.checkPassword(password):
            return response.badRequest([], 'Your credentials is invalid')

        data = singleTransform(user, withTodo=False)
        expires = datetime.timedelta(days=1)
        expires_refresh = datetime.timedelta(days=3)
        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        return response.ok({
                "data": data,
                "token_access": access_token,
                "refresh_token": refresh_token,
            }, "You are logged in successfully")
    except Exception as e:
        #return response.serverError([], 'Internal Server Error 500')
        print(e)

def checkPassword(self, password):
    return check_password_hash(self.password, password)


# @jwt.token_in_blocklist_loader
# def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
#     jti = jwt_payload["jti"]
#     token = db.session.query(Jwts.id).filter_by(jti=jti).scalar()

#     return token is not None

@jwt_required()
def modify_token():
    try:
        jti = get_jwt()["jti"]
        now = datetime.datetime.now()
        jwts = Jwts(jti=jti, created_at=now)
        db.session.add(jwts)
        db.session.commit()
        return response.ok('', 'Revoke Token JWT Succesfully!')

    except Exception as e:
        print(e)

@jwt_required()
def protected():
    try:
        return response.ok('', 'hello world!')

    except Exception as e:
        print(e)

@jwt_required()
def sign_out():
    try:
        session.pop('email')
        return 'Signout Succesfully!'
    except Exception as e:
        return 'You need to login first!'