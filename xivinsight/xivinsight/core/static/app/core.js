angular.module('xivinsight.core', [
    'xivinsight.services.SiteConfiguration',
    'xivinsight.filters',
    'xivinsight.api'
])

.factory('Session', function($rootScope){
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
    var apiSource = Restangular.all('encounter').getList();
    $scope.objects = apiSource.$object;  // to be filled when api call finishes

    this.activateEncounter = function(encounter){
        Session.setEncounter(encounter);
    }
    this.deleteEncounter = function(encounter){
        Restangular.one('encounter', encounter.encid).remove();
    }
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
            console.log(listController);
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
        var swingsDirectory = Restangular.one('encounter', Session.data.encounter.encid);
        apiSource = swingsDirectory.one('gcd').get();

        data.swings = {};
        data.swings.gcd = apiSource.$object;
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
