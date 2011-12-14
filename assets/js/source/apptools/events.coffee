

class CoreEventsAPI extends CoreAPI

	constructor: (apptools) ->

		@registry = []
		@callchain = {}
		@history = []
	
		@trigger = (event, args...) =>
		
			$.apptools.dev.verbose 'Events', 'Triggered event: ', event, args, @callchain[event]
		
			if event in @registry
				
				hook_exec_count = 0
				hook_error_count = 0
				
				for callback_directive in @callchain[event].hooks
					try
						if callback_directive.once == true and callback_directive.has_run == true
							continue
						else
							result = callback_directive.fn(args...)
							hook_exec_count++
							@history.push event: event, callback: callback_directive, args: args, result: result
							callback_directive.has_run = true
					catch error
						hook_error_count++
						@history.push event: event, callback: callback_directive, args: args, error: error
				
				return executed: hook_exec_count, errors: hook_error_count
			else
				return false
		
		@register = (name) =>
			
			@registry.push(name)
			@callchain[name] =
				hooks: []
			apptools.dev.verbose 'Events', 'Registered event: ', name
			return true
		
		@hook = (event, callback, once=false) =>
			
			if event not in @registry
				@register(event)
			@callchain[event].hooks.push(fn: callback, once: once, has_run: false)
			apptools.dev.verbose 'Events', 'Hook registered on event: ', event
			return true
		
			