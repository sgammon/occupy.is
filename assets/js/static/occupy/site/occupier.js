(function() {
  var OccupierPage, OccupierRouter,
    __hasProp = Object.prototype.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor; child.__super__ = parent.prototype; return child; };

  OccupierPage = (function(_super) {

    __extends(OccupierPage, _super);

    function OccupierPage(occupy) {}

    return OccupierPage;

  })(OccupyView);

  OccupierRouter = (function(_super) {

    __extends(OccupierRouter, _super);

    function OccupierRouter(occupy) {}

    return OccupierRouter;

  })(OccupyRouter);

}).call(this);
