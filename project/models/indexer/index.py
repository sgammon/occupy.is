from project.models.indexer import IndexerModel, IndexerExpando


class Index(IndexerModel):

	''' Represents an app-generated index on a certain model>property. '''

	pass


class IndexDescriptor(IndexerExpando):

	''' Represents arbitrary data annotating an Index. '''

	pass