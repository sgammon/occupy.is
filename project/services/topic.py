from project.services import RemoteService, remote
from project.messages import topic as messages


class TopicService(RemoteService):

	@remote.method(messages.NewTopicRequest, messages.NewTopicResponse)
	def new(self, request):

		''' Creates new topic '''

		pass


	@remote.method(messages.GetTopicRequest, messages.GetTopicResponse)
	def get(self, request):

		''' Returns a topic '''

		pass

	@remote.method(messages.TopicStatsRequest, messages.TopicStatsResponse)
	def stats(self, request):

		''' Return stats for a topic '''

		pass

	@remote.method(messages.ListTopicRequest, messages.ListTopicResponse)
	def list(self, request):

		''' Lists topics '''

		pass
	
	@remote.method(messages.UpvoteTopicRequest, messages.UpvoteTopicResponse)
	def upvote(self, request):

		''' Upvotes a topic '''

		pass
	
	@remote.method(messages.DownvoteTopicRequest, messages.DownvoteTopicResponse)
	def downvote(self, request):

		''' Downvotes a topic '''

		pass
	
	@remote.method(messages.StarTopicRequest, messages.StarTopicResponse)
	def star(self, request):

		''' Favorites a topic '''

		pass
	
	@remote.method(messages.CommentTopicRequest, messages.CommentTopicResponse)
	def comment(self, request):

		''' Comments on a topic '''

		pass