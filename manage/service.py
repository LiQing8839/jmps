@classmethod
def create(cls):
	service_obj=cls()
	return service_obj

def launch(service):
	launcher=ServiceLauncher()
	launcher.launch_service(service)

@staticmethod
def run_service(service):
	service.start()
	service.wait()

launcher = service.process_launcher()
ProcessLauncher
server=service.WSGIService(api)

launcher.launch_service(server,workers=server.workers or 1)
launcher.wait()

