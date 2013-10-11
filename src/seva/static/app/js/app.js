'use strict';

angular.module('seva', ['seva.controllers', 'ui.gravatar', 'seva.directives']).
  config(function($routeProvider) {
    $routeProvider.when('/index', {
      templateUrl: '/static/app/tmpl/company-avg.html',
      controller: 'IndexCtrl'
    });
    $routeProvider.when('/user/:username', {
        templateUrl: '/static/app/tmpl/user-details.html',
        controller: 'UserDetails'
      });
    $routeProvider.when('/technology/:tech', {
        templateUrl: '/static/app/tmpl/technology-details.html',
        controller: 'TechnologyDetails'
      });
    $routeProvider.otherwise({redirectTo: '/index'});
  });
