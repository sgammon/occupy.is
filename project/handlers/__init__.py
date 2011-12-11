# -*- coding: utf-8 -*-

## AppTools Imports
from apptools.core import BaseHandler
import logging


class WebHandler(BaseHandler):
	
	''' Handler for desktop web requests. '''

	def get(self, *args, **kwargs):

		from google.appengine.api import backends

		self.response.write('<b>default occupy handler sez:</b><br />')
		self.response.write('- hello my name is <b>'+str(self.__class__.__name__)+'</b><br />')
		self.response.write('- i hail from the package <b>'+str(self.__class__.__module__)+'</b><br />')
		self.response.write('- i can see your nametag says your name is <b>'+str(self.request.environ.get('REMOTE_ADDR', 'missing. [wtf that\'s weird.]'))+'</b><br />')

		## template path
		if hasattr(self, 'template'):
			self.response.write('- i currently <b><span style="color: green">do</span></b> have a configured template path<br />')
		else:
			self.response.write('- i currently <b><span style="color: red">do not</span></b> have a configured template path<br />')

		## runtime environment
		self.response.write('<br /><b>runtime environment:</b><br />')
		self.response.write('- currently running on the "'+str(self.request.environ.get('APPENGINE_RUNTIME', 'python25'))+'" runtime<br />')
		
		if self.request.environ.get('wsgi.version') is not None:
			self.response.write('- this request <span style="color: green"><b>was served via WSGI</b></span><br />')
			if self.request.environ.get('wsgi.multiprocess') == True:
				self.response.write('- also, <span style="color: green"><b>multiprocess is enabled!</b></span><br />')
			else:
				self.response.write('- it looks like <span style="color: orange"><b>multiprocess is disabled.</b></span><br />')
			if self.request.environ.get('wsgi.multithread') == True:
				self.response.write('- in addition, <span style="color: green"><b>multithreading is enabled!</b></span><br />')
			else:
				self.response.write('- it looks like <span style="color: orange"><b>multithreading is disabled.</b></span><br />')
		else:
			self.response.write('<br />- this request <span style="color: red"<b>was served via CGI</b></span><br />')
			self.response.write('- of course, you know this means <span style="color: red"><b>no multithreading</b></span><br />')
			self.response.write('- and also, <span style="color: red"><b>no multithreading.</b></span><br />')

		
		## request environment
		self.response.write('<br /><b>request environment:</b><br />')
		self.response.write('- this request served by instance ID "'+str(self.request.environ.get('INSTANCE_ID', '[none]'))+'"<br />')
		if backends.get_backend() is not None:
			self.response.write('- this request was served from a <b>backend</b>, at ID "'+str(backends.get_backend())+'"')
			self.response.write('- the hostname for this instance of this backend is: '+str(backends.get_hostname(backend=backends.get_backend(), instance=backends.get_instance()))+'<br />')
			self.response.write('- here\'s an SSL-secured link to this <a href='+backends.get_url(backend=backends.get_backend(), instance=backends.get_instance(), protocol='https')+'>instance</a>, and this <a href='+backends.get_url(backend=backends.get_backend(), instance=None, protocol='https')+'>backend</a><br />')
		else:
			self.response.write('- this request was served by a frontend instance.<br />')

		## args
		if len(args) > 0:
			self.response.write('<br /><b>someone passed me some args:</b><br />')
			for index, arg in enumerate(args):
				self.response.write('- at position '+str(index)+', the value: '+str(arg)+'<br />')
			self.response.write('<b>and that\'s all.</b><br />')
		
		## kwargs
		if len(kwargs) > 0:
			self.response.write('<br /><b>someone passed me some kwargs:</b><br />')
			for k, v in kwargs.items():
				self.response.write('- at key '+str(k)+', the value: '+str(v)+'<br />')
			self.response.write('<b>and that\'s all.</b><br />')

		self.response.write('<br /><b>k thats all thanks bye</b>')

		return

	
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