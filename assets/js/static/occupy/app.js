(function() {
  var FeedController, ModelController, Occupy, OccupyCollection, OccupyController, OccupyModel, OccupyRouter, OccupyView, RealtimeController, SocialController, UploadController, WorkerController;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  OccupyController = (function() {
    function OccupyController() {}
    return OccupyController;
  })();
  OccupyView = (function() {
    __extends(OccupyView, Backbone.View);
    function OccupyView() {
      OccupyView.__super__.constructor.apply(this, arguments);
    }
    return OccupyView;
  })();
  OccupyModel = (function() {
    __extends(OccupyModel, Backbone.Model);
    function OccupyModel() {
      OccupyModel.__super__.constructor.apply(this, arguments);
    }
    return OccupyModel;
  })();
  OccupyRouter = (function() {
    __extends(OccupyRouter, Backbone.Router);
    function OccupyRouter() {
      OccupyRouter.__super__.constructor.apply(this, arguments);
    }
    return OccupyRouter;
  })();
  OccupyCollection = (function() {
    __extends(OccupyCollection, Backbone.Collection);
    function OccupyCollection() {
      OccupyCollection.__super__.constructor.apply(this, arguments);
    }
    return OccupyCollection;
  })();
  if (typeof window !== "undefined" && window !== null) {
    window.OccupyController = OccupyController;
    window.OccupyView = OccupyView;
    window.OccupyModel = OccupyModel;
    window.OccupyRouter = OccupyRouter;
    window.OccupyCollection = OccupyCollection;
  }
  ModelController = (function() {
    __extends(ModelController, OccupyController);
    function ModelController(occupy) {}
    return ModelController;
  })();
  WorkerController = (function() {
    __extends(WorkerController, OccupyController);
    function WorkerController(occupy) {}
    return WorkerController;
  })();
  FeedController = (function() {
    __extends(FeedController, OccupyController);
    function FeedController(occupy) {}
    return FeedController;
  })();
  RealtimeController = (function() {
    __extends(RealtimeController, OccupyController);
    function RealtimeController(occupy) {}
    return RealtimeController;
  })();
  SocialController = (function() {
    __extends(SocialController, OccupyController);
    function SocialController(occupy) {}
    return SocialController;
  })();
  UploadController = (function() {
    __extends(UploadController, OccupyController);
    function UploadController(occupy) {}
    return UploadController;
  })();
  Occupy = (function() {
    function Occupy(config) {
      this.config = config;
      this.upload = new UploadController(this);
      this.workers = new WorkerController(this);
      this.realtime = new RealtimeController(this);
      this.feed = new FeedController(this);
      this.social = new SocialController(this);
      this.models = new ModelController(this);
      return this;
    }
    return Occupy;
  })();
  window.occupy = new Occupy();
  if (typeof $ !== "undefined" && $ !== null) {
    $.extend({
      occupy: window.occupy
    });
  }
}).call(this);
