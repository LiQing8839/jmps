from tornado.web import RequestHandler


class LoginHandler(RequestHandler):
	def get(self):
		self.render('login.html')
	def post(self):
		username = self.get_argument('username')
		password = self.get_argument('password')
		self.authentication(username,password)
	def authentication(self,username,password):
		if username != 'niuminguo':
			return self.redirect('/login')	
		return self.redirect('/home')


