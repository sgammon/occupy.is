## social API service
from project.services import RemoteService, remote
from project.messages import social as messages


class SocialService(RemoteService):

	@remote.method(messages.NotificationsRequest, messages.NotificationsResponse)
	def notifications(self, request):

		''' site notification '''

		pass

	@remote.method(messages.AlertsRequest, messages.AlertsResponse)
	def alerts(self, request):

		''' site alerts '''

		pass