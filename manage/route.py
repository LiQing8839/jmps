from images import ImageController

import routes
import routes.middleware
import webob.dec

class Router (object):
	def __init__(self):

		self.mapper=routes.Mapper()
		self.controller=ImageController()

		self.mapper.connect('/images',
				controller=self.controller,
				action='index',
				conditions={'method':['GET']},
		)
		self.mapper.connect('/images/{image_id}',
				controller=self.controller,
				action='inspect',
				conditions={'method':['GET']},
		)

		self.mapper.connect('/images',
				controller=self.controller,
				action='create',
				conditions={'method':['POST']},
		)
		
		self.mapper.connect('/images/{image_id}',
				controller=self.controller,
				action='delete',
				conditions={'method':['DELETE']},
		)
		self.router=routes.middleware.RoutesMiddleware(self._dispatch,self.mapper)

	@classmethod
	def factory(cls,global_config,**local_config):
		return cls()
	
	@webob.dec.wsgify
	def __call__(self,req):
		return self.router

	@staticmethod
	@webob.dec.wsgify
	def _dispatch(req):
		match=req.environ['wsgiorg.routing_args'][1]
		if not match:
			return webob.Response('{"error" : "404 Not Found"}\n')
		app=match['controller']
		return app
