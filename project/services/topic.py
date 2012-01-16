import logging

## topic API service
from project.services import RemoteService, remote
from project.messages import topic as messages

from project.models import ndb, topic
from project.models.social import Star, Comment
from google.appengine.ext import ndb as nndb


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
			t_key = nndb.key.Key(Topic, request.shortname)
		
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

	@remote.method(messages.TopicVoteRequest, messages.TopicVoteResponse)
	def upvote(self, request):

		''' Upvotes a topic '''

		response_obj = messages.TopicVoteResponse()

		t_key = nndb.key.Key(urlsafe=request.topic)
		o_key = nndb.key.Key(urlsafe=request.occupier)

		u = Upvote(nndb.key.Key(Upvote, request.occupier, parent=t_key))
		u.topic = t_key
		u.occupier = o_key

		response_obj.key = u.put().urlsafe()

		return response_obj
	
	@remote.method(messages.TopicVoteRequest, messages.TopicVoteResponse)
	def downvote(self, request):

		''' Downvotes a topic '''

		response_obj = messages.TopicVoteResponse()

		t_key = nndb.key.Key(urlsafe=request.topic)
		o_key = nndb.key.Key(urlsafe=request.occupier)

		d = Downvote(nndb.key.Key(Downvote, request.occupier, parent=t_key))
		d.topic = t_key
		d.occupier = o_key

		response_obj.key = d.put().urlsafe()

		return response_obj
	
	@remote.method(messages.TopicSocialRequest, messages.StarTopicResponse)
	def star(self, request):

		''' Favorites a topic '''

		response_obj = messages.StarTopicResponse()

		s_key = nndb.key.Key(urlsafe=request.subject)
		o_key = nndb.key.Key(urlsafe=request.occupier)

		s = Star(nndb.key.Key(Star, request.occupier, parent=s_key))
		s.subject = s_key
		s.occupier = o_key

		response_obj.key = s.put().urlsafe()

		return response_obj
	
	@remote.method(messages.TopicSocialRequest, messages.CommentTopicResponse)
	def comment(self, request):

		''' Comments on a topic '''

		response_obj = messages.CommentTopicResponse()

		s_key = nndb.key.Key(urlsafe=request.subject)
		o_key = nndb.key.Key(urlsafe=request.occupier)

		s = Comment(nndb.key.Key(Comment, parent=s_key))
		s.subject = s_key
		s.occupier = o_key

		response_obj.key = s.put().urlsafe()
		response_obj.created = str(s.createdAt)

		return response_obj