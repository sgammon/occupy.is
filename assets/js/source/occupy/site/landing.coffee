

class LandingPage extends OccupyView

    constructor: (occupy) ->


    get_topic: (ctx) ->


    post_topic: (topic_name) ->

        current_user = $.apptools.user.current_user['username']

        params =

            name: topic_name
            shortname: (topic_name.replace /\s/g, "-").toLowerCase()

        params.posted_by = current_user if (current_user? and (typeof current_user != "undefined"))

        callbacks =

            success: (object, response) ->

                $.apptools.dev.verbose('TopicCreate','Successfully created topic.', object, response)
                response.id = request.id
                response.topics = [response.topic]
                rendered_stream = Milk.render(document.getElementById('streamitem').innerHTML, response)

                $('#streamcontainer').html(rendered_stream+document.getElementById('streamcontainer').innerHTML)

            failure: (error) ->

                alert('There was an error creating your topic. Check the console.')
                $.apptools.dev.error('TopicCreate', 'Failed to create new topic.', error)
        
        request = `Topic.new(params, callbacks)`
    
    list_topics: () ->

        callbacks = 

            success: (object, response) ->

                $.apptools.dev.verbose('TopicPull', 'Successfully pulled topics.', objects, response)
                response.id = request.id
                rendered_stream = Milk.render(document.getElementById('streamitem').innerHTML, response);
                $('#streamcontainer').html(rendered_stream)

            failure: (error) ->

                alert('There was an error creating your topic. Check the console.')
                $.apptools.dev.error('TopicCreate', 'Failed to create new topic.', error)
        
        request = new Topic().list({}, callbacks)

        

class LandingRouter extends OccupyRouter

    constructor: (occupy) ->