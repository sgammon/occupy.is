from project.models import OccupyModel


class Occupier(OccupyModel):

	''' Represents a concerned citizen who has signed themselves up as an Occupier (essentially a site user). '''

	pass


class ProfilePicture(OccupyModel):

	''' An uploaded/attached profile picture for an Occupier. '''

	pass


class OccupierAccount(OccupyModel):

	''' An attached social media or local account for an Occupier. '''

	pass


class StarredTopic(OccupyModel):

	''' Indicates that an Occupier has starred a topic. '''

	pass


class StarredComment(OccupyModel):

	'''  Indicates that an Occupier has starred a comment. '''

	pass


class StarredMovement(OccupyModel):

	''' Indicates that an Occupier has starred a movement. '''

	pass