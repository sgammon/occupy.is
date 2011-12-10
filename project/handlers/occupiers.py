from project.handlers import OccupyHandler, OccupyFrameHandler


## +=+=+ Main Handler +=+=+ ##
class Occupier(OccupyHandler):
	
	''' User profile page, with signup/edit/post frames. '''

	pass


class Occupiers(OccupyHandler):

	''' General sum-up page for fanning-in occupier data. '''

	pass


## +=+=+ Frame Handlers +=+=+ ##
class NewOccupier(OccupyFrameHandler):
	pass


class EditOccupier(OccupyFrameHandler):
	pass


class PostToOccupier(OccupyFrameHandler):
	pass