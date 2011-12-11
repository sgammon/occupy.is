from project.models.analyzer import AnalyzerModel, AnalyzerExpando


class SummedValue(AnalyzerModel):

	''' Storage of summed values, usually under a timeseries. '''

	pass


class CalculatedValue(AnalyzerModel):

	''' Storage of calculated values, from summed values and other calculated values, usually under a timeseries. '''

	pass