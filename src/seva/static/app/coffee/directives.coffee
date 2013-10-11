"use strict"
angular.module("seva.directives", []).directive "rating", ->
  restrict: "A"
  template: "<figure class='rating'><span ng-repeat='star in stars' ng-class='star'>★</span></figure>"
  scope:
    ratingValue: "=rating"
    max: "="

  link: (scope) ->
    scope.stars = []
    i = 0

    while i < scope.max
      scope.stars.push filled: i < scope.ratingValue
      i++
