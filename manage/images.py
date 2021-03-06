import webob
import webob.dec
import requests
import json



class ImageController(object):
	@webob.dec.wsgify
	def __call__(self,request):
		method=request.environ['wsgiorg.routing_args'][1]['action']
		method=getattr(self,method)		
		response=webob.Response()
		method(request,response)
		return response
	def index(self,request,response):
		headers={'Content-Type':'application/json'}
		result=requests.get("http://0.0.0.0:2375/images/json",headers=headers)	
		if result.status_code == 200:
			response.json=result.json()
	def inspect(self,request,response):
		image_id=request.environ['wsgiorg.routing_args'][1]['image_id']
		result=requests.get("http://0.0.0.0:2375/images/{}/json".format(image_id))
		if result.status_code == 200:
			response.json=result.json()
		if result.status_code == 404:
			errors={"errors":"404 Not Found:no such image {}".format(image_id)}
			response.json=errors
	def create(self,request,response):
		response.body="{create}\n"	
	def delete(self,request,response):
		image_id=request.environ['wsgiorg.routing_args'][1]['image_id']
		result=requests.delete("http://0.0.0.0:2375/images/{}".format(image_id))
		if result.status_code == 200:
			response.json=result.json()
		if result.status_code == 404:
			errors={"errors":"404 Not Found:no such image {}".format(image_id)}
			response.json=errors
		if result.status_code == 409:
			errors={"errors":"409 conflict"}
			response.json=errors
		if result.status_code == 500:
			errors={"errors":"500 internal server error"}
			response.json=errors
