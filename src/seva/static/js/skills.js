$(document).ready(function() {
  $("header nav a").click(function(){
    $("article.user").fadeOut();
    $($(this).attr("href")).fadeIn();
    return false;
  })
});
