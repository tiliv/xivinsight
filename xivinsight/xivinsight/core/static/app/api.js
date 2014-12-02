angular.module('xivinsight.api', ['restangular'])

.config(function(RestangularProvider){
    RestangularProvider.setBaseUrl('/api/act');
    RestangularProvider.setRequestSuffix('/');
})
