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
				'amplify': {'min': True, 'version': '1.1.0'}, # AmplifyJS - for request, local storage + pubsub management
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
		('jquery', 'jquery'): { 
		
			'config': {
				'version_mode': 'getvar',				
				'bundle': 'jquery.bundle.min.js'
			},
			
			'assets': {
				'core': {'name': 'jquery', 'min': True, 'version': '1.6.1'}, # jQuery Core
				'easing': {'path': 'ui/jquery.easing.min.js'}, # Easing transitions for smoother animations
				'mousewheel': {'path': 'ui/jquery.mousewheel.min.js'} # jQuery plugin for mousewheel events + interactions
			}
			
		},

		('plugins', 'plugins'): {
			
			'config': {
				'version_mode': 'getvar',
				'bundle': 'plugins.bundle.min.js'
			},

			'assets': {
				'jquery.fancybox': {'min': True, 'version': '1.3.4'}, # Fancybox plugin for lightbox dialogues
				'jquery.tipsy': {'min': True, 'version': '1.0.0a'}, # Tipsy tooltips
				'jquery.leanmodal': {'min': True, 'version': 1.0}, # leanModal plugin for modal dialogues
				'jquery.isotope': {'min': True, 'version': '1.5.06'}, # Isotope fluid layout plugin
				'jquery.jcrop': {'min': True, 'version': '0.9.9'} # Jcrop image crop/resize plugin
			}
		},

		### Plupload Plugin ###
		('plupload', 'plugins/plupload'): {
			
			'config': {
				'version_mode': 'getvar',
				'bundle': 'plupload.bundle.min.js'
			}, 

			'assets': {
				'plupload': {'min': True, 'version': '1.5.2'}, # Plupload main script
				'queue.jquery': {'min': True, 'version': '1.5.2'}, # Upload queue for plain jQuery
				'queue.jqui': {'min': True, 'version': '1.5.2'}, # Upload queue for jQuery UI
				'runtime.browserplus': {'min': True, 'version': '1.5.2'}, # Yahoo BrowserPlus runtime
				'runtime.flash': {'min': True, 'version': '1.5.2'}, # Adobe Flash runtime
				'runtime.gears': {'min': True, 'version': '1.5.2'}, # Google Gears runtime
				'runtime.html4': {'min': True, 'version': '1.5.2'}, # HTML4
				'runtime.html5': {'min': True, 'version': '1.5.2'}, # HTML5
				'runtime.silverlight': {'min': True, 'version': '1.5.2'}, # Microsoft Silverlight

			}
		}
		
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

		},

		# Plugin-Specific Stylesheets
		('plugins', 'plugins'): {
			
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},

			'assets': {
				'fancybox': {'version': '1.3.4'},
				'tipsy': {'version': '1.0.0a'}, 
				'jcrop': {'version': '0.9.9'}
			}
		}, 

		# Plupload Stylesheets
		('plupload', 'plugins/plupload'): {
			
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},

			'assets': {
				'jquery': {'version': '1.5.2'}, # Base stylesheet
				'jqui': {'version': '1.5.2'} # jQuery UI stylesheet
			}
		}
			
	},

	
	# Other Assets
	'ext': {
	 },
	
}