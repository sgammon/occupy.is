from apptools.model import BaseModel, ndb


class ModelMixin(BaseModel):

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

	pass


class SimpleStructConverterMixin(ModelMixin):

	''' Mixin class for automagically generating a ProtoRPC Message class from a model. '''

	pass