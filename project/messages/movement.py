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

	pass


class NewMovementResponse(messages.Message):

	pass


class GetMovementRequest(messages.Message):

	pass


class GetMovementResponse(messages.Message):

	pass


class MovementStatsRequest(messages.Message):

	pass


class MovementStatsResponse(messages.Message):

	pass


class ListMovementRequest(messages.Message):

	pass


class ListMovementResponse(messages.Message):

	pass


class StarMovementRequest(messages.Message):

	pass


class StarMovementResponse(messages.Message):

	pass


class CommentMovementRequest(messages.Message):

	pass


class CommentMovementResponse(messages.Message):

	pass