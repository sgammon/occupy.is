
class Occupy
	
	constructor: (@config)  ->
		
		@upload = new UploadController(@)
		@workers = new WorkerController(@)
		@realtime = new RealtimeController(@)
		
		@feed = new FeedController(@)
		@social = new SocialController(@)
		@models = new ModelController(@)
				
		return @


window.occupy = new Occupy()
if $?
	$.extend(occupy: window.occupy)