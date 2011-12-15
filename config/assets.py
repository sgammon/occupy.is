# -*- coding: utf-8 -*-
"""

	###################################### Asset configuration. ######################################


"""
config = {}


# Installed Assets
config['apptools.project.assets'] = {

	'debug': False, ## Output log messages about what's going on.
	'verbose': False, ## Raise debug-level messages to 'info'.

	# JavaScript Libraries & Includes
	'js': {


		### Core Dependencies ###
		('core', 'core'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'dependencies.bundle.min.js'
			},
			
			'assets': {
				'backbone': {'min': True, 'version': '0.5.1'}, # Backbone.JS - site MVC core
				'amplify': {'min': True, 'version': '1.0.0'}, # AmplifyJS - for request, local storage + pubsub management
				'modernizr': {'min': True, 'version': '2.0'}, # Modernizr - browser polyfill + compatibility testing
				'lawnchair': {'version': '0.6.3'}, # Lawnchair: Client-side persistent storage
				'underscore': {'min': True, 'version': '1.2.3'} # Underscore: the functional side of javascript
			}
		
		},
		
		### FatCatMap Platform Scripts ###
		('apptools', 'apptools'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'core.bundle.min.js'
			},

			'assets': {
				'base': {'min': True, 'version': 0.1} # milk (mustasche for coffee), _underscore, _root
			}
	
		},
		
		### jQuery Core & Plugins ###
		('jquery', 'core'): { 
		
			'config': {
				'version_mode': 'getvar',				
				'bundle': 'jquery.bundle.min.js'
			},
			
			'assets': {
				'core': {'name': 'jquery', 'min': True, 'version': '1.6.1'}, # jQuery Core
				'easing': {'path': 'interaction/easing.min.js'}, # Easing transitions for smoother animations
				'mousewheel': {'path': 'interaction/mousewheel.min.js'} # jQuery plugin for mousewheel events + interactions
			}
			
		},
		
		'belated_png': {'path': 'util/dd_belatedpng.js'}, # Belated PNG fix

		### Occupy Scripts ###
		('occupy', 'occupy'): {
			
			'config': {
				'version_mode': 'getvar',
				'bundle': 'occupy.bundle.min.js'
			},

			'assets': {
				'app': {'min': True, 'version': '0.0.1'} # main occupy.js
			}

		},

		### Site Scripts ###
		('site', 'occupy/site'): {
			
			'config': {
				'version_mode': 'getvar',
				'bundle': 'site.bundle.min.js'
			},

			'assets': {
				'landing': {'min': True, 'version': '0.0.1'},
				'topic': {'min': True, 'version': '0.0.1'},
				'occupier': {'min': True, 'version': '0.0.1'},
				'movement': {'min': True, 'version': '0.0.1'}
			}

		}
	
	},


	# Cascading Style Sheets
	'style': {
		
		# Main Stylesheets
		('compiled', 'compiled'): {
		
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},
		
			'assets': {
				'main': {'version': 0.2}, # reset, main
				'ie': {'version': 0.1}, # fixes for internet explorer (grrr...)
				'print': {'version': 0.1} # proper format for printing
			}
		
		},
		
		# Site-Specific Stylesheets
		('occupy', 'compiled/occupy'): {
		
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'app': {'version': 0.2}, # the app's css - layout/main/social/etc
			}
		
		},

		# Content Section-Specific Stylesheets
		('site', 'compiled/occupy/site'): {
			
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},

			'assets': {
				'landing': {'version': 0.2},
				'topic': {'version': 0.1},
				'occupier': {'version': 0.1},
				'movement': {'version': 0.1}
			}

		}
			
	},

	
	# Other Assets
	'ext': {
	 },
	
}