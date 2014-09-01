import webob.exc.wsgify

class ImageController(object):
	@webob.exc.wsgify
	def __call__(
