
from tornado.web import RequestHandler
from tornado.web import HTTPError
import log


class ContainerHandler(RequestHandler):
    def get(self):
        containers={}
        if containers:
            try:
                self.render('containers.html')
            except HTTPError as err:
                log.LOG(err)
        else:
            try:
                self.render('no_containers.html')
            except HTTPError as err:
                log.LOG(err)
        
