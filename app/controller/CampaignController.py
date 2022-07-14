from app.model.campaign import Campaign as Campaigns
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
            campaign = Campaigns.query.filter_by(user_id=id).all()
            data = transform(campaign)
            return response.ok(data, "")
        return 'You are not signed in!'
    except Exception as e:
        print(e)


def store():
    try:
        if 'email' in session:
            user_id = request.json['user_id']
            nama_campaign = request.json['nama_campaign']
            status_campaign = request.json['status_campaign']
            type_campaign = request.json['type_campaign']
            phase_campaign = request.json['phase_campaign']
            start_date = request.json['start_date']
            end_date = request.json['end_date']
            product_campaign = request.json['product_campaign']
            tasks = request.json['tasks']
            id_socmed = request.json['id_socmed']
            publish_plan = request.json['publish_plan']
            caption = request.json['caption']
            tag_people = request.json['tag_people']
            

            campaign = Campaigns(user_id=user_id, nama_campaign=nama_campaign, status_campaign=status_campaign, type_campaign=type_campaign, phase_campaign=phase_campaign, start_date=start_date, end_date=end_date, product_campaign=product_campaign, tasks=tasks, id_socmed=id_socmed, publish_plan=publish_plan, caption=caption, tag_people=tag_people)
            db.session.add(campaign)
            db.session.commit()

            return response.ok('', 'Successfully create campaign!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)
        return response.ok('', 'ERROR !')

@jwt_required() 
def update(id):
    try:
        if 'email' in session:
            nama_campaign = request.json['nama_campaign']
            status_campaign = request.json['status_campaign']
            phase_campaign = request.json['phase_campaign']
            start_date = request.json['start_date']
            end_date = request.json['end_date']
            product_campaign = request.json['product_campaign']
            tasks = request.json['tasks']
            id_socmed = request.json['id_socmed']
            publish_plan = request.json['publish_plan']
            caption = request.json['caption']
            tag_people = request.json['tag_people']

            campaign = Campaigns.query.filter_by(id=id).first()
            campaign.nama_campaign = nama_campaign
            campaign.status_campaign = status_campaign
            campaign.phase_campaign = phase_campaign
            campaign.start_date = start_date
            campaign.end_date = end_date
            campaign.product_campaign = product_campaign
            campaign.tasks = tasks
            campaign.id_socmed = id_socmed
            campaign.publish_plan = publish_plan
            campaign.caption = caption
            campaign.tag_people = tag_people

            db.session.commit()

            return response.ok('', 'Successfully update campaign!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)

@jwt_required() 
def show(id):
    try:
        if 'email' in session:
            campaign = Campaigns.query.filter_by(id=id).first()
            if not campaign:
                return response.badRequest([], 'Empty....')

            data = singleTransform(campaign)
            return response.ok(data, "")
        return 'You are not signed in!'
    except Exception as e:
        print(e)

@jwt_required() 
def delete(id):
    try:
        if 'email' in session:
            campaign = Campaigns.query.filter_by(id=id).first()
            if not campaign:
                return response.badRequest([], 'Empty....')

            db.session.delete(campaign)
            db.session.commit()
        
            return response.ok('', 'Successfully delete data!')
        return 'You are not signed in!'
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    pprint(vars(values.campaigns))
    data = {
        'id': values.id,
        'user_id': values.user_id,
        'nama_campaign': values.nama_campaign,
        'status_campaign': values.status_campaign,
        'type_campaign': values.type_campaign,
        'phase_campaign': values.phase_campaign,
        'start_date': values.start_date,
        'end_date' : values.end_date,
        'product_campaign' : values.product_campaign,
        'tasks' : values.tasks,
        'id_socmed' : values.id_socmed,
        'publish_plan' : values.publish_plan,
        'caption' : values.caption,
        'tag_people' : values.tag_people,
        'user': UserController.singleTransform(values.users, withTodo=False)
    }

    return data
