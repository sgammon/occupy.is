from protorpc import messages


class OccupierResponse(messages.Message):

	key = messages.StringField(1)
	username = messages.StringField(2)
	firstname = messages.StringField(3)
	lastname = messages.StringField(4)
	dob = messages.StringField(5)
	ethnicity = messages.StringField(6)
	profession = messages.StringField(7)
	country = messages.StringField(8)
	aboutme = messages.StringField(9)
	manifesto = messages.StringField(10)


class NewOccupierRequest(messages.Message):

	username = messages.StringField(1)
	firstname = messages.StringField(2)
	lastname = messages.StringField(3)
	dob = messages.StringField(4)
	ethnicity = messages.StringField(5)
	profession = messages.StringField(6)
	country = messages.StringField(7)
	aboutme = messages.StringField(8)
	manifesto = messages.StringField(9)


class GetOccupierRequest(messages.Message):

	key = messages.StringField(1)
	username = messages.StringField(2)


class OccupierAvatarRequest(messages.Message):

	pass


class OccupierAvatarResponse(messages.Message):

	pass


class MessageOccupierRequest(messages.Message):

	pass


class MessageOccupierResponse(messages.Message):

	pass