from project.models import OccupyModel, OccupyExpando


class AnalyzerModel(OccupyModel):

	''' Middleware model for Analyzer schema classes. '''

	pass


class AnalyzerExpando(OccupyModel):

	''' Middleware model for Analyzer schema-less classes. '''

	pass


class Timeperiod(AnalyzerModel):

	''' Represents a timeperiod which can contain summed values/stats/trends. Generated when analysis is performed. '''

	pass