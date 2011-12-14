from project.models import OccupyModel, ndb


## abstract levels at which a 'movement' entity can exist
MOVEMENT_SCOPES = set(['city', 'province', 'country', 'region', 'continent', 'world'])


class Movement(OccupyModel):

	''' Represents a localization of the Occupy movement - at any scope (country, state/principality, city). '''

	## parent: none
	## keyname: short name (for use in URLs/subdomains)

	# naming
	name = ndb.StringProperty(required=True)
	shortname = ndb.StringProperty(required=True)

	# geo data
	bounds = ndb.GeoPointProperty(repeated=True)
	epicenter = ndb.GeoPointProperty()

	# web/social links
	website = ndb.StringProperty()
	facebook = ndb.StringProperty()

	# where this movement fits in
	ancestry = ndb.KeyProperty(repeated=True)
	scope = ndb.StringProperty(choices=MOVEMENT_SCOPES, required=True)