import tornado.ioloop
from application import application

PORT='8080'

if __name__ == '__main__':
    application.listen(PORT)
    print "Start server on http *:{}...".format(PORT)
    tornado.ioloop.IOLoop.instance().start()
