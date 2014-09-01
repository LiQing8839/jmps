import pools

class RPCClient(object):
	def __init__(self,proxy,namespace=None,server_params=None):
		super(RPCClient,self).__init__()
	def create_connection(new=True):
		return _create_connection(CONF,new=new)
	def call(context,topic,msg,timeout):
		return _get_impl().call(CONF,context,topic,msg,timeout)
	def cast(context,topic,msg)
		return _get_impl().cast(CONF,context,topic,msg)
		

class RPCAPI(object):
	def __init__(self):
		self.pool=pools.get_connection_pool()
	def get_client():
	def cast(self,context,topic,msg):
		self.client.call(context,topic,msg,self.pool)
	def call():
