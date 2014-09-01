from eventlet import pools
import kombu


class Pool(pools.Pool):
	MAX_SIZE=10
	def __init__(self,conf,connection_cls,**kwargs):
		self.connection = connection_cls
		self.conf = conf

		super(Pool,self).__init__(max_size=self.MAX_SIZE)

	def create(self):
		return self.connection(self.conf)		


def Connection(object):
	def __init__(self,conf):
		self.conf = conf
		self.hostname = self.conf.rabbit_host
		self.port = self.conf.rabbit_port
		self.userid = self.conf.rabbit_username
		self.password = self.conf.rabbit_password
		self.connection = None
		self.channel = None
		self._connect(...)
	def _connect(self,params):
		self.connection = kombu.connection.BrokerConnection(**params)	
		self.connection.connect()
		self.channel = self.connection.channel()
	def publisher_send(self,cls,topic,msg,timeout):
		publisher=cls(self.conf,self.channel,topic)
		publisher.send(msg,timeout)
	def topic_send(self,topic,msg,timeoute=None):
		self.publisher_send(TopicPublisher,topic,msg,timeout)

class Publisher(object):
	def __init__(self,channel,exchange_name,routing_key,type):
		self.exchange_name = exchange_name
		self.routing_key = routing_key
		self.type=type
		self.channel = channel
		self.exchange = kombu.entity.Exchange(name=self.exchange_name,type=self.type)
		self.producer = kombu.messaging.Producer(exchange=self.exchange,channel=self.channel,routing_key=self.routing_key)
	def send(self,msg,timeout=None):
		self.producer.publish(msg)
		
class TopicPublisher(Publisher):
	def __init__(self,conf,channel,topic):
		exchange_name='docker'
		super(TopicPublisher,self).__init__(channel,exchange_name,topic,type='topic')

def get_connection_pool(conf):
	return Pool(conf,Connection)
