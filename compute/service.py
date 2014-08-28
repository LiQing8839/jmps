import threadpool
import manager

class Service(object):
	def __init__(self,host,binary,topic):
		self.host = host
		self.binary = binary
		self.topic=topic
		self.manager=manager.ComputeManager()
		self.thread_pool=threadpool.ThreadPool()
	@staticmethod
	def _start():
		self.conn = rpc.create_connection(new=True)
		LOG.debug(_("Creating Consumer connection for Service %s")%self.topic)
		
		rpc_dispatcher = self.manager.create_rpc_dispatcher()

		self.conn.create_consumer(self.topic,rpc_dispatcher,fanout=False)
		
		node_topic = '%s.%s' % (self.topic,self.host)
		self.conn.create_consumer(node_topic,rpc_dispatcher,fanout=False)
		self.conn.create_consumer(self.topic,rpc_dispatcher,fanout=True)

		self.conn.consume_in_thread()
	def start(self):
		self.thread_pool.pool.start_thread(_start)	

	@classmethod
	def create(cls,host=None,binary=None,topic=None,manager=None):
		return cls(host,binary,topic,manager)
