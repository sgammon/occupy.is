from project.pipelines import OccupyPipeline

from google.appengine.api import mail

### +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ ###
### 		NotifierPipeline
### Inherits from: OccupyPipeline
### +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ ###
class NotifierPipeline(OccupyPipeline):
 	
	def run(self):
		pass


### +=+=+=+ EmailNotifier Pipelines +=+=+=+ ###
class SendEmail(EmailNotifier):

	''' A pipeline that can send email. '''

	def run(self, **kwargs):
		
		try:
			## Message is the compiled email and returning result will send the email
			message = mail.EmailMessage(**kwargs)
			result = message.send()
			
		## Raises an error if the message cannot send	
		except Exception, e:
			
			self.log.error('An error was encountered trying to send an email: '+str(e))
		
		## sends the message
		return result



class XmppPipeline(NotifierPipeline):

	''' Hook-in for XMPP notifications. '''
	
	def run(self):
		pass


class ChannelsPipeline(NotifierPipeline):

	''' Shell for Channel notifications (live user). '''

	def run(self):
		pass