angular.module('xivinsight.core', [
    'ngCookies',
    'xivinsight.services.SiteConfiguration',
    'xivinsight.filters',
    'xivinsight.api'
])

.run(function($http, $cookies){
    var csrf_header = {'X-CSRFToken': $cookies.csrftoken}
    $http.defaults.headers['delete'] = {};
    angular.extend($http.defaults.headers.post, csrf_header);
    angular.extend($http.defaults.headers.put, csrf_header);
    angular.extend($http.defaults.headers.delete, csrf_header);
})

.factory('Session', function(){
    var data = {
        'encounter': null
    };

    function setEncounter(encounter){
        console.log("Setting encounter to", encounter);
        data['encounter'] = encounter;
    }

    return {
        'data': data,
        'setEncounter': setEncounter
    };
})

.controller('XIVINSIGHT', function($rootScope, Session){
    $rootScope.session = Session;
})

// <encounter-list>
.controller('EncounterList', function($scope, Restangular, Session){
    var apiSource = null;
    function _getApiSource(){
        apiSource = Restangular.all('encounter').getList();
        $scope.objects = apiSource.$object;  // to be filled when api call finishes
    }

    this.activateEncounter = function(encounter){
        Session.setEncounter(encounter);
    }
    this.deleteEncounter = function(encounter){
        Restangular.one('encounter', encounter.encid).remove();
        if (Session.data.encounter == encounter) {
            Session.setEncounter(null);
        }
        var i = $scope.objects.indexOf(encounter);
        $scope.objects.splice(i, 1);
    }

    _getApiSource();
})
.directive('encounterList', function(SiteConfiguration){
    return {
        restrict: 'E',
        controller: 'EncounterList',
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'encounter/list.html'
    }
})

// <encounter-item>
.controller('EncounterItem', function(){
})
.directive('encounterItem', function(SiteConfiguration){
    return {
        restrict: 'EA',
        controller: 'EncounterItem',
        require: '^encounterList',
        replace: true,  // the bootstrap a.list-group-item is hard :'(
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'encounter/list_item.html',
        scope: {
            "encounter": '=',
        },
        link: function(scope, element, attrs, listController){
            var fn = {
                activate: function(){
                    listController.activateEncounter(scope.encounter);
                },
                delete: function(){
                    listController.deleteEncounter(scope.encounter);
                }
            }

            // Publish to scope
            angular.extend(scope, fn);
        }
    }
})

// <active-encounter>
.controller('ActiveEncounter', function($scope, Restangular, Session){
    var apiSource = null;
    var data = {
        'encounter': null,
        'allSwings': []
    };
    function _getApiSource(){
        apiSource = Restangular.all('combatant').getList({
            'encid': Session.data.encounter.encid
        });

        data = {};
        data.combatants = apiSource.$object;
    }

    this.clearEncounter = function(){
        Session.setEncounter(null);
    }
    this.loadEncounter = function(){
        // Called by <active-encounter> $watch() every time the session encounter changes
        var encounter = Session.data.encounter;
        data.encounter = encounter;

        if (encounter === null) {
            this.clearEncounter();
            return;
        }

        _getApiSource();

        // Update all of the scope references
        angular.extend($scope, data);
    }
})
.directive('activeEncounter', function(SiteConfiguration, Session){
    return {
        restrict: 'E',
        controller: 'ActiveEncounter',
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'encounter/active_panel.html',
        scope: true,
        link: function(scope, element, attrs, controller){
            scope.$watch(function(){ return Session.data.encounter; }, function(newVal, oldVal, scope){
                controller.loadEncounter();
            });
        }
    }
})

// <swing-list>
.controller('SwingList', function($scope){
    
})
.directive('swingList', function(SiteConfiguration){
    return {
        restrict: 'E',
        controller: 'SwingList',
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'swing/list.html',
        scope: {
            "objects": '=swings'
        }
    }
})

// <swing-item>
.controller('SwingItem', function(){
    
})
.directive('swingItem', function(SiteConfiguration){
    return {
        restrict: 'E',
        controller: 'SwingItem',
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'swing/list_item.html',
        scope: {
            "swing": '='
        }
    }
})
.directive('swingIcon', function(SiteConfiguration){
    function getAttackImageName(attacktype){
        var name = attacktype.toLowerCase().replace(" (*)", "_tick").replace(/ /g, '_');
        return SiteConfiguration.IMAGE_URL + name + ".png";
    }

    return {
        restrict: 'A',
        link: function(scope, element, attrs, controller){
            attrs.$set('src', getAttackImageName(scope.swing.attacktype));
        }
    }
})

// <swing-list>
.controller('CombatantList', function($scope){
    
})
.directive('combatantList', function(SiteConfiguration){
    return {
        restrict: 'E',
        controller: 'SwingList',
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'combatant/list.html',
        scope: {
            "objects": '=combatants'
        }
    }
})

// <swing-item>
.controller('Combatant', function(){
    
})
.directive('combatant', function(SiteConfiguration){
    return {
        restrict: 'E',
        controller: 'SwingItem',
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'combatant/list_item.html',
        scope: {
            "combatant": '='
        }
    }
})
.directive('swingIcon', function(SiteConfiguration){
    function getAttackImageName(attacktype){
        var name = attacktype.toLowerCase().replace(" (*)", "_tick").replace(/ /g, '_');
        return SiteConfiguration.IMAGE_URL + name + ".png";
    }

    return {
        restrict: 'A',
        link: function(scope, element, attrs, controller){
            attrs.$set('src', getAttackImageName(scope.swing.attacktype));
        }
    }
})
