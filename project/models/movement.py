from project.models import OccupyModel, ndb
from project.messages.movement import MovementResponse


## abstract levels at which a 'movement' entity can exist
MOVEMENT_SCOPES = set(['city', 'province', 'country', 'region', 'continent', 'world'])


class Movement(OccupyModel):

	''' Represents a localization of the Occupy movement - at any scope (country, state/principality, city). '''

	## parent: none
	## keyname: short name (for use in URLs/subdomains)
	_message_class = MovementResponse

	# naming
	name = ndb.StringProperty(required=True)
	shortname = ndb.StringProperty(required=True)

	# geo data
	bounds = ndb.GeoPtProperty(repeated=True)
	epicenter = ndb.GeoPtProperty()

	# web/social links
	website = ndb.StringProperty()
	facebook = ndb.StringProperty()

	# where this movement fits in
	ancestry = ndb.KeyProperty(repeated=True)
	scope = ndb.StringProperty(choices=MOVEMENT_SCOPES, required=True)

	@classmethod
	def from_message(cls, message, key=None, **kwargs):

		if hasattr('epicenter', message):
			epicenter = request.epicenter
			request.epicenter = None
		
		if hasattr('bounds', message):
			bounds = request.bounds
			request.bounds = []
		
		new_movement = super(Movement, cls).from_message(message, key, **kwargs)
		new_movement.epicenter = epicenter
		new_movement.bounds = bounds
		return new_movement