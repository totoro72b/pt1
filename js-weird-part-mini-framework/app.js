var g = G$("john", "doe");
g.setLang('es');

// listen to login click
$("#login").click(function () {
    // chaining!
  g.setLang($('#lang').val()).htmlGreet('#greeting', true).log();
});
