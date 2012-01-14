(function() {
  var MovementPage, MovementRouter,
    __hasProp = Object.prototype.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor; child.__super__ = parent.prototype; return child; };

  MovementPage = (function(_super) {

    __extends(MovementPage, _super);

    function MovementPage(occupy) {}

    return MovementPage;

  })(OccupyView);

  MovementRouter = (function(_super) {

    __extends(MovementRouter, _super);

    function MovementRouter(occupy) {}

    return MovementRouter;

  })(OccupyRouter);

}).call(this);
