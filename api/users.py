# -*- coding: utf-8 -*-

"""
    User endpoints
"""

from flask import Blueprint, request, Response
from services import UserService
from models import UserBasic, User

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/add')
def add_user():

    uid = request.args.get('uid')
    uname = request.args.get('uname')
    nick = request.args.get('nick')

    user = User()
    basic_info = UserBasic()
    basic_info.uid = uid
    basic_info.uname = uname
    basic_info.nick = nick
    user.basic_info = basic_info

    userService = UserService()
    userService.save(user)
    return ''

@bp.route('/list')
def list_user():
    userService = UserService()
    users = userService.find()
    resp = Response(users, status=200, mimetype='application/json')
    return resp

@bp.route('/count')
def count_user():
    userService = UserService()
    count = userService.count()
    resp = Response(str(count), status=200, mimetype='application/json')
    return resp


@bp.route('/update')
def update_user():
    return ''
pass