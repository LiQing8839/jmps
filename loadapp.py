from wsgiref.simple_server import make_server


import routes.middleware
import webob.dec
import webob.exc
from paste.deploy import loadapp
from eventlet import wsgi
import eventlet


class Controller:
	@webob.dec.wsgify
	def __call__(self,req):
		return webob.Response("Hello,world")

class Container:
	@webob.dec.wsgify
	def __call__(self,req):
		method=req.environ['wsgiorg.routing_args'][1]['action']
		method=getattr(self,method)		
		response=webob.Response()
		method(response)
		return response
	def index(self,response):
		response.body="index\n"	
	def create(self,response):
		response.body="create\n"	
	def delete(self,response):
		response.body="delete\n"

class Router(object):
	def __init__(self):
		self._mapper=routes.Mapper()
		self._mapper.connect(
					'/home',
					controller=Controller(),
					action='index',
					conditions={'method':['GET']}
		)
		self._mapper.connect('/v1/containers',
					controller=Container(),
					action='index',
					conditions={'method':['GET']}
		)

		self._mapper.connect('/v1/containers',
					controller=Container(),
					action='create',
					conditions={'method':['POST']}
		)

		self._mapper.connect('/v1/containers/{container_id',
					controller=Container(),
					action='delete',
					condition={'method':['DELETE']}
		)

		self._router=routes.middleware.RoutesMiddleware(self._dispatch,self._mapper)

	@classmethod
	def app_factory(cls,global_config,**local_config):
		return cls()
	
	@webob.dec.wsgify
	def __call__(self,req):
		return self._router

	@staticmethod
	@webob.dec.wsgify
	def _dispatch(req):
		match=req.environ['wsgiorg.routing_args'][1]
		if not match:
			return webob.exc.HTTPNotFound()
		app=match['controller']
		return app

if __name__ == "__main__":
	app=loadapp('config:/home/paste.ini',name='hello')
	wsgi.server(eventlet.listen(('',8282)),app)
