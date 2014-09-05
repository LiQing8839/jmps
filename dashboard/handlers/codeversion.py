
from tornado.web import RequestHandler


class CodeVersionHandler(RequestHandler):
	def get(self):
		self.render('codeversion.html')
