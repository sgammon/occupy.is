from project.models import OccupyModel, ndb
from project.messages.topic import TopicResponse, TopicVoteResponse


class Topic(OccupyModel):

	''' Represents a definition for Occupy - an answer to the question, "occupy is?". '''

	## parent: none
	## keyname: shortname
	_message_class = TopicResponse

	# name/proposal
	name = ndb.StringProperty(indexed=True)
	shortname = ndb.StringProperty(indexed=True)
	manifesto = ndb.TextProperty()

	# audit
	posted_by = ndb.KeyProperty(indexed=True)
	edited_by = ndb.KeyProperty(indexed=True, default=None)



class Vote(OccupyModel):

	''' The base model for a topic up- or downvote '''

	_message_class = TopicVoteResponse

	occupier = ndb.KeyProperty(indexed=True)
	topic = ndb.KeyProperty(indexed=True)

	def to_message(self, include=None, exclude=None):
		
		response = self._message_class()

		if self.key is not None:
			response.key = self.key.urlsafe()
		else:
			response.key = None

		for k, v in self.to_dict(include=include, exclude=exclude).items():
			if hasattr(response, k):
				setattr(response, k, v.urlsafe())

		return response



class Upvote(Vote):

	''' An upvote on a topic, indicating approval, placed by an unregistered or registered user of Occupy. '''

	## parent: topic
	## keyname: str(key(occupier))

	pass


class Downvote(Vote):

	''' A downvote on a topic, indicating disapproval, placed by an unregistered or registered user of Occupy. '''

	## parent: topic
	## keyname: str(key(occupier))

	pass