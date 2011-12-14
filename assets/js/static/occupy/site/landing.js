(function() {
  var LandingPage, LandingRouter;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  LandingPage = (function() {
    __extends(LandingPage, OccupyView);
    function LandingPage(occupy) {}
    return LandingPage;
  })();
  LandingRouter = (function() {
    __extends(LandingRouter, OccupyRouter);
    function LandingRouter(occupy) {}
    return LandingRouter;
  })();
}).call(this);
