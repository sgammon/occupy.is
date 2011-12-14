
class AppTools
	
	constructor: (window)  ->
		
		## Library Bridge
		@lib = {}

		## Async Loader
		@lib.modernizr = window.Modernizr
		
		@load = (fragment) =>
			return @lib.modernizr.load(fragment)

		## Backbone
		@lib.backbone = window.Backbone

		## Lawnchair
		@lib.lawnchair = window.Lawnchair

		## Dev Tools
		@dev = new CoreDevAPI(@)
		
		## Agent API
		@agent = new CoreAgentAPI(@)
		@agent.discover()
		
		## Events API
		@events = new CoreEventsAPI(@)

		# Register builtin events...
		@events.register 'PLATFORM_INIT'		
		@events.register 'PLATFORM_READY'
		
		## Users API
		@user = new CoreUserAPI(@)
		
		## RPC API
		@api = new CoreRPCAPI(@)
		
		## Live API
		@push = new CorePushAPI(@)

		return @


window.apptools = new AppTools(window)
if $?
	$.extend(apptools: window.apptools)