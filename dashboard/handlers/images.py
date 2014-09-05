
from tornado.web import RequestHandler
import requests
import json
import pprint
import utils


class ImageHandler(RequestHandler):
    def get(self):
        image_list=[]
        result=requests.get('http://localhost:8383/v1/images')
        result_dict=result.json()
        for res in result_dict:
            _dict={}
            _dict['Container_Id']=res['Id'][:12]
            _dict['Name']=res['RepoTags'][0]
            _dict['VirtualSize']=utils.byte_to_gb(res['VirtualSize'])
            _dict['Created']=utils.timestamp_to_local(res['Created'])
            _dict['Environ']='develop'
            image_list.append(_dict)
        self.render('images.html',data=image_list)
