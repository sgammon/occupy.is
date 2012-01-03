from project.pipelines import OccupyPipeline


class AnalyzerPipeline(OccupyPipeline):
	
	''' Empty shell for analyzer pipeline. '''
	
	def run(self):
		pass


#### +=+=+=+ Analyzer Pipelines +=+=+=+ ####
class SocialActionPipeline(AnalyzerPipeline):
	
	''' Pipeline for social action (upvote, downvote, like, etc.). '''
	
	def run(self):
		pass



class ContentActionPipeline(AnalyzerPipeline):
	
	''' Pipeline for created content like comments, messages, pictures etc. '''
	
	def run(self):
		pass



class TopicCounter(ContentActionPipeline):

	''' Pipeline used for counting topics '''

	def run(self):
		pass



class CommentCounter(ContentActionPipeline):

	''' Pipeline used for counting posted comments per topic. '''

	def run(self):
		pass



class StarCounter(ContentActionPipeline):

    ''' Pipeline used for counting stars on comments and topics. '''

    def run(self):
    	pass



class VoteCounter(ContentActionPipeline):

    ''' Pipeline for up/down votes on topics AND comments, per topic and comment. '''

	def run(self):
		pass








