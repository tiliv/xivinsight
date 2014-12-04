import django.db.models

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models, serializers, utils

filter_types = {
    django.db.models.CharField: ['icontains', 'iexact'],
    django.db.models.IntegerField: ['exact'],
}

class FieldFilterMixin(object):
    pass
    # def get_queryset(self):
    #     queryset = self.queryset
    #     model = queryset.model
    #     queryset_filters = {}
    #     for f in model._meta.local_fields:
    #         if f.name not in self.request.QUERY_PARAMS:
    #             continue
    #         field_search = self.request.QUERY_PARAMS[f.name]
    #
    #         for field_type, filters in filter_types.items():
    #             if not isinstance(f, field_type):
    #                 continue
    #             for filter in filters:
    #                 k = f.name + "__" + filter
    #                 queryset_filters[k] = field_search
    #     return queryset.filter(**queryset_filters)

class AttackTypeViewSet(FieldFilterMixin, viewsets.ModelViewSet):
    queryset = models.AttackType.objects.all()
    serializer_class = serializers.AttackTypeSerializer

class CombatantViewSet(FieldFilterMixin, viewsets.ModelViewSet):
    queryset = models.Combatant.objects.all()
    serializer_class = serializers.CombatantSerializer

class CurrentViewSet(FieldFilterMixin, viewsets.ModelViewSet):
    queryset = models.Current.objects.all()
    serializer_class = serializers.CurrentSerializer

class DamageTypeViewSet(FieldFilterMixin, viewsets.ModelViewSet):
    queryset = models.DamageType.objects.all()
    serializer_class = serializers.DamageTypeSerializer

class EncounterViewSet(FieldFilterMixin, viewsets.ModelViewSet):
    queryset = models.Encounter.objects.all()
    serializer_class = serializers.EncounterSerializer

    @detail_route()
    def gcd(self, request, pk):
        """
        Return the set of swings for this enounter that qualify for analysis as a core rotation.
        """
        queryset = models.Swing.objects.filter(encid=pk).gcd().analyze_fields()
        serializer = serializers.SwingSerializer(queryset, many=True)
        return Response(serializer.data)

class SwingViewSet(FieldFilterMixin, viewsets.ModelViewSet):
    queryset = models.Swing.objects.all()
    serializer_class = serializers.SwingSerializer

    def destroy(self, request, pk=None):
        print('--- destroy requested pk=', pk)
