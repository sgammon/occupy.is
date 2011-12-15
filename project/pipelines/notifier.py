from project.pipelines import OccupyPipeline
### +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ ###
### 		NotifierPipeline
### Inherits from: OccupyPipeline
### +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ ###
class NotifierPipeline(OccupyPipeline):
 	
	def run(self):
		pass


#### +=+=+=+ Notifier Pipelines +=+=+=+ ####
class EmailNotifier(NotifierPipeline):
	
	''' Shell for email notifications. '''
	
	def run(self):
		pass


class XmppPipeline(NotifierPipeline):

	''' Hook-in for XMPP notifications. '''
	
	def run(self):
		pass


class ChannelsPipeline(NotifierPipeline):

	''' Shell for Channel notifications (live user). '''

	def run(self):
		pass