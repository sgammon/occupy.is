from protorpc import messages


class TopicResponse(messages.Message):

	key = messages.StringField(1)
	name = messages.StringField(2)
	shortname = messages.StringField(3)
	manifesto = messages.StringField(4)
	posted_by = messages.StringField(5)
	edited_by = messages.StringField(6)
	created_at = messages.StringField(7)


class NewTopicRequest(messages.Message):

	name = messages.StringField(1)
	shortname = messages.StringField(2)
	manifesto = messages.StringField(3)
	posted_by = messages.StringField(4)
	edited_by = messages.StringField(5)


class GetTopicRequest(messages.Message):

	key = messages.StringField(1)
	shortname = messages.StringField(2)


class TopicStatsRequest(messages.Message):

	pass


class TopicStatsResponse(messages.Message):

	pass


class ListTopicRequest(messages.Message):

	pass


class ListTopicResponse(messages.Message):

	topics = messages.MessageField(TopicResponse, 1, repeated=True)


class TopicVoteRequest(messages.Message):

	occupier = messages.StringField(1)
	topic = messages.StringField(2)


class TopicVoteResponse(messages.Message):

	key = messages.StringField(1)


class TopicSocialRequest(messages.Message):

	occupier = messages.StringField(1)
	subject = messages.StringField(2)


class StarTopicResponse(messages.Message):

	key = messages.StringField(1)


class CommentTopicResponse(messages.Message):

	key = messages.StringField(1)
	created = messages.StringField(2)	