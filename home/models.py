from __future__ import absolute_import, unicode_literals

from django.db import models
import json
from django.http import HttpRequest
import requests

from wagtail.wagtailcore.models import Page

# def json_test():
#     return requests.get('http://localhost:8000/parts_by_press/WC420/EXT/')
#
# # print(json_test().json())
#
# r = requests.post('http://localhost:8000/workcenter/', json={'workcenters': ['WC400', 'WC420',]}).json()
# # print(r.text)
# print(r)

class HomePage(Page):
    pass
