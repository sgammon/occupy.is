from project.models.indexer import IndexerModel, IndexerExpando


class IndexMapping(IndexerModel):

	''' Represents a mapping between an IndexEntry and a resource. '''

	pass


class IndexMappingDescriptor(IndexerExpando):

	''' Represents arbitrary data annotating an IndexMapping. '''

	pass