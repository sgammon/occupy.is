# -*- coding: utf-8 -*-
"""

	###################################### Services configuration. ######################################


"""
config = {}

# Project Services
config['apptools.project.services'] = {

	'enabled': True, ## Disable API services system wide
	'logging': True, ## Logging for service request handling

	# Module-level (default) config (NOT IMPLEMENTED YET)
	'config': {
	
		'url_prefix': '/_api/rpc', ## Prefix for all service invocation URLs
	
	},

	# Installed API's
	'services': {
	

		## Topic API Service
		'topic': {
			'enabled': False,
			'service': 'project.services.topic.TopicService',
			'methods': ['new', 'get', 'stats', 'list', 'upvote', 'downvote', 'star', 'comment'],
			
			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'
			}

		},


		## Movement API Service
		'movement': {
			'enabled': False,
			'methods': ['new', 'get', 'stats', 'list', 'star', 'comment'],
		},


		## Occupier API Service
		'occupier': {
			'enabled': False,
			'methods': ['new', 'get', 'avatar', 'message'],
		},


		## Search API Service
		'search': {
			'enabled': False,
			'methods': ['autocomplete', 'quicksearch', 'fullsearch'],
		},


		## Social API Service
		'social': {
			'enabled': False,
			'methods': ['notifications', 'alerts'],
		},


		## Authorization/Authentication API Service
		'auth': {
			'enabled': False,
			'methods': ['login', 'logout', 'connect'],
		},


		## Feed API Service
		'feed': {
			'enabled': False,
			'methods': ['main', 'movement', 'topic', 'occupier']
		}

		
	} ## End services

} ## End services


## Global Services
config['apptools.services'] = {

	'logging': True,

	'hooks': {
		'appstats': {'enabled': False}, ## RPC profiling
		'apptrace': {'enabled': False}, ## memory usage profiling
		'profiler': {'enabled': False} ## CPU usage profiling
	},

	'middleware': [

		('authentication', {
		
			## Configuration for authentication middleware
		
			'enabled': False,
			'debug': False,
			'path': 'apptools.middleware.AuthenticationMiddleware',
			'args': {
			
			}
		
		}),
		
		('monitoring', {
		
			## Configuration for monitoring middleware
		
			'enabled': False,
			'debug': False,
			'path': 'apptools.middleware.MonitoringMiddleware',
			'args': {
			
			}			
		
		}),
		
		('authorization', {
		
			## Configuration for authorization middleware
		
			'enabled': False,
			'debug': False,
			'path': 'apptools.middleware.AuthorizationMiddleware',
			'args': {
			
			}			
		
		}),
		
		('caching', {
		
			## Configuration for caching middleware
		
			'enabled': False,
			'debug': False,
			'path': 'apptools.middleware.CachingMiddleware',
			'args': {
			
			}
		
		})

	],
	
	## Configuration profiles that can be assigned to services
	'middleware_config': {
	
		## Response + data caching middleware
		'caching': {
		
			'profiles': {
			
				## No caching
				'none': {
					
					'localize': False,					
					'default_ttl': 1, ## Default Time-to-Live for cached items
					
					'activate': {
						'local': False, ## Local browser-side caching, if supported
						'request': False, ## Caching of full API responses by hashed API requests
						'internal': False ## Caching inside the remote service object
					}
				
				},
			
			
				## Cache things as they are pulled/used by clients
				'lazy': {
					
					'localize': False,
					'default_ttl': 60,
				
					'activate': {
						'local': False,
						'request': True,
						'internal': True
					},

				},
				
				## Cache things as they are used, but set low timeouts to avoid stale data
				'safe': {
				
					'localize': False,
					'default_ttl': 60,
					
					'activate': {
						'local': False,
						'request': False,
						'internal': True
					}
				
				},
				
				## Cache things before they are accessed, predictively, and with long timeouts
				'aggressive': {

					'localize': False,				
					'default_ttl': 120,
					
					'activate': {
						'local': True,
						'request': True,
						'internal': True
					}
				
				}
			
			},
			
			'default_profile': 'none' ## Default caching profile for APIs that don't specify one
		
		},
		
		## Security and permissions enforcement middleware
		'security': {
			
			'profiles': {
			
				## APIs with no security features
				'none': {
				
					'expose': 'all', ## Whether to expose existence of this API to javascript clients
					
					## Client authentication
					'authentication': {
						'enabled': False
					},
					
					## Client authorization
					'authorization': {
						'enabled': False
					}
				
				},
				
				## APIs marked public
				'public': {
				
					'expose': 'all',
					
					'authentication': {
						'enabled': False,
						'mode': None
					},
					
					'authorization': {
						'enabled': False,
						'mode': None
					}
				
				},
				
				## APIs marked private
				'private': {
				
					'expose': 'admin',
					
					'authentication': {
						'enabled': False,
						'mode': None
					},
					
					'authorization': {
						'enabled': False,
						'mode': None
					}
				
				}
			
			},
			
			'default_profile': 'public'
		
		},
		
		## Recording and logging middleware
		'recording': {
		
			'profiles': {
			
				'none': {
					'mode': None
				},
				
				'minimal': {
					'mode': None
				},
				
				'full': {
					'mode': None
				},
				
				'debug': {
					'mode': None
				}
			
			},
		
		},
	
	},
	
	### Default config values
	'defaults': {
	
		'module': {},
		'service': {
		
			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'
			},
			
			'args': {
			
			}
		
		}
	
	},

}