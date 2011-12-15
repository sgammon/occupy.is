

class CorePushAPI extends CoreAPI

	constructor: (apptools) ->

		## Register events
		apptools.events.register 'SOCKET_OPEN'
		apptools.events.register 'SOCKET_CLOSE'
		apptools.events.register 'SOCKET_ACTIVITY'
		apptools.events.register 'SOCKET_EXPECT'
		apptools.events.register 'SOCKET_MESSAGE'
		apptools.events.register 'SOCKET_ERROR'

		## Connect/disconnect/expect
		@connect = () ->
		@disconnect = () ->
		@expect = (request) ->

		## Config/state
		@state =
			token: null
			socket: null
			channel: null
			
			activity:
				expecting: {}
				complete: {}
				error: {}

		## Socket handles, + fn
		@socket =
			
			establish: () ->
			register: () ->

		## Socket event callbacks
		@events =
			
			open: () ->
			message: () ->
			error: () ->
			close: () ->