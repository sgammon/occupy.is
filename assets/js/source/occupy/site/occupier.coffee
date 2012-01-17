

class OccupierPage extends OccupyView

	constructor: (occupy) ->


	get_topics: (ctx) ->


	post_topic: (topic_name) ->

		 post_topic: (topic_name) ->

        current_user = $.apptools.user.current_user['username']

        params =

            name: topic_name
            shortname: (topic_name.replace /\s/g, "-").toLowerCase()

        params.posted_by = current_user if (current_user? and (typeof current_user != "undefined"))

        callbacks =

            success: (object, response) ->


            failure: (error) ->

                    
        request = `Topic.new(params, callbacks)`
    
    list_topics: () ->

        callbacks = 

            success: (object, response) ->

                
            failure: (error) ->

                        
        request = new Topic().list({}, callbacks)



class OccupierRouter extends OccupyRouter

	constructor: (occupy) ->