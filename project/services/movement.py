## movement API service
from project.services import RemoteService, remote
from project.messages import movement as messages


class MovementService(RemoteService):

	@remote.method(messages.NewMovementRequest, messages.NewMovementResponse)
	def new(self, request):

		''' request to create new movement '''

		pass

	@remote.method(messages.GetMovementRequest, messages.GetMovementResponse)
	def get(self, request):

		''' get movement profile '''
		
		pass
	
	@remote.method(messages.MovementStatsRequest, messages.MovementStatsResponse)
	def stats(self, request):

		''' movement stats! '''

		pass
	
	@remote.method(messages.ListMovementRequest, messages.ListMovementResponse)
	def list(self, request):

		''' list movements '''

		pass

	@remote.method(messages.StarMovementRequest, messages.StarMovementResponse):
	def star(self, request):

		''' favorite a particular movement '''
		
		pass
		
	@remote.method(messages.CommentMovementRequest, messages.CommentMovementResponse):
	def comment(self, request):
	
		''' comment on a movement '''
		
		pass		