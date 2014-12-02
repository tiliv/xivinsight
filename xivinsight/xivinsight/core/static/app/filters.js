angular.module('xivinsight.filters', [])

.filter('padZeroes', function(){
    return function(number, padSize){
        var numberSize = ("" + number).length;
        var padding = "0000000000";
        padSize = Math.max(1, Math.min(padding.length, padSize || 1));
        var leadingPadding = padding.substr(padding.length - padSize + numberSize);
        return leadingPadding + number
    }
})
