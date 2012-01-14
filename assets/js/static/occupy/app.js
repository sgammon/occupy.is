(function() {
  var ChartsController, Comment, FeedController, KindCollection, ModelController, Movement, ObjectCollection, Occupier, Occupy, OccupyCollection, OccupyController, OccupyModel, OccupyRouter, OccupyView, RealtimeController, SocialController, Star, Topic, UploadController, WorkerController,
    __hasProp = Object.prototype.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor; child.__super__ = parent.prototype; return child; },
    __indexOf = Array.prototype.indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  OccupyController = (function() {

    function OccupyController() {}

    return OccupyController;

  })();

  OccupyView = (function(_super) {

    __extends(OccupyView, _super);

    function OccupyView() {
      OccupyView.__super__.constructor.apply(this, arguments);
    }

    return OccupyView;

  })(Backbone.View);

  OccupyModel = (function(_super) {

    __extends(OccupyModel, _super);

    function OccupyModel(object, register) {
      if (register == null) register = true;
      this.kind = this.__proto__.constructor.name;
      OccupyModel.__super__.constructor.call(this, object);
      if (((object != null ? object.key : void 0) != null) && register) {
        this.register(key);
      }
      return this;
    }

    OccupyModel.prototype.register = function(key) {
      $.apptools.dev.verbose('ModelRegistry', 'Registering model.', this.__proto__.constructor.name, this);
      $.occupy.models.register(this.kind, key, this);
    };

    OccupyModel.prototype._parseListResponse = function(response) {
      var models, object, record, records, _i, _len;
      records = response[this.kind.toLowerCase() + 's'];
      $.apptools.dev.verbose('OccupyModel', 'Parsing "list" response.', response, this.kind.toLowerCase() + 's');
      models = [];
      for (_i = 0, _len = records.length; _i < _len; _i++) {
        record = records[_i];
        $.apptools.dev.verbose('OccupyModel', 'Making object.', record);
        object = this._makeObject(record);
        $.apptools.dev.verbose('OccupyModel', 'Made object.', object);
        models.push(object);
      }
      return models;
    };

    OccupyModel.prototype._makeObject = function(object) {
      object = new this(object, true);
      return object;
    };

    OccupyModel.prototype.list = function(params, callbacks) {
      var injected_callbacks, request,
        _this = this;
      request = $.apptools.api[this.kind.toLowerCase()].list(params);
      injected_callbacks = {
        success: function(response) {
          var objects;
          objects = _this._parseListResponse(response);
          if ((callbacks != null ? callbacks.success : void 0) != null) {
            return callbacks.success(objects, response);
          }
        },
        failure: function(error) {
          $.apptools.dev.error('ModelList', 'Error encountered listing models of kind "' + _this.kind + '".', params, request, _this);
          if ((callbacks != null ? callbacks.failure : void 0) != null) {
            return callbacks.failure(error);
          }
        }
      };
      return request.fulfill(injected_callbacks);
    };

    OccupyModel.prototype.get = function(params, callbacks) {
      var injected_callbacks, request,
        _this = this;
      request = $.apptools.api[this.kind.toLowerCase()].get(params);
      injected_callbacks = {
        success: function(response) {
          var object;
          object = _this._makeObject(response[_this.kind.toLowerCase()]);
          if ((callbacks != null ? callbacks.success : void 0) != null) {
            return callbacks.success(object, response);
          }
        },
        failure: function(error) {
          $.apptools.dev.error('ModelGet', 'Error encountered getting model of kind "' + _this.kind + '".', params, request, _this);
          if ((callbacks != null ? callbacks.failure : void 0) != null) {
            return callbacks.failure(error);
          }
        }
      };
      return request.fulfill(injected_callbacks);
    };

    OccupyModel.prototype["new"] = function(params, callbacks) {
      var injected_callbacks, request,
        _this = this;
      request = $.apptools.api[this.kind.toLowerCase()].get(params);
      injected_callbacks = {
        success: function(response) {
          var object;
          object = _this._makeObject(response);
          if ((callbacks != null ? callbacks.success : void 0) != null) {
            return callbacks.success(object, response);
          }
        },
        failure: function(error) {
          $.apptools.dev.error('ModelNew', 'Error encountered creating model of kind "' + _this.kind + '".', params, request, _this);
          if ((callbacks != null ? callbacks.failure : void 0) != null) {
            return callbacks.failure(error);
          }
        }
      };
      return request.fulfill(injected_callbacks);
    };

    return OccupyModel;

  })(Backbone.Model);

  OccupyRouter = (function(_super) {

    __extends(OccupyRouter, _super);

    function OccupyRouter() {
      OccupyRouter.__super__.constructor.apply(this, arguments);
    }

    return OccupyRouter;

  })(Backbone.Router);

  OccupyCollection = (function(_super) {

    __extends(OccupyCollection, _super);

    function OccupyCollection() {
      OccupyCollection.__super__.constructor.apply(this, arguments);
    }

    return OccupyCollection;

  })(Backbone.Collection);

  if (typeof window !== "undefined" && window !== null) {
    window.OccupyController = OccupyController;
    window.OccupyView = OccupyView;
    window.OccupyModel = OccupyModel;
    window.OccupyRouter = OccupyRouter;
    window.OccupyCollection = OccupyCollection;
  }

  Topic = (function(_super) {

    __extends(Topic, _super);

    function Topic() {
      Topic.__super__.constructor.apply(this, arguments);
    }

    return Topic;

  })(OccupyModel);

  Occupier = (function(_super) {

    __extends(Occupier, _super);

    function Occupier() {
      Occupier.__super__.constructor.apply(this, arguments);
    }

    return Occupier;

  })(OccupyModel);

  Movement = (function(_super) {

    __extends(Movement, _super);

    function Movement() {
      Movement.__super__.constructor.apply(this, arguments);
    }

    return Movement;

  })(OccupyModel);

  Comment = (function(_super) {

    __extends(Comment, _super);

    function Comment() {
      Comment.__super__.constructor.apply(this, arguments);
    }

    return Comment;

  })(OccupyModel);

  Star = (function(_super) {

    __extends(Star, _super);

    function Star() {
      Star.__super__.constructor.apply(this, arguments);
    }

    return Star;

  })(OccupyModel);

  KindCollection = (function(_super) {

    __extends(KindCollection, _super);

    function KindCollection() {
      KindCollection.__super__.constructor.apply(this, arguments);
    }

    return KindCollection;

  })(OccupyCollection);

  ObjectCollection = (function(_super) {

    __extends(ObjectCollection, _super);

    function ObjectCollection() {
      ObjectCollection.__super__.constructor.apply(this, arguments);
    }

    return ObjectCollection;

  })(OccupyCollection);

  ModelController = (function(_super) {

    __extends(ModelController, _super);

    function ModelController(occupy) {
      this.classes = {
        Topic: Topic,
        Occupier: Occupier,
        Movement: Movement,
        Comment: Comment,
        Star: Star
      };
      this.index = {
        by_key: {
          _map: {},
          add: function(key, index) {
            return this._map[key] = index;
          },
          find: function(key) {
            if (__indexOf.call(this._map, key) >= 0) {
              return this._map[key];
            } else {
              return false;
            }
          }
        },
        by_query: {}
      };
      this.state = {
        last_error: null,
        last_request: null,
        last_response: null
      };
      this.objects = {
        count: 0,
        _data: {},
        _kind: {}
      };
    }

    ModelController.prototype.register = function(kind, key, object) {
      var index, model;
      $.apptools.dev.verbose('Models', 'Registering model.', kind, key, object);
      model = new this.classes[kind](object);
      if (!this.objects._kind[kind].add([model])) {
        this.objects._kind[kind] = new KindCollection({
          model: this.classes[kind]
        });
      }
      index = this.objects._kind[kind].add([model]);
      this.objects._data[key] = object;
      return this.index.by_key.add(key, index);
    };

    ModelController.prototype.get = function(key) {
      return this.objects._data[key];
    };

    return ModelController;

  })(OccupyController);

  if (typeof window !== "undefined" && window !== null) {
    window.Topic = Topic;
    window.Occupier = Occupier;
    window.Movement = Movement;
    window.Comment = Comment;
    window.Star = Star;
    window.KindCollection = KindCollection;
    window.ObjectCollection = ObjectCollection;
    window.ModelController = ModelController;
  }

  FeedController = (function(_super) {

    __extends(FeedController, _super);

    function FeedController(occupy) {}

    return FeedController;

  })(OccupyController);

  RealtimeController = (function(_super) {

    __extends(RealtimeController, _super);

    function RealtimeController(occupy) {}

    return RealtimeController;

  })(OccupyController);

  WorkerController = (function(_super) {

    __extends(WorkerController, _super);

    function WorkerController(occupy) {}

    return WorkerController;

  })(OccupyController);

  ChartsController = (function(_super) {

    __extends(ChartsController, _super);

    function ChartsController(occupy) {}

    return ChartsController;

  })(OccupyController);

  SocialController = (function(_super) {

    __extends(SocialController, _super);

    function SocialController(occupy) {}

    return SocialController;

  })(OccupyController);

  UploadController = (function(_super) {

    __extends(UploadController, _super);

    function UploadController(occupy) {}

    return UploadController;

  })(OccupyController);

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
