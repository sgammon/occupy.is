(function() {
  var TopicPage, TopicRouter;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  TopicPage = (function() {
    __extends(TopicPage, OccupyView);
    function TopicPage(occupy) {}
    return TopicPage;
  })();
  TopicRouter = (function() {
    __extends(TopicRouter, OccupyRouter);
    function TopicRouter(occupy) {}
    return TopicRouter;
  })();
}).call(this);
