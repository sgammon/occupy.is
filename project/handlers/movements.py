from project.handlers import OccupyHandler, OccupyFrameHandler


## +=+=+ Main Handlers +=+=+ ##
class Movement(OccupyHandler):
	
	''' Movement page, with new/edit frames. '''

	pass


class Trends(OccupyHandler):

	''' Shows trending topics, users, comments, etc for a Movement. '''

	pass


class Members(OccupyHandler):

	''' Shows a listing of active members that have indicated they are part of this Movement. '''

	pass


## +=+=+ Frame Handlers +=+=+ ##
class NewMovement(OccupyFrameHandler):
	pass


class EditMovement(OccupyFrameHandler):
	pass