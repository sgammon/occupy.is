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

	''' Frame that contains a form to create a new Occupier. '''

	pass


class EditOccupier(OccupyFrameHandler):

	''' Frame that contains a form to edit an existing Occupier. '''

	pass


class PostToOccupier(OccupyFrameHandler):

	''' Frame that contains a form to post a message to an Occupier. '''

	pass