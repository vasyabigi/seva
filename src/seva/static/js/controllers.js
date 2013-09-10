'use strict';

angular.module('seva.controllers', []).
  controller('IndexCtrl', ['$scope', '$log', '$http', '$rootScope', function($scope, $log, $http, $rootScope){
      $http.get('/api/v1/technology/?format=json').
        success(function(data){
          $scope.technologies = data.objects;
        });
      $http.get('/api/v1/users/').
        success(function(data){
          $rootScope.users = data.objects;
        });
     }])
  .controller('UserDetails', [function() {
     alert('ok'); 
      }])
  .controller('TechnologyDetails', [function() {

      }]);
