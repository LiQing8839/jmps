from handlers.index import MainHandler
from handlers.login import LoginHandler
from handlers.home   import HomeHandler


urls = [
	(r'/',MainHandler),
	(r'/login',LoginHandler),
	(r'/home',HomeHandler),
]
