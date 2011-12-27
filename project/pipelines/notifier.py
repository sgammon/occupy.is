from project.pipelines import OccupyPipeline
from google.appengine.api import xmpp
from google.appengine.ext import db
from google.appengine.api import channel
from google.appengine.api import mail




### +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ ###
### 		NotifierPipeline
### Inherits from: OccupyPipeline
### +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ ###
class NotifierPipeline(OccupyPipeline):
 	
	def run(self):
		pass


### +=+=+=+ EmailNotifier Pipelines +=+=+=+ ###
class SendEmail(NotifierPipeline):

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



class XmppSendPipeline(NotifierPipeline):

	''' Hook-in for XMPP notifications. '''
	
	def run(self, *args, **kwargs):

	     try:
		     ##Using Xmpp to send notification to user
		     send_to_user = xmpp.send_message(*args, **kwargs)

         ## Raises error if notification cannot send
		 except Exception, r:
		 	
		 	self.log.error('An error was encountered while trying to send an XMPP notification: '+str(r))
         
         ## Sends the notification 
		 return send_to_user
		 		


class ChannelSendPipeline(NotifierPipeline):

	''' Shell for Channel notifications (live user). '''

	def run(self, *args, **kwargs):
		
		try:
            ## Using channel to push notifications to user
            send_notification = channel.send_message(*args, **kwargs)
           
       ## Raises error if specified Client ID is malformed
        except InvalidChannelClientIdError, e:

        	self.log.error('An error was encountered while trying to establish a Channel: '+str(e)),
        
        ## Raises error if specified message is malformed       
        except InvalidMessageError, e:

            self.log.error('An error was encountered while trying to send Channel notification: '+str(eIME))

        finally:
        	try:
	        	if send_notification is None or isinstance(send_message, Exception):
	        		send_notification = False
	        except NameError, e:
	        	send_notification = False
       
        ## Pushes notification to user
        return send_notification




##Last edit by: Tyler Porras Tue. Dec. 27.2011 1:04pm
		## - built XmppSendPipeline, ChannelSendPipeline