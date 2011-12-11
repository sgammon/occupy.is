from project.models import OccupyModel


class Topic(OccupyModel):

	''' Represents a definition for Occupy - an answer to the question, "occupy is?". '''

	pass


class Upvote(OccupyModel):

	''' An upvote on a topic, indicating approval, placed by an unregistered or registered user of Occupy. '''

	pass


class Downvote(OccupyModel):

	''' A downvote on a topic, indicating disapproval, placed by an unregistered or registered user of Occupy. '''

	pass