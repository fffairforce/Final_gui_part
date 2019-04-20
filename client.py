# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:17:29 2019

@author: wl181
"""

import requests

api_host = "http://127.0.0.1:5000"

def get_uploaded_img():
    website = api_host + '/image/upload'
    r = requests.get(website)
    upload = r.json
    return upload

def post_uploaded_img():
    r = requests.post(api_host + '/image/upload' + json=img_dic)  #need define 
    
def get_timestamp():
    website = api_host + '/image/timstamp'
    r = requests.get(website)
    timestamp = r.json
    return timestamp

def get_img_size():
    website = api_host + '/image/size'
    r = requests.get(website)
    img_size = r.json
    return img_size

def post_processed_img():
    pass

