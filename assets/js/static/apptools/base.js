(function() {
  var AppTools, CoreAPI, CoreAgentAPI, CoreDevAPI, CoreEventsAPI, CoreModelAPI, CorePushAPI, CoreRPCAPI, CoreSysAPI, CoreUserAPI, Expand, Find, Milk, Parse, TemplateCache, key;
  var __slice = Array.prototype.slice, __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; }, __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  };
  TemplateCache = {};
  Find = function(name, stack, value) {
    var ctx, i, part, parts, _i, _len, _ref, _ref2;
    if (value == null) {
      value = null;
    }
    if (name === '.') {
      return stack[stack.length - 1];
    }
    _ref = name.split(/\./), name = _ref[0], parts = 2 <= _ref.length ? __slice.call(_ref, 1) : [];
    for (i = _ref2 = stack.length - 1; _ref2 <= -1 ? i < -1 : i > -1; _ref2 <= -1 ? i++ : i--) {
      if (stack[i] == null) {
        continue;
      }
      if (!(typeof stack[i] === 'object' && name in (ctx = stack[i]))) {
        continue;
      }
      value = ctx[name];
      break;
    }
    for (_i = 0, _len = parts.length; _i < _len; _i++) {
      part = parts[_i];
      value = Find(part, [value]);
    }
    if (value instanceof Function) {
      value = (function(value) {
        return function() {
          var val;
          val = value.apply(ctx, arguments);
          return (val instanceof Function) && val.apply(null, arguments) || val;
        };
      })(value);
    }
    return value;
  };
  Expand = function() {
    var args, f, obj, tmpl;
    obj = arguments[0], tmpl = arguments[1], args = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
    return ((function() {
      var _i, _len, _results;
      _results = [];
      for (_i = 0, _len = tmpl.length; _i < _len; _i++) {
        f = tmpl[_i];
        _results.push(f.call.apply(f, [obj].concat(__slice.call(args))));
      }
      return _results;
    })()).join('');
  };
  Parse = function(template, delimiters, section) {
    var BuildRegex, buffer, buildInterpolationTag, buildInvertedSectionTag, buildPartialTag, buildSectionTag, cache, content, contentEnd, d, error, escape, isStandalone, match, name, parseError, pos, sectionInfo, tag, tagPattern, tmpl, type, whitespace, _name, _ref, _ref2, _ref3;
    if (delimiters == null) {
      delimiters = ['{{', '}}'];
    }
    if (section == null) {
      section = null;
    }
    cache = (TemplateCache[_name = delimiters.join(' ')] || (TemplateCache[_name] = {}));
    if (template in cache) {
      return cache[template];
    }
    buffer = [];
    BuildRegex = function() {
      var tagClose, tagOpen;
      tagOpen = delimiters[0], tagClose = delimiters[1];
      return RegExp("([\\s\\S]*?)([" + ' ' + "\\t]*)(?:" + tagOpen + "\\s*(?:(!)\\s*([\\s\\S]+?)|(=)\\s*([\\s\\S]+?)\\s*=|({)\\s*(\\w[\\S]*?)\\s*}|([^0-9a-zA-Z._!={]?)\\s*([\\w.][\\S]*?))\\s*" + tagClose + ")", "gm");
    };
    tagPattern = BuildRegex();
    tagPattern.lastIndex = pos = (section || {
      start: 0
    }).start;
    parseError = function(pos, msg) {
      var carets, e, endOfLine, error, indent, key, lastLine, lastTag, lineNo, parsedLines, tagStart;
      (endOfLine = /$/gm).lastIndex = pos;
      endOfLine.exec(template);
      parsedLines = template.substr(0, pos).split('\n');
      lineNo = parsedLines.length;
      lastLine = parsedLines[lineNo - 1];
      tagStart = contentEnd + whitespace.length;
      lastTag = template.substr(tagStart + 1, pos - tagStart - 1);
      indent = new Array(lastLine.length - lastTag.length + 1).join(' ');
      carets = new Array(lastTag.length + 1).join('^');
      lastLine = lastLine + template.substr(pos, endOfLine.lastIndex - pos);
      error = new Error();
      for (key in e = {
        "message": "" + msg + "\n\nLine " + lineNo + ":\n" + lastLine + "\n" + indent + carets,
        "error": msg,
        "line": lineNo,
        "char": indent.length,
        "tag": lastTag
      }) {
        error[key] = e[key];
      }
      return error;
    };
    while (match = tagPattern.exec(template)) {
      _ref = match.slice(1, 3), content = _ref[0], whitespace = _ref[1];
      type = match[3] || match[5] || match[7] || match[9];
      tag = match[4] || match[6] || match[8] || match[10];
      contentEnd = (pos + content.length) - 1;
      pos = tagPattern.lastIndex;
      isStandalone = (contentEnd === -1 || template.charAt(contentEnd) === '\n') && ((_ref2 = template.charAt(pos)) === void 0 || _ref2 === '' || _ref2 === '\r' || _ref2 === '\n');
      if (content) {
        buffer.push((function(content) {
          return function() {
            return content;
          };
        })(content));
      }
      if (isStandalone && (type !== '' && type !== '&' && type !== '{')) {
        if (template.charAt(pos) === '\r') {
          pos += 1;
        }
        if (template.charAt(pos) === '\n') {
          pos += 1;
        }
      } else if (whitespace) {
        buffer.push((function(whitespace) {
          return function() {
            return whitespace;
          };
        })(whitespace));
        contentEnd += whitespace.length;
        whitespace = '';
      }
      switch (type) {
        case '!':
          break;
        case '':
        case '&':
        case '{':
          buildInterpolationTag = function(name, is_unescaped) {
            return function(context) {
              var value, _ref3;
              if ((value = (_ref3 = Find(name, context)) != null ? _ref3 : '') instanceof Function) {
                value = Expand.apply(null, [this, Parse("" + (value()))].concat(__slice.call(arguments)));
              }
              if (!is_unescaped) {
                value = this.escape("" + value);
              }
              return "" + value;
            };
          };
          buffer.push(buildInterpolationTag(tag, type));
          break;
        case '>':
          buildPartialTag = function(name, indentation) {
            return function(context, partials) {
              var partial;
              partial = partials(name).toString();
              if (indentation) {
                partial = partial.replace(/^(?=.)/gm, indentation);
              }
              return Expand.apply(null, [this, Parse(partial)].concat(__slice.call(arguments)));
            };
          };
          buffer.push(buildPartialTag(tag, whitespace));
          break;
        case '#':
        case '^':
          sectionInfo = {
            name: tag,
            start: pos,
            error: parseError(tagPattern.lastIndex, "Unclosed section '" + tag + "'!")
          };
          _ref3 = Parse(template, delimiters, sectionInfo), tmpl = _ref3[0], pos = _ref3[1];
          sectionInfo['#'] = buildSectionTag = function(name, delims, raw) {
            return function(context) {
              var parsed, result, v, value;
              value = Find(name, context) || [];
              tmpl = value instanceof Function ? value(raw) : raw;
              if (!(value instanceof Array)) {
                value = [value];
              }
              parsed = Parse(tmpl || '', delims);
              context.push(value);
              result = (function() {
                var _i, _len, _results;
                _results = [];
                for (_i = 0, _len = value.length; _i < _len; _i++) {
                  v = value[_i];
                  context[context.length - 1] = v;
                  _results.push(Expand.apply(null, [this, parsed].concat(__slice.call(arguments))));
                }
                return _results;
              }).apply(this, arguments);
              context.pop();
              return result.join('');
            };
          };
          sectionInfo['^'] = buildInvertedSectionTag = function(name, delims, raw) {
            return function(context) {
              var value;
              value = Find(name, context) || [];
              if (!(value instanceof Array)) {
                value = [1];
              }
              value = value.length === 0 ? Parse(raw, delims) : [];
              return Expand.apply(null, [this, value].concat(__slice.call(arguments)));
            };
          };
          buffer.push(sectionInfo[type](tag, delimiters, tmpl));
          break;
        case '/':
          if (section == null) {
            error = "End Section tag '" + tag + "' found, but not in section!";
          } else if (tag !== (name = section.name)) {
            error = "End Section tag closes '" + tag + "'; expected '" + name + "'!";
          }
          if (error) {
            throw parseError(tagPattern.lastIndex, error);
          }
          template = template.slice(section.start, (contentEnd + 1) || 9e9);
          cache[template] = buffer;
          return [template, pos];
        case '=':
          if ((delimiters = tag.split(/\s+/)).length !== 2) {
            error = "Set Delimiters tags should have two and only two values!";
          }
          if (error) {
            throw parseError(tagPattern.lastIndex, error);
          }
          escape = /[-[\]{}()*+?.,\\^$|#]/g;
          delimiters = (function() {
            var _i, _len, _results;
            _results = [];
            for (_i = 0, _len = delimiters.length; _i < _len; _i++) {
              d = delimiters[_i];
              _results.push(d.replace(escape, "\\$&"));
            }
            return _results;
          })();
          tagPattern = BuildRegex();
          break;
        default:
          throw parseError(tagPattern.lastIndex, "Unknown tag type -- " + type);
      }
      tagPattern.lastIndex = pos != null ? pos : template.length;
    }
    if (section != null) {
      throw section.error;
    }
    if (template.length !== pos) {
      buffer.push(function() {
        return template.slice(pos);
      });
    }
    return cache[template] = buffer;
  };
  Milk = {
    VERSION: '1.2.0',
    helpers: [],
    partials: null,
    escape: function(value) {
      var entities;
      entities = {
        '&': 'amp',
        '"': 'quot',
        '<': 'lt',
        '>': 'gt'
      };
      return value.replace(/[&"<>]/g, function(ch) {
        return "&" + entities[ch] + ";";
      });
    },
    render: function(template, data, partials) {
      var context;
      if (partials == null) {
        partials = null;
      }
      if (!((partials || (partials = this.partials || {})) instanceof Function)) {
        partials = (function(partials) {
          return function(name) {
            if (!(name in partials)) {
              throw "Unknown partial '" + name + "'!";
            }
            return Find(name, [partials]);
          };
        })(partials);
      }
      context = this.helpers instanceof Array ? this.helpers : [this.helpers];
      return Expand(this, Parse(template), context.concat([data]), partials);
    }
  };
  if (typeof exports !== "undefined" && exports !== null) {
    for (key in Milk) {
      exports[key] = Milk[key];
    }
  } else {
    this.Milk = Milk;
  }
  CoreAPI = (function() {
    function CoreAPI() {}
    return CoreAPI;
  })();
  CoreSysAPI = (function() {
    __extends(CoreSysAPI, CoreAPI);
    function CoreSysAPI() {
      CoreSysAPI.__super__.constructor.apply(this, arguments);
    }
    return CoreSysAPI;
  })();
  CoreAgentAPI = (function() {
    __extends(CoreAgentAPI, CoreAPI);
    function CoreAgentAPI() {
      CoreAgentAPI.__super__.constructor.apply(this, arguments);
    }
    return CoreAgentAPI;
  })();
  CoreModelAPI = (function() {
    __extends(CoreModelAPI, CoreAPI);
    function CoreModelAPI() {
      CoreModelAPI.__super__.constructor.apply(this, arguments);
    }
    return CoreModelAPI;
  })();
  CoreDevAPI = (function() {
    __extends(CoreDevAPI, CoreAPI);
    function CoreDevAPI(fcm) {
      this.verbose = __bind(this.verbose, this);
      this.error = __bind(this.error, this);
      this.eventlog = __bind(this.eventlog, this);
      this.log = __bind(this.log, this);
      this.setDebug = __bind(this.setDebug, this);      this.config = {};
      this.environment = {};
      this.performance = {};
      this.debug = {
        logging: true,
        eventlog: true,
        verbose: true
      };
    }
    CoreDevAPI.prototype.setDebug = function(debug) {
      this.debug = debug;
      return console.log("[CoreDev] Debug has been set.", this.debug);
    };
    CoreDevAPI.prototype.log = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (!(context != null)) {
        context = '{no context}';
      }
      if (this.debug.logging === true) {
        console.log.apply(console, ["[" + module + "] INFO: " + message].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.eventlog = function() {
      var context, sublabel;
      sublabel = arguments[0], context = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      if (!(context != null)) {
        context = '{no context}';
      }
      if (this.debug.eventlog === true) {
        console.log.apply(console, ["[EventLog] " + sublabel].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.error = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (this.debug.logging === true) {
        console.log.apply(console, ["[" + module + "] ERROR: " + message].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.verbose = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (this.debug.verbose === true) {
        this.log.apply(this, [module, message].concat(__slice.call(context)));
      }
    };
    return CoreDevAPI;
  })();
  CoreAgentAPI = (function() {
    __extends(CoreAgentAPI, CoreAPI);
    function CoreAgentAPI(apptools) {
      this._data = {};
      this.platform = {};
      this.capabilities = {};
      if (apptools.lib.modernizr != null) {
        this.capabilities = apptools.lib.modernizr;
      }
      this._data = {
        browsers: [
          {
            string: navigator.userAgent,
            subString: "Chrome",
            identity: "Chrome"
          }, {
            string: navigator.userAgent,
            subString: "OmniWeb",
            versionSearch: "OmniWeb/",
            identity: "OmniWeb"
          }, {
            string: navigator.vendor,
            subString: "Apple",
            identity: "Safari",
            versionSearch: "Version"
          }, {
            prop: window.opera,
            identity: "Opera"
          }, {
            string: navigator.vendor,
            subString: "iCab",
            identity: "iCab"
          }, {
            string: navigator.vendor,
            subString: "KDE",
            identity: "Konqueror"
          }, {
            string: navigator.userAgent,
            subString: "Firefox",
            identity: "Firefox"
          }, {
            string: navigator.vendor,
            subString: "Camino",
            identity: "Camino"
          }, {
            string: navigator.userAgent,
            subString: "Netscape",
            identity: "Netscape"
          }, {
            string: navigator.userAgent,
            subString: "MSIE",
            identity: "Explorer",
            versionSearch: "MSIE"
          }, {
            string: navigator.userAgent,
            subString: "Gecko",
            identity: "Mozilla",
            versionSearch: "rv"
          }, {
            string: navigator.userAgent,
            subString: "Mozilla",
            identity: "Netscape",
            versionSearch: "Mozilla"
          }
        ],
        os: [
          {
            string: navigator.platform,
            subString: "Win",
            identity: "Windows"
          }, {
            string: navigator.platform,
            subString: "Mac",
            identity: "Mac"
          }, {
            string: navigator.userAgent,
            subString: "iPhone",
            identity: "iPhone/iPod"
          }, {
            string: navigator.platform,
            subString: "Linux",
            identity: "Linux"
          }
        ]
      };
    }
    CoreAgentAPI.prototype._makeMatch = function(data) {
      var prop, string, value, _i, _len, _results;
      _results = [];
      for (_i = 0, _len = data.length; _i < _len; _i++) {
        value = data[_i];
        string = value.string;
        prop = value.prop;
        this._data.versionSearchString = value.versionSearch || value.identity;
        if (string !== null) {
          if (value.string.indexOf(value.subString) !== -1) {
            return value.identity;
          }
        } else if (prop) {
          return value.identity;
        }
      }
      return _results;
    };
    CoreAgentAPI.prototype._makeVersion = function(dataString) {
      var index;
      index = dataString.indexOf(this._data.versionSearchString);
      if (index === -1) {} else {
        return parseFloat(dataString.substring(index + this._data.versionSearchString.length + 1));
      }
    };
    CoreAgentAPI.prototype.discover = function() {
      var browser, mobile, os, type, version;
      browser = this._makeMatch(this._data.browsers) || "unknown";
      version = this._makeVersion(navigator.userAgent) || this._makeVersion(navigator.appVersion) || "unknown";
      os = this._makeMatch(this._data.os) || "unknown";
      if (browser === 'iPod/iPhone' || browser === 'Android') {
        type = 'mobile';
        mobile = false;
      }
      this.platform = {
        os: os,
        type: type,
        vendor: navigator.vendor,
        product: navigator.product,
        browser: browser,
        version: version,
        flags: {
          mobile: mobile,
          webkit: $.browser.webkit,
          msie: $.browser.msie,
          opera: $.browser.opera,
          mozilla: $.browser.mozilla
        }
      };
      return this.capabilities.simple = {
        cookies: navigator.cookieEnabled,
        ajax: $.support.ajax
      };
    };
    return CoreAgentAPI;
  })();
  CoreEventsAPI = (function() {
    __extends(CoreEventsAPI, CoreAPI);
    function CoreEventsAPI(apptools) {
      this.registry = [];
      this.callchain = {};
      this.history = [];
      this.trigger = __bind(function() {
        var args, callback_directive, event, hook_error_count, hook_exec_count, result, _i, _len, _ref;
        event = arguments[0], args = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
        $.apptools.dev.verbose('Events', 'Triggered event: ', event, args, this.callchain[event]);
        if (__indexOf.call(this.registry, event) >= 0) {
          hook_exec_count = 0;
          hook_error_count = 0;
          _ref = this.callchain[event].hooks;
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            callback_directive = _ref[_i];
            try {
              if (callback_directive.once === true && callback_directive.has_run === true) {
                continue;
              } else {
                result = callback_directive.fn.apply(callback_directive, args);
                hook_exec_count++;
                this.history.push({
                  event: event,
                  callback: callback_directive,
                  args: args,
                  result: result
                });
                callback_directive.has_run = true;
              }
            } catch (error) {
              hook_error_count++;
              this.history.push({
                event: event,
                callback: callback_directive,
                args: args,
                error: error
              });
            }
          }
          return {
            executed: hook_exec_count,
            errors: hook_error_count
          };
        } else {
          return false;
        }
      }, this);
      this.register = __bind(function(name) {
        this.registry.push(name);
        this.callchain[name] = {
          hooks: []
        };
        apptools.dev.verbose('Events', 'Registered event: ', name);
        return true;
      }, this);
      this.hook = __bind(function(event, callback, once) {
        if (once == null) {
          once = false;
        }
        if (__indexOf.call(this.registry, event) < 0) {
          this.register(event);
        }
        this.callchain[event].hooks.push({
          fn: callback,
          once: once,
          has_run: false
        });
        apptools.dev.verbose('Events', 'Hook registered on event: ', event);
        return true;
      }, this);
    }
    return CoreEventsAPI;
  })();
  CoreRPCAPI = (function() {
    __extends(CoreRPCAPI, CoreAPI);
    function CoreRPCAPI() {
      CoreRPCAPI.__super__.constructor.apply(this, arguments);
    }
    return CoreRPCAPI;
  })();
  CorePushAPI = (function() {
    __extends(CorePushAPI, CoreAPI);
    function CorePushAPI() {
      CorePushAPI.__super__.constructor.apply(this, arguments);
    }
    return CorePushAPI;
  })();
  CoreUserAPI = (function() {
    __extends(CoreUserAPI, CoreAPI);
    function CoreUserAPI() {
      CoreUserAPI.__super__.constructor.apply(this, arguments);
    }
    return CoreUserAPI;
  })();
  AppTools = (function() {
    function AppTools(window) {
      this.lib = {};
      this.lib.modernizr = window.Modernizr;
      this.load = __bind(function(fragment) {
        return this.lib.modernizr.load(fragment);
      }, this);
      this.lib.backbone = window.Backbone;
      this.lib.lawnchair = window.Lawnchair;
      this.dev = new CoreDevAPI(this);
      this.agent = new CoreAgentAPI(this);
      this.agent.discover();
      this.events = new CoreEventsAPI(this);
      this.events.register('PLATFORM_INIT');
      this.events.register('PLATFORM_READY');
      this.user = new CoreUserAPI(this);
      this.api = new CoreRPCAPI(this);
      this.push = new CorePushAPI(this);
      return this;
    }
    return AppTools;
  })();
  window.apptools = new AppTools(window);
  if (typeof $ !== "undefined" && $ !== null) {
    $.extend({
      apptools: window.apptools
    });
  }
}).call(this);
