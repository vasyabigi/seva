'use strict';

angular.module('seva.directives', [])
  .directive('rating', function () {
    return {
        restrict: 'A',
        template: '<ul class="rating">' +
                    '<li ng-repeat="star in stars" ng-class="star">' +
                      '\u2605' +
                    '</li>' +
                  '</ul>',
        scope: {
            ratingValue: '=rating',
            max: '=',
        },
        link: function (scope) {
            scope.stars = [];
            for (var  i = 0; i < scope.max; i++) {
                scope.stars.push({filled: i < scope.ratingValue });
            }
        }
    };
});
