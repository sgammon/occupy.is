from project.services import RemoteService, remote
from project.messages import topic as messages


class TopicService(RemoteService):

	@remote.method(messages.NewTopicRequest, messages.NewTopicResponse)
	def new(self, request):

		''' Request to create new topic '''

		pass


	@remote.method(messages.GetTopicRequest, messages.GetTopicResponse)
	def get(self, request):

		''' Get topic request '''

		pass

	@remote.method(messages.TopicStatsRequest, messages.TopicStatsResponse)
	def stats(self, request):

		''' Request for topic stats '''

		pass

	@remote.method(messages.ListTopicRequest, messages.ListTopicResponse)
	def list(self, request):

		''' lists topics '''

		pass
	
	@remote.method(messages.UpvoteTopicRequest, messages.UpvoteTopicResponse)
	def upvote(self, request):

		''' upvotes a topic '''

		pass
	
	@remote.method(messages.DownvoteTopicRequest, messages.DownvoteTopicResponse)
	def downvote(self, request):

		''' downvotes a topic '''

		pass
	
	@remote.method(messages.StarTopicRequest, messages.StarTopicResponse)
	def star(self, request):

		''' favorites a topic '''

		pass
	
	@remote.method(messages.CommentTopicRequest, messages.CommentTopicResponse)
	def comment(self, request):

		''' comments on a topic '''

		pass