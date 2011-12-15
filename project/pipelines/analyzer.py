from project.pipelines import OccupyPipeline


class AnalyzerPipeline(OccupyPipeline):
	
	''' Empty shell for analyzer pipeline. '''
	
	def run(self):
		pass


#### +=+=+=+ Analyzer Pipelines +=+=+=+ ####
class SocialAction(AnalyzerPipeline):
	
	''' Pipeline for social action (upvote, downvote like, etc.). '''
	
	def run(self):
		pass


class ContentAction(AnalyzerPipeline):
	
	''' Pipeline for created content like comments, messages, pictures etc. '''
	
	def run(self):
		pass







