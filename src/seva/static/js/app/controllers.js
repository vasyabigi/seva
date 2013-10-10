'use strict';

angular.module('seva.controllers', []).
  controller('IndexCtrl', ['$scope', '$log', '$http', '$rootScope', function($scope, $log, $http, $rootScope){
    $http.get('/api/v1/technology/?format=json').success(function(data){
      $scope.technologies = data.objects;
    });

    $http.get('/api/v1/users/').success(function(data){
      $rootScope.users = data.objects;
    });

  }]).
  controller('UserDetails', ['$scope', '$log', '$http', '$routeParams', function($scope, $log, $http, $routeParams) {
    $http.get('/api/v1/users/'+$routeParams.username).success(function(data){
      $scope.user = data;
    });

  }]).
  controller('TechnologyDetails', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams) {
    $http.get('/api/v1/technology/'+$routeParams.tech+'?format=json').success(function(data){
      $scope.technology = data;
    });

  }]);
