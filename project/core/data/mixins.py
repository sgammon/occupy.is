import logging
from apptools.model import NDBModel, ndb
from google.appengine.ext import ndb as nndb

class ModelMixin(object):

	''' Base mixin class. '''

	def kind(self):
		return '__mixin__'


#### +=+=+=+ Audit Mixins +=+=+=+ ####
class CreatedModifiedMixin(ModelMixin):

	''' Keeps track of modified/created times. '''

	createdAt = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
	modifiedAt = ndb.DateTimeProperty(auto_now=True, indexed=True)


class UserAuditMixin(ModelMixin):

	''' Keeps track of modified/created times. '''

	createdBy = ndb.UserProperty()
	modifiedBy = ndb.UserProperty()


#### +=+=+=+ Backend Processing Mixins +=+=+=+ ####
class IndexerMixin(ModelMixin):
	
	''' Functionality-only mixin for specifying indexer config for a model (and implicitly enabling app-level indexing). '''

	pass


class AnalysisMixin(ModelMixin):

	''' Functionality-only mixin for specifying count/sum/calculated property config for a model (and implicitly enabling app-level analysis). '''

	pass


#### +=+=+=+ Service Layer Mixins +=+=+=+ ####
class MessageConverterMixin(ModelMixin):

	''' Mixin class for automagically generating a ProtoRPC Message class from a model. '''

	def to_message(self, include=None, exclude=None):
		response = self._message_class()

		if self.key is not None:
			response.key = self.key.urlsafe()
		else:
			response.key = None

		for k, v in self.to_dict(include=include, exclude=exclude).items():
			if hasattr(response, k):
				setattr(response, k, v)

		return response

	@classmethod
	def from_message(cls, message, key=None, **kwargs):

		if hasattr(message, 'key') and key is None:
			obj = cls(key=nndb.key.Key(urlsafe=message.key), **kwargs)
		elif key is not None and isinstance(key, nndb.key.Key):
			obj = cls(key=nndb.key.Key(urlsafe=key.urlsafe()), **kwargs)
		elif key is not None and isinstance(key, basestring):
			obj = cls(key=nndb.key.Key(urlsafe=key), **kwargs)
		else:
			obj = cls(**kwargs)

		for k, v in cls._properties.items():
			if k == 'key':
				continue
			if hasattr(message, k):
				try:
					setattr(obj, str(k), getattr(message, k))

				except TypeError:
					if k is not None and k not in [False, True, '']:

						try:
							setattr(obj, str(k), str(getattr(message, k)))
						except TypeError:
							continue
					
				else:
					continue

		
		return obj



class SimpleStructConverterMixin(ModelMixin):

	''' Mixin class for automagically generating a ProtoRPC Message class from a model. '''

	pass