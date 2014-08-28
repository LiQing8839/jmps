import webob
import webob.dec
import requests
import json
import ast

URL="http://0.0.0.0:2375"
PORT=2375

class ContainerController(object):
	@webob.dec.wsgify
	def __call__(self,request):
		method=request.environ['wsgiorg.routing_args'][1]['action']
		method=getattr(self,method)		
		response=webob.Response()
		method(request,response)
		return response
	def index(self,request,response):
		result=requests.get("http://0.0.0.0:2375/containers/json")	
		response.headers.add("Content-Type","application/json")
		response.json=result.json()
	def inspect(self,request,response):
		container_id=request.environ['wsgiorg.routing_args'][1]['container_id']
		result=requests.get("http://0.0.0.0:2375/containers/{}/json".format(container_id))
		if result.status_code == 200:
			response.json=json.dumps(dict(result.json()))
		if result.status_code == 404:
			errors={"errors":"404 Not Found:no such container {}".format(container_id)}
			response.json=errors
			
	def create(self,request,response):
		params=list(request.POST)[0]
		params_dict=ast.literal_eval(params)
		cmd=params_dict.get('cmd')
		image=params_dict.get('image')	
		args={'Cmd':cmd,'Image':image}	
		url="http://0.0.0.0:2375/container/create"
		headers={'Content-Type':'application/json'}
		result=requests.post(url,data=json.dumps(args),headers=headers)
		print result.status_code
		if result.status_code == 404:
			error={"error":"404 Not Found:no such image {}".format(image)}
			response.json=error
		if result.status_code == 201:
			response.json=json.dumps(dict(result.json()))
		if result.status_code == 500:
			error={"error":"500 internal server error"}
			response.json=error
			
	def delete(self,request,response):
		response.body="{delete}\n"
	def start(self,request,response):
		container_id=request.environ['wsgiorg.routing_args'][1]['container_id']
		result=requests.get("http://0.0.0.0:2375/containers/{}/json".format(container_id))
	def stop(self.request,response):
		pass
		
		
