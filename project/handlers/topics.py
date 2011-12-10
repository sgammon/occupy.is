from project.handlers import OccupyHandler, OccupyFrameHandler


## +=+=+ Main Handler +=+=+ ##
class Topic(OccupyHandler):
	
	''' Topic page, with new/edit frames. '''

	pass


class Trends(OccupyHandler):

	''' Displays trends relating to a Topic, possibly in the scope of a Movement. '''

	pass


## +=+=+ Frame Handlers +=+=+ ##
class NewTopic(OccupyFrameHandler):
	pass


class EditTopic(OccupyFrameHandler):
	pass