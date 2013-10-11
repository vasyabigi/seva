"use strict"
angular.module("seva.directives", []).directive "rating", ->
  restrict: "A"
  template: "<ul class=\"rating\">" + "<li ng-repeat=\"star in stars\" ng-class=\"star\">" + "★" + "</li>" + "</ul>"
  scope:
    ratingValue: "=rating"
    max: "="

  link: (scope) ->
    scope.stars = []
    i = 0

    while i < scope.max
      scope.stars.push filled: i < scope.ratingValue
      i++
