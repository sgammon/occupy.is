(function() {
  var OccupierPage, OccupierRouter;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  OccupierPage = (function() {
    __extends(OccupierPage, OccupyView);
    function OccupierPage(occupy) {}
    return OccupierPage;
  })();
  OccupierRouter = (function() {
    __extends(OccupierRouter, OccupyRouter);
    function OccupierRouter(occupy) {}
    return OccupierRouter;
  })();
}).call(this);
