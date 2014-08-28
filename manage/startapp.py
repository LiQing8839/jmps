from eventlet import wsgi
import eventlet
from paste.deploy import loadapp



app=loadapp('config:/home/image/paste.ini',name='manage')
wsgi.server(eventlet.listen(('',8181)),app)
