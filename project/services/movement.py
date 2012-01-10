import logging

## movement API service
from project.services import RemoteService, remote
from project.messages import movement as messages

from project.models import ndb
from google.appengine.ext import ndb as nndb
from project.models.movement import Movement
from project.models.topic import Topic


class MovementService(RemoteService):

	@remote.method(messages.NewMovementRequest, messages.MovementResponse)
	def new(self, request):

		''' Creates new movement '''

		m = Movement.from_message(request, key=nndb.key.Key(Movement, request.shortname))

		m_key = m.put()

		response_obj = m.to_message()
		response_obj.key = m_key.urlsafe()
		return response_obj


	@remote.method(messages.GetMovementRequest, messages.MovementResponse)
	def get(self, request):

		''' Returns a movement '''

		if request.key is not None:
			m_key = Movement.Key(urlsafe=request.key)

		else:
			m_key = nndb.key.Key(Movement, request.shortname)
		
		m = m_key.get()

		return m.to_message()
		
	
	@remote.method(messages.MovementStatsRequest, messages.MovementStatsResponse)
	def stats(self, request):

		''' Returns stats about a movement '''

		pass
	
	@remote.method(messages.ListMovementRequest, messages.ListMovementResponse)
	def list(self, request):

		''' Lists movements '''

		response_obj = messages.ListMovementResponse()

		movement_query = Movement.query()
		movement_results = movement_query.fetch(25)

		if len(movement_results) > 0:
			movement_responses = []

			for movement in movement_results:
				movement_responses.append(movement.to_message())
			
		else:
			movement_responses = []

		response_obj.movements = movement_responses
		return response_obj


	@remote.method(messages.MovementSocialRequest, messages.StarMovementResponse)
	def star(self, request):

		''' Favorites a movement '''
		
		response_obj = messages.StarMovementResponse()

		s_key = nndb.key.Key(urlsafe=request.subject)
		o_key = nndb.key.Key(urlsafe=request.occupier)

		s = Star(nndb.key.Key(Star, request.occupier, parent=s_key))
		s.subject = s_key
		s.occupier = o_key

		response_obj.key = s.put().urlsafe()

		return response_obj
		
	@remote.method(messages.MovementSocialRequest, messages.CommentMovementResponse)
	def comment(self, request):
	
		''' Comments on a movement '''
		
		response_obj = messages.CommentMovementResponse()

		s_key = nndb.key.Key(urlsafe=request.subject)
		o_key = nndb.key.Key(urlsafe=request.occupier)

		s = Comment(nndb.key.Key(Comment, parent=s_key))
		s.subject = s_key
		s.occupier = o_key

		response_obj.key = s.put().urlsafe()
		response_obj.created = str(s.createdAt)

		return response_obj		