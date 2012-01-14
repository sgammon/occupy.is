## Model classes
class Topic extends OccupyModel
class Occupier extends OccupyModel
class Movement extends OccupyModel
class Comment extends OccupyModel
class Star extends OccupyModel

## Collection classes
class KindCollection extends OccupyCollection
class ObjectCollection extends OccupyCollection


class ModelController extends OccupyController

	constructor: (occupy) ->

		@classes =
			Topic: Topic
			Occupier: Occupier
			Movement: Movement
			Comment: Comment
			Star: Star
		
		@index =
			
			by_key:
				_map: {}

				add: (key, index) ->
					@_map[key] = index

				find: (key) ->
					if key in @_map
						return @_map[key]
					else
						return false
				
			by_query: {}

		@state =
			last_error: null
			last_request: null
			last_response: null

		@objects =
			count: 0
			_data: {}
			_kind: {}


	register: (kind, key, object) ->

		$.apptools.dev.verbose 'Models', 'Registering model.', kind, key, object

		model = new @classes[kind](object)

		if not @objects._kind[kind].add([model])
			@objects._kind[kind] = new KindCollection(model: @classes[kind])

		index = @objects._kind[kind].add([model])
		@objects._data[key] = object

		@index.by_key.add(key, index)

	get: (key) ->
		return @objects._data[key]


## Export classes
if window?
	# Models
	window.Topic = Topic
	window.Occupier = Occupier
	window.Movement = Movement
	window.Comment = Comment
	window.Star = Star

	# Collections
	window.KindCollection = KindCollection
	window.ObjectCollection = ObjectCollection

	# Controller
	window.ModelController = ModelController