from eventlet import greenpool


class ThreadPool(object):
	def __init__(self,thread_pool_size=10):
		self.pool = greenpool.GreenPool(thread_pool_size)

	def start_thread(self,callback,*args,**kwargs):
		self.pool.spawn(callback,*args,**kwargs)
