from app.model.profile import Profile as Profiles
from app import response, db
from flask import jsonify, request, session
from app.controller import UserController
from pprint import pprint
from flask_jwt_extended import *

@jwt_required() 
def index():
    try:
        if 'email' in session:
            id = request.args.get('user_id')
            profile = Profiles.query.filter_by(user_id=id).all()
            data = transform(profile)
            return response.ok(data, "")
        return 'You are not signed in!'
    except Exception as e:
        print(e)

 
def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array

@jwt_required() 
def show(id):
    try:
        if 'email' in session:
            profile = Profiles.query.filter_by(id=id).first()
            if not profile:
                return response.badRequest([], 'Empty....')

            data = singleTransform(profile)
            return response.ok(data, "")
        return 'You are not signed in!'
    except Exception as e:
        print(e)

def store():
    try:
        if 'email' in session:
            user_id = request.json['user_id']
            nama_lengkap = request.json['nama_lengkap']
            foto_profil = request.json['foto_profil']
            alamat = request.json['alamat']
            kategori = request.json['kategori']
            kategori_influencer = request.json['kategori_influencer']
            instagram = request.json['instagram']
            instagram_link = request.json['instagram_link']
            twitter = request.json['twitter']
            twitter_link = request.json['twitter_link']
            facebook = request.json['facebook']
            facebook_link = request.json['facebook_link']
            tiktok = request.json['tiktok']
            tiktok_link = request.json['tiktok_link']
            youtube = request.json['youtube']
            youtube_link = request.json['youtube_link']
            

            profile = Profiles(user_id=user_id, nama_lengkap=nama_lengkap, alamat=alamat, kategori=kategori, kategori_influencer=kategori_influencer, instagram=instagram, instagram_link=instagram_link, twitter=twitter, twitter_link=twitter_link, facebook=facebook, facebook_link=facebook_link, youtube=youtube, youtube_link=youtube_link, tiktok=tiktok, tiktok_link=tiktok_link, foto_profil=foto_profil)
            db.session.add(profile)
            db.session.commit()

            return response.ok('', 'Successfully create profile!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)
        return response.ok('', 'ERROR !')


@jwt_required() 
def update(id):
    try:
        if 'email' in session:
            nama_lengkap = request.json['nama_lengkap']
            alamat = request.json['alamat']
            kategori = request.json['kategori']
            kategori_influencer = request.json['kategori_influencer']
            foto_profil = request.json['foto_profil']
            instagram = request.json['instagram']
            instagram_link = request.json['instagram_link']
            twitter = request.json['twitter']
            twitter_link = request.json['twitter_link']
            facebook = request.json['facebook']
            facebook_link = request.json['facebook_link']
            youtube = request.json['facebook']
            youtube_link = request.json['youtube_link']

            profile = Profiles.query.filter_by(id=id).first()
            profile.nama_lengkap = nama_lengkap
            profile.alamat = alamat
            profile.kategori = kategori
            profile.kategori_influencer = kategori_influencer
            profile.foto_profil = foto_profil
            profile.instagram = instagram
            profile.instagram_link = instagram_link
            profile.twitter = twitter
            profile.twitter_link = twitter_link
            profile.facebook = facebook
            profile.facebook_link = facebook_link
            profile.youtube = youtube
            profile.youtube_link = youtube_link

            db.session.commit()

            return response.ok('', 'Successfully update profile!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)

@jwt_required() 
def delete(id):
    try:
        if 'email' in session:
            profile = Profiles.query.filter_by(id=id).first()
            if not profile:
                return response.badRequest([], 'Empty....')

            db.session.delete(profile)
            db.session.commit()

            return response.ok('', 'Successfully delete data!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)

 
def singleTransform(values):
    if values.instagram == 0:
        ig = False
    elif values.instagram == 1:
        ig = True
    if values.twitter == 0:
        tw = False
    elif values.twitter == 1:
        tw = True
    if values.facebook == 0:
        fb = False
    elif values.facebook == 1:
        fb = True
    if values.tiktok == 0:
        tt = False
    elif values.tiktok == 1:
        tt = True
    if values.youtube == 0:
        yt = False
    elif values.youtube == 1:
        yt = True
    #pprint(vars(values))
    data = {
        'id': values.id,
        'user_id': values.user_id,
        'nama_lengkap': values.nama_lengkap,
        'alamat': values.alamat,
        'kategori': values.kategori,
        'kategori_influencer': values.kategori_influencer,
        'foto_profil': values.foto_profil,
        'social_media': {
            'instagram' : ig,
            'instagram_link' : values.instagram_link,
            'twitter' : tw,
            'twitter_link' : values.twitter_link,
            'facebook' : fb,
            'facebook_link' : values.facebook_link,
            'tiktok' : tt,
            'tiktok_link' : values.tiktok_link,
            'youtube' : yt,
            'youtube_link' : values.youtube_link,
        },
        'users': UserController.singleTransform(values.users, withTodo=False)
    }

    return data