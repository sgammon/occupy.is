## auth API service
from project.services import RemoteService, remote
from project.messages import auth as messages


class AuthService(RemoteService):

	@remote.method(messages.LoginRequest, messages.LoginResponse)
	def login(self, request):

		''' login to site '''

		pass
	
	@remote.method(messages.LogoutRequest, messages.LogoutResponse)
	def logout(self, request):

		''' logout of site '''

		pass

	@remote.method(messages.ConnectRequest, messages.ConnectResponse)
	def connect(self, request):

		''' '''

		pass