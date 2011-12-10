from project.handlers import WebHandler


class Landing(WebHandler):
	
	''' occupy.is main page :) '''
	
	def get(self):
		self.render('main/landing/frame.html')