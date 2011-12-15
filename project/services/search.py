## search API service
from project.services import RemoteService, remote
from project.messages import search as messages


class SearchService(RemoteService):

	@remote.method(messages.AutocompleteRequest, messages.AutocompleteResponse)
	def autocomplete(self, request):

		''' Autocompletes partially-entered search terms '''

		pass

	@remote.method(messages.QuicksearchRequest, messages.QuicksearchResponse)
	def quicksearch(self, request):

		''' Does a quicksearch'''

		pass

	@remote.method(messages.FullsearchRequest, messages.FullsearchResponse)
	def fullsearch(self, request):

		''' Full-text search '''

		pass