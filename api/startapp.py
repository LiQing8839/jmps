from eventlet import wsgi
import eventlet
from paste.deploy import loadapp



app=loadapp('config:/home/api/paste.ini',name='api')
wsgi.server(eventlet.listen(('',8383)),app)
