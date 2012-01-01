from project.models import OccupyModel, ndb

class Star(OccupyModel):

	''' Marker for a Star placed on a Topic, Movement, Occupier, Comment or Trend. '''

	## parent: topic/movement/occupier/comment/trend
	## keyname: str(key(occupier))

	subject = ndb.KeyProperty(indexed=True)
	occupier = ndb.KeyProperty(indexed=True)


class Comment(OccupyModel):

	''' Comment made by a registered or unregistered user of Occupy, on a Topic, Movement, Occupier, or Trend. '''

	## parent: topic/movement/occupier/trend
	## keyname: none

	subject = ndb.KeyProperty(indexed=True)
	occupier = ndb.KeyProperty(indexed=True)