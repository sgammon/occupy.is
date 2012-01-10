from project.models import OccupyModel, ndb


#### +=+=+=+ Occupiers + Accounts +=+=+=+ ####
class Occupier(OccupyModel):

	''' Represents a concerned citizen who has signed themselves up as an Occupier (essentially a site user). '''

	## parent: none
	## keyname: username (for use in URLs)

	_message_class = OccupierResponse

	# name + basic ID
	username = ndb.StringProperty(indexed=True, required=True)
	firstname = ndb.StringProperty(indexed=True, required=True)
	lastname = ndb.StringProperty(indexed=True, required=False)

	# demographics
	dob = ndb.DateProperty(indexed=True, required=False)
	ethnicity = ndb.StringProperty(repeated=True, indexed=False, required=False)
	profession = ndb.StringProperty(indexed=False, required=False)
	country = ndb.StringProperty(indexed=True, required=False)

	# fun profile stuff
	aboutme = ndb.TextProperty()
	manifesto = ndb.TextProperty()

	def to_message(self, include=None, exclude=None):
		
		response = self._message_class()

		if self.key is not None:
			response.key = self.key.urlsafe()
		else:
			response.key = None

		for k, v in self.to_dict(include=include, exclude=exclude).items():
			if hasattr(response, k):
				setattr(response, k, str(v))

		return response
	
	@classmethod
	def from_message(cls, message, key=None, **kwargs):

		if hasattr('dob', message):
			dob = request.dob
			request.dob = None
		
		new_occupier = super(Occupier, cls).from_message(message, key, **kwargs)
		new_occupier.dob = dob
		return new_occupier


class OccupierAccount(OccupyModel):

	''' An attached social media or local account for an Occupier. '''

	## parent: occupier
	## keyname: username

	# account ID info
	id = ndb.StringProperty(indexed=True)
	source = ndb.StringProperty(choices=['facebook', 'twitter', 'foursquare'], indexed=True)
	account = ndb.UserProperty(indexed=True)
	username = ndb.StringProperty(indexed=True)

	# account links
	profile_page = ndb.StringProperty(indexed=False)
	display_public = ndb.BooleanProperty(indexed=False)

	# crawl/storage info
	authorized = ndb.BooleanProperty(default=False, indexed=True)
	crawl_posts = ndb.BooleanProperty(default=False, indexed=True)


#### +=+=+=+ Attached Media +=+=+=+ ####
class ProfilePicture(OccupyModel):

	''' An uploaded/attached profile picture for an Occupier. '''

	## parent: occupier
	## keyname: none

	# basic data
	occupier = ndb.KeyProperty(indexed=True)
	caption = ndb.StringProperty(indexed=False)

	# blob/serving data
	blob_ref = ndb.BlobKeyProperty(indexed=True)
	enable_fast_serving = ndb.BooleanProperty(indexed=True)
	fast_serving_href = ndb.StringProperty(indexed=False)

	# img data
	width = ndb.IntegerProperty(indexed=False)
	height = ndb.IntegerProperty(indexed=False)


#### +=+=+=+ Starred Items +=+=+=+ ####
class OccupierStarredItem(OccupyModel):

	''' An item that an Occupier has starred. '''

	## parent: occupier
	## keyname: see subclasses

	star = ndb.KeyProperty(indexed=True)


class StarredTopic(OccupierStarredItem):

	''' Indicates that an Occupier has starred a topic. '''

	## parent: occupier
	## keyname: str(key(topic))

	occupier = ndb.KeyProperty(indexed=True)
	topic = ndb.KeyProperty(indexed=True)


class StarredComment(OccupierStarredItem):

	'''  Indicates that an Occupier has starred a comment. '''

	## parent: occupier
	## keyname: str(key(comment))

	occupier = ndb.KeyProperty(indexed=True)
	comment = ndb.KeyProperty(indexed=True)


class StarredMovement(OccupierStarredItem):

	''' Indicates that an Occupier has starred a movement. '''

	## parent: occupier
	## keyname: str(key(movement))

	occupier = ndb.KeyProperty(indexed=True)
	movement = ndb.KeyProperty(indexed=True)