import logging

## occupier API service
from project.services import RemoteService, remote
from project.messages import occupier as messages

from project.models import ndb, occupier
from google.appengine.ext import ndb as nndb


class OccupierService(RemoteService):

	@remote.method(messages.NewOccupierRequest, messages.OccupierResponse)
	def new(self, request):

		''' Creates new Occupier (user) '''

		o = Occupier.from_message(request, key=nndb.key.Key(Occupier, request.username))
		
		o_key = o.put()

		response_obj = o.to_message()
		response_obj.key = o_key.urlsafe()
		return response_obj

	@remote.method(messages.GetOccupierRequest, messages.OccupierResponse)
	def get(self, request):

		''' Returns an occupier '''

		if request.key is not None:
			o_key = Occupier.Key(urlsafe=request.key)
		
		else:
			o_key= nndb.key.Key(Occupier, request.username)
		
		o = o_key.get()

		return o.to_message()

	@remote.method(messages.OccupierAvatarRequest, messages.OccupierAvatarResponse)
	def avatar(self, request):

		''' Returns an occupier's avatar '''

		pass

	@remote.method(messages.MessageOccupierRequest, messages.MessageOccupierResponse)
	def message(self, request):

		''' Sends a private message to an occupier '''

		pass