import webob
import webob.dec
import requests
import json
import ast
#from database import DB
import config

class ContainerAPI():
    def __init__(self):
        self.url = "http://{}:{}".format(config.docker_host,config.docker_port) 
    def create_container(self,name,image_id,exposed_port,cmd_context):
		kwargs = { 
			'name' 	:  name,
		       	'image' :  image_id,
			'port' 	:  exposed_port,
			'cmd'  	:  cmd_context,
		}
    def delete_container(self,container_id):
	result=requests.delete("{}/containers/{}".format(self.url,container_id))	
	return result
    def get_containers(self):
	result=requests.get("{}/containers/json?all=1".format(self.url))	
	return result
    def get_container_by_id(self,container_id):
	result=requests.get("{}/containers/json?all=1".format(self.url))	
	response=webob.Response()
	for res in result.json():
		if container_id in res['Id']:
			#response.json = res	
			pass
	return result 
    def start_container(self,ctxt,instance):
	cctxt.cast(ctxt,'start_instance',instance=instance)
    def stop_container(instance):
	rpc.cast('stop_instance',instance=instance)


class ContainerController(object):
    def __init__(self):
    	self.compute_api=ContainerAPI()
    @webob.dec.wsgify
    def __call__(self,request):
	print request.environ['wsgiorg.routing_args']
	print request.method
    	method=request.environ['wsgiorg.routing_args'][1]['action']
	print '----------------'
	print method
	print '----------------'
    	method=getattr(self,method)		
    	response=webob.Response()
    	result_json=method(request)
    	response.headers.add("Content-Type","application/json")
    	response.json=result_json
    	return response
    def index(self,request):
    	containers=self.compute_api.get_containers()
    	return containers
    def show(self,request):
    	container_id=request.environ['wsgiorg.routing_args'][1]['container_id']
    	container=self.compute_api.get_container_by_id(container_id)
    	return container
    def inspect(self,request):
    	container_id=request.environ['wsgiorg.routing_args'][1]['container_id']
    	result=requests.get("http://0.0.0.0:2375/containers/{}/json".format(container_id))
    	#if result.status_code == 200:
    	#	response.json=json.dumps(dict(result.json()))
    	#if result.status_code == 404:
    	#	errors={"errors":"404 Not Found:no such container {}".format(container_id)}
    	#	response.json=errors
    	#	
    def delete(self,request):
    	container_id=request.environ['wsgiorg.routing_args'][1]['container_id']
    	result=self.compute_api.delete_container(container_id)
	if result.status_code == 204:
		result_json = {"succeed":"{} deleted".format(container_id)}
	if result.status_code == 400:
		result_json = {"error":"400 bad parameter"}	
	if result.status_code == 404:
		result_json = {"error":"404 no such container"}
	if result.status_code == 500:
		result_json = {"error":"500 internal server error"}
    	return result_json
    def create(self,request):
    	container_dict=body['container']
    	if 'name' not in container_dict:
    		msg = _("Container name is not defined")
    		raise exc.HTTPBadRequest(explanation=msg)
    
    	image_id=self._image_from_req_data(body)
    	
    	command_context=self._command_from_req_data(body)
    
    	exposed_port=self._get_exposed_port(image_id)
    
    	self.compute_api.create_container(name,image_id,exposed_port,command_context)
    	#params=list(request.POST)[0]
    	#params_dict=ast.literal_eval(params)
    	#cmd=params_dict.get('cmd')
    	#image=params_dict.get('image')	
    	#args={'Cmd':cmd,'Image':image}	
    	#url="http://0.0.0.0:2375/container/create"
    	#headers={'Content-Type':'application/json'}
    	#result=requests.post(url,data=json.dumps(args),headers=headers)
    	#print result.status_code
    	#if result.status_code == 404:
    	#	error={"error":"404 Not Found:no such image {}".format(image)}
    	#	response.json=error
    	#if result.status_code == 201:
    	#	response.json=json.dumps(dict(result.json()))
    	#if result.status_code == 500:
    	#	error={"error":"500 internal server error"}
    	#	response.json=error
    		
