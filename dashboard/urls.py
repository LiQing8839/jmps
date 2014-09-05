from handlers.index import MainHandler
from handlers.login import LoginHandler
from handlers.home   import HomeHandler
from handlers.containers import ContainerHandler
from handlers.images    import ImageHandler
from handlers.codeversion import CodeVersionHandler


urls = [
	(r'/',MainHandler),
	(r'/login',LoginHandler),
	(r'/home',HomeHandler),
    (r'/containers',ContainerHandler),
    (r'/images',ImageHandler),
    (r'/codeversion',CodeVersionHandler),
]
