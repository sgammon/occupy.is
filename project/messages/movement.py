from protorpc import messages


class LatLong(messages.Message):

	latitude = messages.StringField(1)
	longitude = messages.StringField(2)


class MovementResponse(messages.Message):

	key = messages.StringField(1)
	name = messages.StringField(2)
	shortname = messages.StringField(3)
	bounds = messages.MessageField(LatLong, 4, repeated=True)
	epicenter = messages.StringField(5)
	website = messages.StringField(6)
	facebook = messages.StringField(7)
	ancestry = messages.StringField(8, repeated=True)
	scope = messages.StringField(9)


class NewMovementRequest(messages.Message):

	name = messages.StringField(1)
	shortname = messages.StringField(2)
	bounds = messages.MessageField(LatLong, 3, repeated=True)
	epicenter = messages.StringField(4)
	website = messages.StringField(5)
	facebook = messages.StringField(6)
	ancestry = messages.StringField(7, repeated=True)
	scope = messages.StringField(8)


class GetMovementRequest(messages.Message):

	key = messages.StringField(1)
	shortname = messages.StringField(2)


class MovementStatsRequest(messages.Message):

	pass


class MovementStatsResponse(messages.Message):

	pass


class ListMovementRequest(messages.Message):

	pass


class ListMovementResponse(messages.Message):

	movements = messages.MessageField(MovementResponse, 1, repeated=True)


class MovementSocialRequest(messages.Message):

	occupier = messages.StringField(1)
	subject = messages.StringField(2)


class StarMovementResponse(messages.Message):

	key = messages.StringField(1)


class CommentMovementResponse(messages.Message):

	key = messages.StringField(1)
	created = messages.StringField(2)	