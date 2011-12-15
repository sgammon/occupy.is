## occupier API service
from project.services import RemoteService, remote
from project.messages import occupier as messages


class OccupierService(RemoteService):

	@remote.method(messages.NewOccupierRequest, messages.NewOccupierResponse)
	def new(self, request):

		''' request for new occupier '''

		pass

	@remote.method(messages.GetOccupierRequest, messages.GetOccupierResponse)
	def get(self, request):

		''' get an occupier entity? '''

		pass

	@remote.method(messages.OccupierAvatarRequest, messages.OccupierAvatarResponse)
	def avatar(self, request):

		''' assign/retrieve avatar for occupier '''

		pass

	@remote.method(messages.MessageOccupierRequest, messages.MessageOccupierResponse)
	def message(self, request):

		''' message an occupier '''

		pass