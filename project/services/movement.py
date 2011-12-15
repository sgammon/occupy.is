## movement API service
from project.services import RemoteService, remote
from project.messages import movement as messages


class MovementService(RemoteService):

	@remote.method(messages.NewMovementRequest, messages.NewMovementResponse)
	def new(self, request):

		''' Creates new movement '''

		pass

	@remote.method(messages.GetMovementRequest, messages.GetMovementResponse)
	def get(self, request):

		''' Returns a movement '''
		
		pass
	
	@remote.method(messages.MovementStatsRequest, messages.MovementStatsResponse)
	def stats(self, request):

		''' Returns stats about a movement '''

		pass
	
	@remote.method(messages.ListMovementRequest, messages.ListMovementResponse)
	def list(self, request):

		''' Lists movements '''

		pass

	@remote.method(messages.StarMovementRequest, messages.StarMovementResponse):
	def star(self, request):

		''' Favorites a movement '''
		
		pass
		
	@remote.method(messages.CommentMovementRequest, messages.CommentMovementResponse):
	def comment(self, request):
	
		''' Comments on a movement '''
		
		pass		