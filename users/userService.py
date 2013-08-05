# -*- coding: utf-8 -*-

from core.service import Service
from user import User
import json

class UserService(Service):
    def __init__(self):
        super(UserService, self).__init__()

    def save(self, model):
        model.save()

    def find(self):
        found = User.objects
        return User.json_tree(found)

    def count(self):
        found = User.objects
        return len(found)