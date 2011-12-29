import logging
from project.services import RemoteService, remote
from project.messages import topic as messages

from project.models import ndb
from google.appengine.ext import ndb as nndb
from project.models.topic import Topic


class TopicService(RemoteService):

	@remote.method(messages.NewTopicRequest, messages.TopicResponse)
	def new(self, request):

		''' Creates new topic '''

		t = Topic.from_message(request, key=nndb.key.Key(Topic, request.shortname))
		
		t_key = t.put()

		response_obj = t.to_message()
		response_obj.key = t_key.urlsafe()
		return response_obj

	@remote.method(messages.GetTopicRequest, messages.TopicResponse)
	def get(self, request):

		''' Returns a topic '''

		if request.key is None:
			t_key= nndb.key.Key(Topic, request.shortname)
		
		elif request.shortname is None:
			t_key = Topic.Key(urlsafe=request.key)
		
		t = t_key.get()

		return t.to_message()

	@remote.method(messages.TopicStatsRequest, messages.TopicStatsResponse)
	def stats(self, request):

		''' Return stats for a topic '''

		pass

	@remote.method(messages.ListTopicRequest, messages.ListTopicResponse)
	def list(self, request):

		''' Lists topics '''

		response_obj = messages.ListTopicResponse()

		topic_query = Topic.query()
		topic_results = topic_query.fetch(25)

		if len(topic_results) > 0:
			topic_responses = []

			for topic in topic_results:
				topic_responses.append(topic.to_message())

		else:
			topic_responses = []
		
		response_obj.topics = topic_responses
		return response_obj

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