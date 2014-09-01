import webob
import webob.dec
import requests
import json
import ast
from database import DB

class ContainerAPI():
	def __init__(self):
		self.image_api=images.ImageAPI()
		self.db_api=DB()
		self.rpc_api=rpc.RPCAPI()
	def create(self,name,image_id,exposed_port,cmd_context):
		kwargs = { 'name' :  name,
		       'image' : image_id,
			'port' : exposed_port,
			'cmd'  : cmd_context,
		}
		rpc_client=self.rpc_api.get_client(
		self.rpc_api.cast('build_container',**kwargs)	
	def delete(self,container_id):
		self.rpc_api.cast('terminate_instance',instance=container_id)
	def get_containers(self):
		self.db.get_containers()
	def get_container_by_id(self,id):
		self.db.get_container_by_id(id)	
	def create_container(self):
		pass
	def delete_container(self,id):
		self.db.delete_container_by_id(id)
	def start_instance(self,ctxt,instance):
		cctxt.cast(ctxt,'start_instance',instance=instance)
	def stop_instance(instance):
		rpc.cast('stop_instance',instance=instance)

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
	def __init__(self):
		self.compute_api=ContainerAPI()
	def index(self,request,response):
		containers=self.compute_api.get_containers(request)
		return containers
		#result=requests.get("http://0.0.0.0:2375/containers/json")	
		#response.headers.add("Content-Type","application/json")
		#response.json=result.json()
	def inspect(self,request,response):
		container_id=request.environ['wsgiorg.routing_args'][1]['container_id']
		result=requests.get("http://0.0.0.0:2375/containers/{}/json".format(container_id))
		if result.status_code == 200:
			response.json=json.dumps(dict(result.json()))
		if result.status_code == 404:
			errors={"errors":"404 Not Found:no such container {}".format(container_id)}
			response.json=errors
			
	def create(self,request,response):
		container_dict=body['container']
		if 'name' not in container_dict:
			msg = _("Container name is not defined")
			raise exc.HTTPBadRequest(explanation=msg)

		image_id=self._image_from_req_data(body)
		
		command_context=self._command_from_req_data(body)

		exposed_port=self._get_exposed_port(image_id)

		self.compute_api.create(name,image_id,exposed_port,command_context)
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
			
	def delete(self,request,response):
		#response.body="{delete}\n"
		try:
			self.compute.api._delete(id)
		except  exception.NotFound:
			msg=_("Containers could not be found")
			raise exc.HTTPNotFound(explanation=msg)
	def start(self,request,response):
		container_id=request.environ['wsgiorg.routing_args'][1]['container_id']
		result=requests.get("http://0.0.0.0:2375/containers/{}/json".format(container_id))
	def stop(self.request,response):
		pass
		
		
def create_resource():
	return Controller()
