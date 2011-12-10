# -*- coding: utf-8 -*-

## AppTools Imports
from apptools.core import BaseHandler
import logging


class WebHandler(BaseHandler):
	
	''' Handler for desktop web requests. '''

	pass
	
	
class MobileHandler(BaseHandler):
	
	''' Handler for mobile web requests. '''

	pass


## +=+=+ Occupy Handlers +=+=+ ##
class OccupyHandler(WebHandler):
	
	''' Handler for everything Occupy :). '''

	pass


class OccupyFrameHandler(OccupyHandler):

	''' Handler for frames pulled into lightboxes. '''

	pass