from project.models import OccupyModel, ndb
from project.messages.topic import TopicResponse


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


class Upvote(OccupyModel):

	''' An upvote on a topic, indicating approval, placed by an unregistered or registered user of Occupy. '''

	## parent: topic
	## keyname: str(key(occupier))

	occupier = ndb.KeyProperty(indexed=True)
	topic = ndb.KeyProperty(indexed=True)

	

class Downvote(OccupyModel):

	''' A downvote on a topic, indicating disapproval, placed by an unregistered or registered user of Occupy. '''

	## parent: topic
	## keyname: str(key(occupier))

	occupier = ndb.KeyProperty(indexed=True)
	topic = ndb.KeyProperty(indexed=True)