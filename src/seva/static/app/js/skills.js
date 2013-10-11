$(document).ready(function() {
  'use strict';

  $("header nav a").click(function() {
    $("article.user").fadeOut();
    $($(this).attr("href")).fadeIn();
    return false;
  });
});
