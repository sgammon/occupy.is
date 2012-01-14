(function() {
  var TopicPage, TopicRouter,
    __hasProp = Object.prototype.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor; child.__super__ = parent.prototype; return child; };

  TopicPage = (function(_super) {

    __extends(TopicPage, _super);

    function TopicPage(occupy) {}

    return TopicPage;

  })(OccupyView);

  TopicRouter = (function(_super) {

    __extends(TopicRouter, _super);

    function TopicRouter(occupy) {}

    return TopicRouter;

  })(OccupyRouter);

}).call(this);
