from project.models.indexer import IndexerModel, IndexerExpando


class IndexEntry(IndexerModel):

	''' Represents an entry in an index that is then mapped to matching resources. '''

	pass


class IndexEntryDescriptor(IndexerExpando):

	''' Represents arbitrary data annotating an IndexEntry. '''

	pass