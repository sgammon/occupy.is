from protorpc import messages


class HelloRequest(messages.Message):

	name = messages.StringField(1)


class HelloResponse(messages.Message):

	message = messages.StringField(1)