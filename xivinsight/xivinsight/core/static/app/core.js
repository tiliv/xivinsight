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
.controller('EncounterList', function($scope, Restangular){
    var apiSource = Restangular.all('encounter').getList();
    $scope.objects = apiSource.$object;  // to be filled when api call finishes
})
.directive('encounterList', function(SiteConfiguration){
    return {
        restrict: 'E',
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'encounter/list.html'
    }
})

// <encounter-item>
.controller('EncounterItem', function(Session){
    this.activateEncounter = function(encounter){
        Session.setEncounter(encounter);
    }
})
.directive('encounterItem', function(SiteConfiguration){
    return {
        restrict: 'EA',
        controller: 'EncounterItem',
        replace: true,  // the bootstrap a.list-group-item is hard :'(
        templateUrl: SiteConfiguration.TEMPLATE_URL + 'encounter/list_item.html',
        scope: {
            "encounter": '=',
            "itemController": '='
        },
        link: function(scope, element, attrs, controller){
            function activate(){
                controller.activateEncounter(scope.encounter);
            }

            // Publish to scope
            scope.activate = activate;
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
        apiSource = Restangular.all('swing').getList({
            encid: Session.data.encounter.encid,
        });
        // TODO: Split all of these into their viewable categories
        data.allSwings = apiSource.$object;
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
        scope: true
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
        var name = attacktype.toLowerCase().replace(" (*)", "_tick").replace(" ", '_');
        return SiteConfiguration.IMAGE_URL + name + ".png";
    }

    return {
        restrict: 'A',
        link: function(scope, element, attrs, controller){
            attrs.$set('src', getAttackImageName(scope.swing.attacktype));
        }
    }
})
