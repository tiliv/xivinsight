angular.module('xivinsight.services.SiteConfiguration', [])

.factory('SiteConfiguration', function(){
    return {
        STATIC_URL: window._STATIC_URL,
        IMAGE_URL: window._STATIC_URL + 'img/',
        TEMPLATE_URL: window._STATIC_URL + 'templates/'
    }
})
