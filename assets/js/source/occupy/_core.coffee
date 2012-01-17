class OccupyController

class OccupyView extends Backbone.View

class OccupyModel extends Backbone.Model

	constructor: (object, register=true) ->
		
		@kind = @__proto__.constructor.name
		super object

		if object?.key? and register
			@register(key)
		return @

	register: (key) ->
		$.apptools.dev.verbose('ModelRegistry', 'Registering model.', @__proto__.constructor.name, @)
		$.occupy.models.register(@kind, key, @)
		return

	_parseListResponse: (response) ->
		records = response[@kind.toLowerCase()+'s']
		$.apptools.dev.verbose('OccupyModel', 'Parsing "list" response.', response, @kind.toLowerCase()+'s')
		models = []
		for record in records
			$.apptools.dev.verbose('OccupyModel', 'Making object.', record)
			object = @_makeObject(record)
			$.apptools.dev.verbose('OccupyModel', 'Made object.', object)
			models.push(object)

		return models

	_makeObject: (object) ->
		object = @__proto__.constructor(object, true)
		return object

	list: (params, callbacks) ->
		request = $.apptools.api[@kind.toLowerCase()].list(params)

		injected_callbacks =
			success: (response) =>
				objects = @_parseListResponse(response)
				if callbacks?.success?
					callbacks.success(objects, response)
			
			failure: (error) =>
				$.apptools.dev.error('ModelList', 'Error encountered listing models of kind "'+@kind+'".', params, request, @)
				if callbacks?.failure?
					callbacks.failure(error)

		return request.fulfill(injected_callbacks)

	get: (params, callbacks) ->
		request = $.apptools.api[@kind.toLowerCase()].get(params)

		injected_callbacks =
			success: (response) =>
				object = @_makeObject(response[@kind.toLowerCase()])
				if callbacks?.success?
					callbacks.success(object, response)
			
			failure: (error) =>
				$.apptools.dev.error('ModelGet', 'Error encountered getting model of kind "'+@kind+'".', params, request, @)
				if callbacks?.failure?
					callbacks.failure(error)

		return request.fulfill(injected_callbacks)

	new: (params, callbacks) ->
		request = $.apptools.api[@kind.toLowerCase()].new(params)

		injected_callbacks =
			success: (response) =>
				object = @_makeObject(response)
				if callbacks?.success?
					callbacks.success(object, response)
			
			failure: (error) =>
				$.apptools.dev.error('ModelNew', 'Error encountered creating model of kind "'+@kind+'".', params, request, @)
				if callbacks?.failure?
					callbacks.failure(error)

		return request.fulfill(injected_callbacks)


class OccupyRouter extends Backbone.Router

class OccupyCollection extends Backbone.Collection

if window?
	window.OccupyController = OccupyController
	window.OccupyView = OccupyView
	window.OccupyModel = OccupyModel
	window.OccupyRouter = OccupyRouter
	window.OccupyCollection = OccupyCollection