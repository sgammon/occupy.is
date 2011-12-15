from project.services import RemoteService, remote
from project.messages import hello as messages


class TopicService(RemoteService):

	@remote.method(messages.HelloRequest, messages.HelloResponse)
	def hello(self, request):

		if request.name is not None:
			message = "Hello, "+request.name+"!"

		else:
			message = "Hello, friend!"

		return messages.HelloResponse(message=message)