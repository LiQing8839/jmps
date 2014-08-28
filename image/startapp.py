from eventlet import wsgi
import eventlet
from paste.deploy import loadapp



app=loadapp('config:/home/image/paste.ini',name='docker-image')
wsgi.server(eventlet.listen(('',8282)),app)
