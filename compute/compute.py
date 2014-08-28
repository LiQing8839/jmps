import service


if __name__ == "__main__":
	server=service.Service.create(binary='docker-compute',topic='docker.compute')
	server.start()

