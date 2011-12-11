from project.models import OccupyModel, OccupyExpando


class IndexerModel(OccupyModel):

	''' Middleware model for Indexer schema classes. '''

	pass


class IndexerExpando(OccupyExpando):

	''' Middleware model for Indexer schema-less classes. '''

	pass