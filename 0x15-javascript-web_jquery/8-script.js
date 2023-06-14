#!/usr/bin/node

$(document).ready(function() {
  $("ul#list_movies").click(function() {
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
      data.results.forEach(function(movie) {
        $("<li>").text(movie.title).appendTo("ul#list_movies");
      });
    });
  });
});

