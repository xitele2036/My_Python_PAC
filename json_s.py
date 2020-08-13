#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import os
import json
import demjson




f = open("web.json",'r',encoding='utf-8')
data=json.loads(web.json)
jobs=data['content']['data']['page']['result']
