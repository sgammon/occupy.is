(function() {
  var LandingPage, LandingRouter,
    __hasProp = Object.prototype.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor; child.__super__ = parent.prototype; return child; };

  LandingPage = (function(_super) {

    __extends(LandingPage, _super);

    function LandingPage(occupy) {}

    LandingPage.prototype.get_topic = function(ctx) {};

    LandingPage.prototype.post_topic = function(topic_name) {
      var callbacks, current_user, params, request;
      current_user = $.apptools.user.current_user['username'];
      params = {
        name: topic_name,
        shortname: (topic_name.replace(/[ ]/gi, "-")).toLowerCase()
      };
      if ((current_user != null) && (typeof current_user !== "undefined")) {
        params.posted_by = current_user;
      }
      callbacks = {
        success: function(object, response) {
          var rendered_stream;
          $.apptools.dev.verbose('TopicCreate', 'Successfully created topic.', object, response);
          response.id = request.id;
          response.topics = [response.topic];
          rendered_stream = Milk.render(document.getElementById('streamitem').innerHTML, response);
          return $('#streamcontainer').html(rendered_stream + document.getElementById('streamcontainer').innerHTML);
        },
        failure: function(error) {
          alert('There was an error creating your topic. Check the console.');
          return $.apptools.dev.error('TopicCreate', 'Failed to create new topic.', error);
        }
      };
      return request = Topic.new(params, callbacks);
    };

    LandingPage.prototype.list_topics = function() {
      var callbacks, request;
      callbacks = {
        success: function(object, response) {
          var rendered_stream;
          $.apptools.dev.verbose('TopicPull', 'Successfully pulled topics.', objects, response);
          response.id = request.id;
          rendered_stream = Milk.render(document.getElementById('streamitem').innerHTML, response);
          return $('#streamcontainer').html(rendered_stream);
        },
        failure: function(error) {
          alert('There was an error creating your topic. Check the console.');
          return $.apptools.dev.error('TopicCreate', 'Failed to create new topic.', error);
        }
      };
      return request = new Topic().list({}, callbacks);
    };

    return LandingPage;

  })(OccupyView);

  LandingRouter = (function(_super) {

    __extends(LandingRouter, _super);

    function LandingRouter(occupy) {}

    return LandingRouter;

  })(OccupyRouter);

}).call(this);
