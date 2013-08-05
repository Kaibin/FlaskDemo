# -*- coding: utf-8 -*-

from mongoengine import *
from common.mongo_serialize import Serializable

class UserBasic(EmbeddedDocument, Serializable):
    uid = StringField(max_length=50, required=True)
    uname = StringField(max_length=50, required=True)
    nick = StringField(max_length=50, required=True)
    role = IntField()
    gender = BooleanField()
    avatar = StringField()
    status = IntField()
    introduction = StringField()
    birth_date = IntField()
    tags = ListField(StringField())

class SNS(EmbeddedDocument, Serializable):
    tel_number = StringField(max_length=50)
    qq_number = StringField(max_length=50)
    qq_weibo_id = StringField(max_length=50)
    qq_weibo_nick = StringField(max_length=50)
    sina_weibo_id = StringField(max_length=50)
    sina_weibo_nick = StringField(max_length=50)
    renren_id = StringField(max_length=50)
    renren_nick = StringField(max_length=50)

class Log(EmbeddedDocument, Serializable):
    last_log_date = IntField()
    last_log_ip = IntField()
    last_log_latitude = FloatField()
    last_log_longitude = FloatField()

class Statistic(EmbeddedDocument, Serializable):
    fan_count = IntField()
    follow_count = IntField()
    my_activity = IntField()

class Device(EmbeddedDocument, Serializable):
    device_id = StringField(max_length=50, required=True)
    device_os = StringField(max_length=50, required=True)
    device_token = StringField(max_length=50, required=True)
    device_name = StringField(max_length=50, required=True)

class Registion(EmbeddedDocument, Serializable):
    reg_date = IntField(required=True)
    reg_type = IntField(default=1)
    reg_ip = IntField()

class User(Document, Serializable):
    basic_info = EmbeddedDocumentField(UserBasic, required=True)
    registion = EmbeddedDocumentField(Registion)
    device_info = EmbeddedDocumentField(Device)
    log_info = EmbeddedDocumentField(Log)
    sns_info = EmbeddedDocumentField(SNS)
    statistic = EmbeddedDocumentField(Statistic)




