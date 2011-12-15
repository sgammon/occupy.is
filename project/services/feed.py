## feed API service
from project.services import RemoteService, remote
from project.messages import feed as messages


class FeedService(RemoteService):

	@remote.method(messages.MainFeedRequest, messages.MainFeedResponse)
	def main(self, request):

		''' main site feed '''

		pass

	@remote.method(messages.MovementFeedRequest, messages.MovementFeedResponse)
	def movement(self, request):

		''' movement feed '''

		pass

	@remote.method(messages.TopicFeedRequest, messages.TopicFeedResponse)
	def topic(self, request):

		''' topic feed '''

		pass
	
	@remote.method(messages.OccupierFeedRequest, messages.OccupierFeedResponse)
	def occupier(self, request):

		''' occupier feed '''

		pass