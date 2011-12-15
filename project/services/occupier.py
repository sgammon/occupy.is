## occupier API service
from project.services import RemoteService, remote
from project.messages import occupier as messages


class OccupierService(RemoteService):

	@remote.method(messages.NewOccupierRequest, messages.NewOccupierResponse)
	def new(self, request):

		''' Creates new Occupier (user) '''

		pass

	@remote.method(messages.GetOccupierRequest, messages.GetOccupierResponse)
	def get(self, request):

		''' Returns an occupier '''

		pass

	@remote.method(messages.OccupierAvatarRequest, messages.OccupierAvatarResponse)
	def avatar(self, request):

		''' Returns an occupier's avatar '''

		pass

	@remote.method(messages.MessageOccupierRequest, messages.MessageOccupierResponse)
	def message(self, request):

		''' Sends a private message to an occupier '''

		pass