(function (global, $) {
  var Greetr = function (first, last, language) {
      // use new here so the caller doesn't have to
    return new Greetr.init(first, last, language);
  };
  var supportedLangs = ["en", "es"];

  var greetings = {
    en: "Hello",
    es: "Hola",
  };

  var formalGreetings = {
    en: "Greetings",
    es: "Saludos",
  };

  var logMessages = {
    en: "Logged in",
    es: "Inicio sesion",
  };

  // prototypes that all objects will point to
  Greetr.prototype = {
    fullName: function () {
      return this.first + " " + this.last;
    },
    validate: function () {
      if (supportedLangs.indexOf(this.language) === -1) {
        throw "Invalid Language";
      }
    },
    greeting: function () {
      return greetings[this.language] + " " + this.first + "!";
    },
    formalGreetings: function () {
      return formalGreetings[this.language] + ", " + this.fullName();
    },
    getGreetStr(formal) {
      if (formal) {
        return this.formalGreetings();
      }
      return this.greeting();
    },
    greet: function (formal) {
      var msg = this.getGreetStr(formal);
      if (console) {
        console.log(msg);
      }
      // this refers to the calling obj at execution time
      // make the method chainable
      return this;
    },
    htmlGreet: function(selectorStr, formal){
        var msg = this.getGreetStr(formal);
        $(selectorStr).html(msg);
        return this;
    },
    log: function () {
      if (console) {
        console.log(logMessages[this.language] + ": " + this.fullName());
      }
      return this;
    },
    setLang: function (lang) {
      this.language = lang;
      this.validate();
      return this;
    },
  };

  Greetr.init = function (first, last, language) {
    var self = this;
    self.first = first || "";
    self.last = last || "";
    self.language = language || "en";
    self.validate();
  };
  Greetr.init.prototype = Greetr.prototype;
  // so we can use Greetr or G$
  global.Greetr = global.G$ = Greetr;
})(window, jQuery);
